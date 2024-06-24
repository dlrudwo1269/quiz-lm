# Prompt used for formatting Question & Answer output format
format_instruction = """

    Now, generate the flashcards based on the given text in the following format:

    Question 1: [Question 1]
    Answer 1: [Answer 1]

    Question 2: [Question 2]
    Answer 2: [Answer 2]

    ...

    Question {num_cards}: [Question {num_cards}]
    Answer {num_cards}: [Answer {num_cards}]
"""

# Zero-Shot Prompt
zeroshot_prompt = """
    Create {num_cards} flashcards from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    For each flashcard, provide a [Question] on one side and a corresponding [Answer] on the other side.
""" + format_instruction


# Few-Shot Prompt
fewshot_prompt = """
    Create {num_cards} flashcards from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    For each flashcard, provide a [Question] on one side and a corresponding [Answer] on the other side.

    Here are some examples of flashcards:

    Example 1:
    Question: What is the capital of France?
    Answer: Paris

    Example 2:
    Question: What is the process by which plants make food?
    Answer: Photosynthesis

""" + format_instruction


# Chain-of-Thought Prompt
chain_of_thought_prompt = """
    Create {num_cards} flashcards from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    For each flashcard, provide a [Question] on one side and a corresponding [Answer] on the other side.

    First, identify key pieces of information in the text. Then, formulate questions that would prompt someone to recall this information. Finally, provide the correct answer for each question.

    Here are some examples of the thought process for creating flashcards:

    Example 1:
    Text: "The capital of France is Paris."
    Step 1: Identify key information - "capital of France"
    Step 2: Formulate a question - "What is the capital of France?"
    Step 3: Provide the answer - "Paris"

    Question: What is the capital of France?
    Answer: Paris

    Example 2:
    Text: "Plants make food through the process called photosynthesis."
    Step 1: Identify key information - "process called photosynthesis"
    Step 2: Formulate a question - "What is the process by which plants make food?"
    Step 3: Provide the answer - "Photosynthesis"

    Question: What is the process by which plants make food?
    Answer: Photosynthesis

""" + format_instruction


# Analogy-Based Prompt
analogy_based_prompt = """
    Create {num_cards} flashcards from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    For each flashcard, provide a [Question] on one side and a corresponding [Answer] on the other side.

    Think of creating flashcards as similar to creating trivia questions based on a passage from a book. First, identify key pieces of information that are important to remember, similar to how you would pick out interesting facts for a trivia game. Then, formulate questions that would prompt someone to recall these key pieces of information, just like crafting trivia questions. Finally, provide the correct answer for each question.

    Here are some examples of using analogies to create flashcards:

    Example 1:
    Text: "The capital of France is Paris."
    Analogy: Creating a trivia question about geography
    Step 1: Identify key information - "capital of France"
    Step 2: Formulate a trivia-like question - "What is the capital of France?"
    Step 3: Provide the answer - "Paris"

    Question: What is the capital of France?
    Answer: Paris

    Example 2:
    Text: "Plants make food through the process called photosynthesis."
    Analogy: Creating a trivia question about biology
    Step 1: Identify key information - "process called photosynthesis"
    Step 2: Formulate a trivia-like question - "What is the process by which plants make food?"
    Step 3: Provide the answer - "Photosynthesis"

    Question: What is the process by which plants make food?
    Answer: Photosynthesis

""" + format_instruction





