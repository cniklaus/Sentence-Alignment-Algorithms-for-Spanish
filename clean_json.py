import json
import os
import re

def clean_text(text):
    """Remove unwanted characters and normalize whitespace."""
    text = re.sub(r'[“”„‟"\'‹›«»]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def normalize_text(text):
    if isinstance(text, list):
        text = " ".join(text)
    elif not isinstance(text, str):
        return ""
    return clean_text(text)

def json_to_tabbed_lines(input_json_path):
    try:
        with open(input_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        lines = []
        for alignment in data.get("alignments", []):
            complex_text = normalize_text(alignment.get("complex", ""))
            simple_text = normalize_text(alignment.get("simple", ""))
            lines.append(f"{complex_text}\t{simple_text}")
        return lines
    except Exception as e:
        print(f"❌ Error in {input_json_path}: {e}")
        return []

def process_all_jsons(folder_path, output_folder, start=0, end=242):
    os.makedirs(output_folder, exist_ok=True)
    missing_count = 0
    total_files = end - start + 1

    for i in range(start, end + 1):
        json_path = os.path.join(folder_path, f"{i}.json")
        output_txt_path = os.path.join(output_folder, f"{i}.txt")

        if os.path.exists(json_path):
            lines = json_to_tabbed_lines(json_path)
            with open(output_txt_path, 'w', encoding='utf-8') as out_file:
                out_file.write("\n".join(lines))
        else:
            open(output_txt_path, 'w', encoding='utf-8').close()
            print(f"⚠️ Missing JSON: {json_path} — created empty {output_txt_path}")
            missing_count += 1

    missing_pct = (missing_count / total_files) * 100
    print(f"✅ Finished writing tab-separated files to {output_folder}")
    print(f"📊 Missing JSONs in '{folder_path}': {missing_count}/{total_files} ({missing_pct:.2f}%)")
    return missing_count, total_files

def process_all_subfolders(base_folder):
    """Iterate through all subfolders starting with 'Llama_70B'."""
    total_missing = 0
    total_expected = 0

    for subdir in sorted(os.listdir(base_folder)):
        if not subdir.startswith("Llama_70B"):
            continue  # skip other folders

        full_subdir_path = os.path.join(base_folder, subdir)
        if os.path.isdir(full_subdir_path):
            print(f"\n🔹 Processing folder: {subdir}")
            output_folder = os.path.join(full_subdir_path, "aligned_txt_output")
            missing_count, total_files = process_all_jsons(full_subdir_path, output_folder)
            total_missing += missing_count
            total_expected += total_files

    overall_pct = (total_missing / total_expected) * 100 if total_expected > 0 else 0
    print(f"\n🏁 All 'Llama_70B*' subfolders processed successfully.")
    print(f"📈 TOTAL missing JSONs: {total_missing}/{total_expected} ({overall_pct:.2f}%)")

if __name__ == "__main__":
    process_all_subfolders("LLM_sentence_alignment")
