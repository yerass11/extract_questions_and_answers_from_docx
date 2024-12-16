from docx import Document
import os

# Load the Word document
doc_path = 'Example2.docx'
doc = Document(doc_path)

# Extract questions and answers
questions_and_answers = []
for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text.lower().startswith("question") and "answer:" in text.lower():
        parts = text.split("Answer:", 1)
        if len(parts) == 2:
            question, answer = parts
            question = question.strip().replace(":", "").replace("?", "").replace("/", "").replace("\\", "").replace("*", "").replace(">", "").replace("<", "").replace("|", "").replace('"', "").replace(":", "")
            answer = answer.strip()
            questions_and_answers.append((question, answer))

# Ensure output directory exists
output_dir = "data2/"
os.makedirs(output_dir, exist_ok=True)

# Save each question and answer to a separate text file
output_files = []
for idx, (question, answer) in enumerate(questions_and_answers, start=1):
    sanitized_question = question[:50] if len(question) > 50 else question
    filename = os.path.join(output_dir, f"{sanitized_question}.txt")
    output_files.append(filename)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Question: {question}\nAnswer: {answer}")

# List the generated files
output_files
