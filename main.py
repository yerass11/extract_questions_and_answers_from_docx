from docx import Document

# Load the Word document
doc_path = 'Example2.docx'
doc = Document(doc_path)

# Extract questions and answers
questions_and_answers = []
for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text.startswith("Question") and "ANSWER:" in text:
        question, answer = text.split("ANSWER:", 1)
        question = question.strip().replace(":", "").replace("?", "").replace("/", "").replace("\\", "").replace("*", "").replace(">", "").replace("<", "").replace("|", "").replace('"', "").replace(":", "")
        answer = answer.strip()
        questions_and_answers.append((question, answer))

# Save each question and answer to a separate text file
output_dir = "res2/"
for idx, (question, answer) in enumerate(questions_and_answers, start=1):
    filename = f"{output_dir}{question[:50]}...txt" if len(question) > 50 else f"{output_dir}{question}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"{question}\n{answer}")

# List the generated files
output_files = [f"{question[:50]}...txt" if len(question) > 50 else f"{question}.txt" for question, _ in questions_and_answers]
output_files
