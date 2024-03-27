import os


def save_text_file(artifact_id, content, path="."):
    txt_filename = f"{artifact_id}.txt"
    txt_path = os.path.join(path, txt_filename)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(content)
    return {"message": f"Text file saved to {txt_path}"}


def save_pdf_file(artifact_id, content, path="."):
    pdf_filename = f"{artifact_id}.pdf"
    pdf_path = os.path.join(path, pdf_filename)
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(content)
    return {"message": f"PDF file saved to {pdf_path}"}


def save_csv_file(artifact_id, content, path="."):
    csv_filename = f"{artifact_id}.csv"
    csv_path = os.path.join(path, csv_filename)
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_file.write(content)
    return {"message": f"CSV file saved to {csv_path}"}
