# prompts.py
# এই ফাইলে সব prompt template থাকবে - একটা জায়গায় সব prompt manage হবে


def resume_analysis_prompt(resume_text: str) -> str:
    """Resume analyze করার জন্য standard prompt"""
    return f"""
    You are an expert technical recruiter. Analyze the following resume 
    and extract strengths, weaknesses, and a suggested role.

    Resume:
    {resume_text}
    """


def classification_prompt(text: str, categories: list[str]) -> str:
    """Text কে দেওয়া categories এর মধ্যে classify করার prompt"""
    categories_str = ", ".join(categories)
    return f"""
    Classify the following text into exactly one of these categories: {categories_str}.
    Respond with only the category name, nothing else.

    Text: {text}
    """


def summarizer_prompt(text: str, max_words: int = 50) -> str:
    """Text summarize করার prompt, word limit সহ"""
    return f"""
    Summarize the following text in at most {max_words} words.
    Keep the tone neutral and factual.

    Text:
    {text}
    """


def translation_prompt(text: str, target_language: str = "Bangla") -> str:
    """Text translate করার prompt"""
    return f"""
    Translate the following text into {target_language}.
    Preserve technical terms in English if they don't have a common translation.

    Text:
    {text}
    """
