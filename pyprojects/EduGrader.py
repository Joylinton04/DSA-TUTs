# -*- coding: utf-8 -*-
"""
Created on Sun May 11 12:32:07 2025

@author: Bloyd-247
"""

import cv2
import numpy as np
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image
import tempfile
import shutil
import io

# Colors
BLUE = '#1E1EBE'
WHITE = '#FFFFFF'
ORANGE = '#F57C00'

# Global variables
image_dir = ""
key_file = ""
output_dir = ""
root = None
status_var = None
progress = None
progress_label = None

def show_menu():
    menu = tk.Toplevel(root)
    menu.title("Menu")
    menu.geometry("200x150")
    
    tk.Button(menu, text="Settings", command=lambda: None).pack(fill=tk.X, pady=2)
    tk.Button(menu, text="Help", command=show_help).pack(fill=tk.X, pady=2)
    tk.Button(menu, text="About", command=show_about).pack(fill=tk.X, pady=2)

def show_about():
    messagebox.showinfo("About", "KNUST Scannable Sheet Marker\nStudent Project 2025")

def show_help():
    messagebox.showinfo(
        "Help",
        f"-Save scan sheets in a folder.Choose the folder by clicking on browse against scan sheet folder.\n"
        f"-Save marking scheme as csv file and choose marking scheme by clicking on browse against marking scheme csv file.\n"
        f"-Select folder for total outputs.\n"
        f"-Click on Grade sheets to Grade.\n"
    )
    
def select_image_dir():
    global image_dir
    dir_path = filedialog.askdirectory(title="Select Folder with KNUST Scan sheet Images")
    if dir_path:
        img_dir_var.set(dir_path)
        image_dir = dir_path

