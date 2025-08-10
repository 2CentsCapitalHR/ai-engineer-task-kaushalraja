# checklist.py

def get_checklist_for_process():
    """Returns the required documents for Company Incorporation."""
    return [
        "Articles of Association",
        "Memorandum of Association",
        "UBO Declaration Form",
        "Incorporation Application Form",
        "Register of Members and Directors"
    ]


def check_missing_documents(uploaded_doc_names):
    """
    Compares uploaded document names to required checklist.
    
    Parameters:
        uploaded_doc_names (list): Cleaned names of uploaded documents.
        
    Returns:
        list: Missing document names.
    """
    required = get_checklist_for_process()
    missing = [doc for doc in required if doc not in uploaded_doc_names]
    return missing


def clean_doc_name(name):
    """
    Maps uploaded file names to standard document titles based on keywords.
    
    Parameters:
        name (str): Raw uploaded file name.
        
    Returns:
        str: Cleaned, standardized document name.
    """
    name = name.lower()
    if "articles" in name:
        return "Articles of Association"
    elif "memorandum" in name or "mou" in name:
        return "Memorandum of Association"
    elif "ubo" in name:
        return "UBO Declaration Form"
    elif "application" in name:
        return "Incorporation Application Form"
    elif "register" in name:
        return "Register of Members and Directors"
    else:
        return name.title()  # fallback
