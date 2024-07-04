import os


def save_json_file(artifact_id, content, path="."):
    json_filename = f"{artifact_id}.json"
    json_path = os.path.join(path, json_filename)
    with open(json_path, "w", encoding="utf-8") as json_file:
        json_file.write(content)
    return {"message": f"Json file saved to {json_path}", "file_path": json_path}


def save_pdf_file(artifact_id, content, path="."):
    pdf_filename = f"{artifact_id}.pdf"
    pdf_path = os.path.join(path, pdf_filename)
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(content)
    return {"message": f"PDF file saved to {pdf_path}", "file_path": pdf_path}


def save_csv_file(artifact_id, content, path="."):
    csv_filename = f"{artifact_id}.csv"
    csv_path = os.path.join(path, csv_filename)
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_file.write(content)
    return {"message": f"CSV file saved to {csv_path}", "file_path": csv_path}