def select_key_file():
    global key_file
    file_path = filedialog.askopenfilename(
        title="Select Marking Scheme CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if file_path:
        key_file_var.set(file_path)
        key_file = file_path

def select_output_dir():
    global output_dir
    dir_path = filedialog.askdirectory(title="Select Output Folder for Grading Reports")
    if dir_path:
        output_dir_var.set(dir_path)
        output_dir = dir_path

def update_status(message):
    status_var.set(message)
    root.update_idletasks()

def update_progress(value, max_value=None):
    if max_value:
        progress['maximum'] = max_value
    progress['value'] = value
    progress_label.config(text=f"Processing: {value}/{progress['maximum']}")
    root.update_idletasks()

def load_answer_key_from_csv(path):
    try:
        df = pd.read_csv(path)
        letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        return {int(row["Question"]) - 1: letter_to_index[row["Answer"].strip().upper()] for _, row in df.iterrows()}
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load answer key:\n{str(e)}")
        return None

def load_image(path):
    try:
        image = cv2.imread(path)
        if image is None:
            raise ValueError(f"Could not read image file: {path}")
        image = cv2.resize(image, (1500, 2100))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
        return image, thresh
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image {os.path.basename(path)}:\n{str(e)}")
        return None, None

def extract_answers(thresh, num_questions=30, choices=5):
    questions = []
    box_width = 90
    box_height = 30
    
    columns = [
        {"x": 115, "y": 1010},   # Column 1 (Questions 1-6)
        {"x": 115 + 150, "y": 1010},  # Column 2 (Questions 7-12)
        {"x": 115 + 300, "y": 1010},  # Column 3 (Questions 13-18)
        {"x": 115 + 450, "y": 1010},  # Column 4 (Questions 19-24)
        {"x": 115 + 600, "y": 1010}    # Column 5 (Questions 25-30)
    ]
    
    final_answers = [-1] * num_questions
    
    for col_idx, col in enumerate(columns):
        x1, y1 = col["x"], col["y"]
        for q_in_col in range(6):  # 6 questions per column
            q_num = col_idx * 6 + q_in_col
            if q_num >= num_questions:
                break
                
            counts = []
            for choice in range(choices):
                top = y1 + q_in_col * choices * box_height + choice * box_height
                bottom = top + box_height
                right = x1 + box_width
                box = thresh[top:bottom, x1:right]
                counts.append(cv2.countNonZero(box))
            
            if counts:
                selected = np.argmax(counts)
                final_answers[q_num] = selected if counts[selected] >= 150 else -1
    
    return final_answers

def grade(answers, key):
    report = []
    score = 0
    for i, a in enumerate(answers):
        correct = key.get(i, -1)
        match = a == correct
        score += match
        report.append((i + 1, a, correct, match))
    return score, report

def save_report(report, output_path):
    letter_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", -1: "None"}
    df = pd.DataFrame([{
        "Question": q,
        "Selected": letter_map.get(sel, "None"),
        "Correct": letter_map.get(corr, "None"),
        "Correct?": "✓" if match else "✗"
    } for q, sel, corr, match in report])
    df.to_csv(output_path, index=False)

def calculate_rankings(output_dir):
    graded_files = [f for f in os.listdir(output_dir) if f.endswith('_graded.csv')]
    
    rankings = []
    
    for filename in graded_files:
        filepath = os.path.join(output_dir, filename)
        df = pd.read_csv(filepath)
        
        score = df['Correct?'].value_counts().get('✓', 0)
        student_name = filename.replace('_graded.csv', '')
        
        rankings.append({
            'Student ID': student_name,
            'Score': score,
            'Percentage': round((score / 30) * 100, 2),
            'Total Questions': 30
        })
    
    rankings_df = pd.DataFrame(rankings)
    rankings_df = rankings_df.sort_values(by=['Score', 'Student ID'], ascending=[False, True])
    rankings_df.insert(0, 'Rank', range(1, len(rankings_df) + 1))
    
    return rankings_df

def generate_question_stats(output_dir):
    graded_files = [f for f in os.listdir(output_dir) if f.endswith('_graded.csv')]
    all_reports = []
    
    for filename in graded_files:
        filepath = os.path.join(output_dir, filename)
        df = pd.read_csv(filepath)
        all_reports.append(df)
    
    if not all_reports:
        return None
    
    combined = pd.concat(all_reports)
    
    # Calculate question statistics
    question_stats = []
    for q in range(1, 31):  # Assuming 30 questions
        q_data = combined[combined['Question'] == q]
        total = len(q_data)
        correct = q_data['Correct?'].value_counts().get('✓', 0)
        incorrect = total - correct
        
        # Get answer distribution
        answer_dist = q_data['Selected'].value_counts().to_dict()
        
        # Get most common wrong answer if there are incorrect answers
        if incorrect > 0:
            wrong_answers = q_data[q_data['Correct?'] == '✗']['Selected']
            if not wrong_answers.empty:
                most_common_wrong = wrong_answers.mode()[0]
            else:
                most_common_wrong = 'None'
        else:
            most_common_wrong = 'None'
        
        question_stats.append({
            'Question': q,
            'Correct': correct,
            'Incorrect': incorrect,
            'Accuracy (%)': round((correct/total)*100, 2),
            'Most Common Wrong': most_common_wrong,
            'Answer Distribution': answer_dist
        })
    
    return pd.DataFrame(question_stats)

def create_performance_pdf(output_dir, rankings_df, question_stats):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add title page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'KNUST Exam Performance Report', 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Date: {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}', 0, 1, 'C')
    pdf.ln(20)
    
    # Add summary statistics
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Class Performance Summary', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    avg_score = rankings_df['Score'].mean()
    high_score = rankings_df['Score'].max()
    low_score = rankings_df['Score'].min()
    
    pdf.cell(0, 10, f'Number of Students: {len(rankings_df)}', 0, 1)
    pdf.cell(0, 10, f'Average Score: {avg_score:.1f}/30 ({avg_score/30*100:.1f}%)', 0, 1)
    pdf.cell(0, 10, f'Highest Score: {high_score}/30 ({high_score/30*100:.1f}%)', 0, 1)
    pdf.cell(0, 10, f'Lowest Score: {low_score}/30 ({low_score/30*100:.1f}%)', 0, 1)
    pdf.ln(10)
    
    # Add top performers
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Top Performers', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    top_students = rankings_df.head(5)
    for _, row in top_students.iterrows():
        pdf.cell(0, 10, f"{row['Rank']}. {row['Student ID']} - {row['Score']}/30 ({row['Percentage']}%)", 0, 1)
    
    # Add score distribution histogram
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Score Distribution', 0, 1)
    
    # Create score distribution plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(rankings_df['Score'], bins=10, color='skyblue', edgecolor='black')
    ax.set_title('Score Distribution', pad=20)
    ax.set_xlabel('Score')
    ax.set_ylabel('Number of Students')
    plt.tight_layout()
    
    # Save plot to temporary file
    temp_img_path = os.path.join(tempfile.gettempdir(), 'score_dist.png')
    plt.savefig(temp_img_path, format='png', dpi=300)
    plt.close(fig)
    pdf.image(temp_img_path, x=10, w=190)
    os.remove(temp_img_path)  # Clean up
    
    # Add question accuracy chart
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Question Accuracy', 0, 1)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(question_stats['Question'], question_stats['Accuracy (%)'], color='skyblue')
    ax.axhline(y=50, color='red', linestyle='--', label='50% Threshold')
    ax.set_title('Question Accuracy (%)', pad=20)
    ax.set_xlabel('Question Number')
    ax.set_ylabel('Percentage Correct')
    ax.set_xticks(range(1, 31))
    ax.set_ylim(0, 100)
    ax.legend()
    plt.tight_layout()
    
    # Save plot to temporary file
    temp_img_path = os.path.join(tempfile.gettempdir(), 'question_accuracy.png')
    plt.savefig(temp_img_path, format='png', dpi=300)
    plt.close(fig)
    pdf.image(temp_img_path, x=10, w=190)
    os.remove(temp_img_path)  # Clean up
    
    # Add correct answers chart
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Correct Answers by Question', 0, 1)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(question_stats['Question'], question_stats['Correct'], color='green')
    ax.set_title('Number of Students Who Answered Correctly', pad=20)
    ax.set_xlabel('Question Number')
    ax.set_ylabel('Number Correct')
    ax.set_xticks(range(1, 31))
    plt.tight_layout()
    
    # Save plot to temporary file
    temp_img_path = os.path.join(tempfile.gettempdir(), 'question_correct.png')
    plt.savefig(temp_img_path, format='png', dpi=300)
    plt.close(fig)
    pdf.image(temp_img_path, x=10, w=190)
    os.remove(temp_img_path)  # Clean up
    
    # Add detailed question statistics
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Question Performance Analysis', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    # Create a table with question stats
    col_widths = [15, 20, 20, 25, 35]
    headers = ['Q#', 'Correct', 'Incorrect', 'Accuracy %', 'Common Wrong']
    
    # Header
    pdf.set_fill_color(200, 220, 255)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C', True)
    pdf.ln()
    
    # Rows
    pdf.set_fill_color(255, 255, 255)
    for _, row in question_stats.iterrows():
        pdf.cell(col_widths[0], 10, str(row['Question']), 1, 0, 'C')
        pdf.cell(col_widths[1], 10, str(row['Correct']), 1, 0, 'C')
        pdf.cell(col_widths[2], 10, str(row['Incorrect']), 1, 0, 'C')
        pdf.cell(col_widths[3], 10, str(row['Accuracy (%)']), 1, 0, 'C')
        pdf.cell(col_widths[4], 10, str(row['Most Common Wrong']), 1, 0, 'C')
        pdf.ln()
    
    # Add answer distribution for each question
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Answer Distribution by Question', 0, 1)
    
    # Process 4 questions per page
    questions_per_page = 4
    total_questions = len(question_stats)
    
    for page_start in range(0, total_questions, questions_per_page):
        if page_start > 0:
            pdf.add_page()
            
        for i in range(questions_per_page):
            q_idx = page_start + i
            if q_idx >= total_questions:
                break
                
            row = question_stats.iloc[q_idx]
            
            # Create answer distribution plot for this question
            fig, ax = plt.subplots(figsize=(6, 4))
            dist = row['Answer Distribution']
            labels = list(dist.keys())
            values = list(dist.values())
            
            colors = ['green' if label == row['Correct'] else 'red' for label in labels]
            ax.bar(labels, values, color=colors)
            ax.set_title(f'Question {row["Question"]} Answer Distribution')
            ax.set_xlabel('Answer Choice')
            ax.set_ylabel('Number of Students')
            plt.tight_layout()
            
            # Save plot to temporary file
            temp_img_path = os.path.join(tempfile.gettempdir(), f'q{row["Question"]}_dist.png')
            plt.savefig(temp_img_path, format='png', dpi=300)
            plt.close(fig)
            pdf.image(temp_img_path, x=10, y=20 + (i % questions_per_page) * 50, w=90)
            os.remove(temp_img_path)  # Clean up
            
            pdf.set_xy(105, 20 + (i % questions_per_page) * 50)
            pdf.multi_cell(90, 5, 
                          f"Q{row['Question']}: Correct Answer: {row['Correct']}\n"
                          f"Accuracy: {row['Accuracy (%)']}%\n"
                          f"Most Common Wrong: {row['Most Common Wrong']}")
    
    # Add full rankings table
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Full Class Rankings', 0, 1)
    
    # Create a table with all rankings
    col_widths = [15, 40, 20, 25, 25]
    headers = ['Rank', 'Student ID', 'Score', 'Percentage', 'Total']
    
    # Header
    pdf.set_fill_color(200, 220, 255)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C', True)
    pdf.ln()
    
    # Rows
    pdf.set_fill_color(255, 255, 255)
    for _, row in rankings_df.iterrows():
        pdf.cell(col_widths[0], 10, str(row['Rank']), 1, 0, 'C')
        pdf.cell(col_widths[1], 10, str(row['Student ID']), 1, 0, 'L')
        pdf.cell(col_widths[2], 10, str(row['Score']), 1, 0, 'C')
        pdf.cell(col_widths[3], 10, str(row['Percentage']), 1, 0, 'C')
        pdf.cell(col_widths[4], 10, str(row['Total Questions']), 1, 0, 'C')
        pdf.ln()
    
    # Save the PDF
    pdf_path = os.path.join(output_dir, 'exam_performance_report.pdf')
    pdf.output(pdf_path)
    
    return pdf_path

def batch_grade():
    global image_dir, key_file, output_dir
    
    # Validate inputs
    if not image_dir:
        messagebox.showwarning("Input Error", "Please select a folder with scantron images")
        return
    if not key_file:
        messagebox.showwarning("Input Error", "Please select an answer key CSV file")
        return
    if not output_dir:
        messagebox.showwarning("Input Error", "Please select an output folder")
        return
    
    try:
        # Load answer key
        update_status("Loading answer key...")
        key = load_answer_key_from_csv(key_file)
        if key is None:
            return
        
        # Get list of image files
        files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if not files:
            messagebox.showwarning("Input Error", "No image files found in the selected folder")
            return
        
        update_status(f"Found {len(files)} images to process...")
        update_progress(0, len(files))
        
        # Process each file
        graded = 0
        for i, filename in enumerate(files):
            try:
                update_status(f"Processing {filename}...")
                
                # Load and process image
                image_path = os.path.join(image_dir, filename)
                _, thresh = load_image(image_path)
                if thresh is None:
                    continue
                
                # Extract and grade answers
                student_answers = extract_answers(thresh, num_questions=30)
                score, report = grade(student_answers, key)
                
                # Save report
                base = os.path.splitext(filename)[0]
                output_file = os.path.join(output_dir, f"{base}_graded.csv")
                save_report(report, output_file)
                
                graded += 1
                update_progress(i + 1)
                
            except Exception as e:
                update_status(f"Error processing {filename}: {str(e)}")
                continue
        
        # Generate reports if we processed any files
        if graded > 0:
            update_status("Generating class reports...")
            
            # Generate rankings and statistics
            rankings_df = calculate_rankings(output_dir)
            question_stats = generate_question_stats(output_dir)
            
            if question_stats is not None:
                # Generate the performance PDF report
                pdf_path = create_performance_pdf(output_dir, rankings_df, question_stats)
                update_status(f"Performance report generated: {os.path.basename(pdf_path)}")
            
            messagebox.showinfo(
                "Sheet Grading Complete",
                f"Successfully graded {graded} answer sheets.\n\n"
                f"Individual reports saved in:\n{output_dir}\n\n"
                f"Performance report saved to: exam_performance_report.pdf"
            )
        else:
            messagebox.showwarning("No Files Processed", "No files were successfully graded.")
        
        update_status("Ready")
        update_progress(0)
        
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")
        update_status("Error occurred")
        update_progress(0)

def main():
    global root, status_var, progress, progress_label, img_dir_var, key_file_var, output_dir_var
    
    root = tk.Tk()
    root.title("EduGrader")
    root.geometry("800x600")
    root.resizable(True, True)
   
    header_font = ('Nunito', 20, 'bold')
    button_font = ('Nunito', 10, 'bold')
    
    # Configure styles
    style = ttk.Style()
    style.configure('TFrame', background='BLUE')
    style.configure('ColoredHeader.TLabel', 
               font=header_font,
               foreground='ORANGE', 
               background='BLUE')
    style.configure('TButton', 
                   font=button_font, 
                   padding=5,
                   background=ORANGE,
                   foreground=WHITE,
                   bordercolor=ORANGE)
    style.configure('TLabel', 
               background=BLUE,
               foreground=ORANGE, 
               font=button_font)
    
    # Create main container
    mainframe = ttk.Frame(root)
    mainframe.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Header
    header = ttk.Label(mainframe, text="EduGrader", style='ColoredHeader.TLabel')
    header.pack(pady=(0, 20))
    tk.Button(mainframe, text="☰", font=("Arial", 14), bg=BLUE, fg=ORANGE, command=show_menu).pack(side=tk.RIGHT, padx=5)
    
    # Input frame
    input_frame = ttk.Frame(mainframe)
    input_frame.pack(fill=tk.X, pady=5)
    
    # Image directory input
    img_dir_var = tk.StringVar()
    ttk.Label(input_frame, text="Scan Images Folder:").grid(row=0, column=0, sticky=tk.W, pady=2)
    img_dir_entry = ttk.Entry(input_frame, textvariable=img_dir_var, width=40)
    img_dir_entry.grid(row=0, column=1, padx=5)
    img_dir_btn = ttk.Button(input_frame, text="Browse...", command=select_image_dir)
    img_dir_btn.grid(row=0, column=2)
    
    # Answer key input
    key_file_var = tk.StringVar()
    ttk.Label(input_frame, text="Marking Scheme CSV File:").grid(row=1, column=0, sticky=tk.W, pady=2)
    key_file_entry = ttk.Entry(input_frame, textvariable=key_file_var, width=40)
    key_file_entry.grid(row=1, column=1, padx=5)
    key_file_btn = ttk.Button(input_frame, text="Browse...", command=select_key_file)
    key_file_btn.grid(row=1, column=2)
    
    # Output directory input
    output_dir_var = tk.StringVar()
    ttk.Label(input_frame, text="Output Folder:").grid(row=2, column=0, sticky=tk.W, pady=2)
    output_dir_entry = ttk.Entry(input_frame, textvariable=output_dir_var, width=40)
    output_dir_entry.grid(row=2, column=1, padx=5)
    output_dir_btn = ttk.Button(input_frame, text="Browse...", command=select_output_dir)
    output_dir_btn.grid(row=2, column=2)
    
    # Progress bar
    progress_frame = ttk.Frame(mainframe)
    progress_frame.pack(fill=tk.X, pady=10)
    progress_label = ttk.Label(progress_frame, text="Ready")
    progress_label.pack()
    progress = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
    progress.pack()
    
    # Action buttons
    btn_frame = ttk.Frame(mainframe)
    btn_frame.pack(pady=10)
    grade_btn = ttk.Button(btn_frame, text="Grade Sheets", command=batch_grade, style='TButton')
    grade_btn.pack(side=tk.LEFT, padx=5)
    exit_btn = ttk.Button(btn_frame, text="Exit", command=root.quit)
    exit_btn.pack(side=tk.LEFT, padx=5)
    
    # Status bar
    status_var = tk.StringVar()
    status_var.set("Ready")
    status_bar = ttk.Label(mainframe, textvariable=status_var, relief=tk.SUNKEN)
    status_bar.pack(fill=tk.X, pady=(10, 0))
    
    root.mainloop()

if __name__ == "__main__":
    main()