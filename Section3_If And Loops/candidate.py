experience = 2
languages = ["python", "javascript", "java"]
contractType = "b2b"

def check_candidate(experience, languages, contractType):
    if experience >= 2 and "python" in languages and "java" in languages:
        if contractType == "b2b" or contractType == "employment":
            print("Welcome aboard, Dear Candidate!")
        else:
            print("Sorry — we only hire on B2B or employment contracts.")
    else:
        print("Sorry Candidate - we are looking for someone else")

check_candidate(experience,languages,contractType)