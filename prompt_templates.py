def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer the user's question clearly and accurately.
Do not use examples unless they are needed.

Question:
{task}
""".strip()

    elif technique == "One-shot":
        return f"""
Follow the format shown in this example.

Example:
Question: What is a database?
Answer: A database is an organized collection of information
that can be stored, searched, and updated.

Now answer this question:
{task}
""".strip()

    elif technique == "Few-shot":
        return f"""
Study these examples and follow their answer style.

Example 1:
Question: What is Python?
Answer: Python is a programming language used to build software.

Example 2:
Question: What is an API?
Answer: An API allows different software applications to communicate.

Example 3:
Question: What is cloud computing?
Answer: Cloud computing provides computing services over the internet.

Now answer:
{task}
""".strip()

    elif technique == "CoT":
        return f"""
Solve the task carefully.
Provide a concise explanation of the key steps and the final answer.
Do not provide private internal chain-of-thought.

Task:
{task}
""".strip()

    elif technique == "Manual CoT":
        return f"""
Organize your answer using these stages.

1. Understand the question.
2. Identify the important information.
3. Apply the relevant rule or method.
4. Check the result.
5. Present the final answer.

Task:
{task}
""".strip()

    elif technique == "ToT":
        return f"""
Consider different possible solutions to the task.
Briefly describe up to three alternatives, compare their
advantages and disadvantages, and select the most suitable one.
Give a concise explanation rather than private internal
chain-of-thought.

Task:
{task}
""".strip()

    else:
        raise ValueError(
            f"Unsupported prompting technique: {technique}"
        )