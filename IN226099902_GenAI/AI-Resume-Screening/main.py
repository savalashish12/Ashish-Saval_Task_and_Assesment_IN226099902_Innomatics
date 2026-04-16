import os
import sys
os.makedirs("Outputs", exist_ok=True)

from utils.parser import read_pdf
from utils.json_parser import safe_json_parse
from langchain_core.prompts import PromptTemplate
from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain
from chains.jd_extract_chain import jd_extract_chain



def process_resume(pdf_path, jd):

    # STEP 1: Read Resume PDF
    resume_text = read_pdf(pdf_path)

    # STEP 2: Extract Resume Data (with tag)
    extracted_raw = extract_chain.invoke(
        {"resume": resume_text},
        config={"tags": ["extract"]}
    )
    extracted = safe_json_parse(extracted_raw)
    print("DEBUG Extracted:",extracted)

    # STEP 3: Extract JD Skills (with tag)
    jd_raw = jd_extract_chain.invoke(
        {"jd": jd},
        config={"tags": ["jd_extract"]}
    )
    jd_data = safe_json_parse(jd_raw)

    # STEP 4: Match
    match_raw = match_chain.invoke({
        "required_skills": jd_data.get("required_skills", []),
        "candidate_skills": extracted.get("skills", [])
        },
        config={"tags": ["match"]}
    )
    matched = safe_json_parse(match_raw)

    # STEP 5: Score
    score_raw = score_chain.invoke(
        {
            "data": {
                "jd": jd_data,
                "match": matched,
                "candidate": extracted
                }
        },
        config={"tags": ["score"]}
    )

    score_data = safe_json_parse(score_raw)
    # score_data = safe_json_parse(score_raw)
    # score = score_data.get("score", 0)
    # exp = extracted.get("experience_years", 0)

    # if exp >= 3:
    #     score += 10
    # elif exp < 1:
    #     score -= 10

    # score_data["score"] = round(score, 2)

    # STEP 6: Explain
    explanation = explain_chain.invoke(
        {
            "data": {
                "jd": jd_data,
                "match": matched,
                "score": score_data,
                "candidate": extracted
            }
        },
        config={"tags": ["explain"]}
    )

    return score_data, explanation


if __name__ == "__main__":

    # 🔥 FIX JD PDF READING
    jd = read_pdf("data/Job Description - Data Scientist.pdf")
    
    if len(sys.argv) > 1:
        resumes = [sys.argv[1]]
    else:
        resumes = [
            "data/resumes/Nitin Satarkar.pdf",
            "data/resumes/Ashish Saval.pdf",
            "data/resumes/Ram Kachare.pdf"
        ]

    for resume in resumes:
        print(f"\nProcessing: {resume}")

        score, explanation = process_resume(resume, jd)

        print("Score:", score)
        print("Explanation:", explanation)

        # 🔥 SAVE TO FILE
        filename = os.path.basename(resume).replace(".pdf", ".txt")

        with open(f"Outputs/{filename}", "w", encoding="utf-8") as f:
            f.write(f"Resume: {resume}\n\n")
            f.write(f"Score: {score}\n\n")
            f.write(f"Explanation:\n{explanation}\n")
            
        print("-" * 50)