# Prompt used for formatting Question & Answer output format
format_instruction = """

    If the provided context lacks sufficient information to create {num_questions} distinct flashcards,
    do not generate any flashcards. Instead, respond that the context given is insufficient.

    Now, generate the flashcards based on the given text in the following format:

    Question: [Question 1]
    Answers: [Option 1]|[Option 2]|[Option 3]|[Option 4](o)

    Question: [Question 2]
    Answers: [Option 1](o)|[Option 2]|[Option 3]|[Option 4]

    ...

    Question: [Question {num_questions}]
    Answers: [Option 1]|[Option 2](o)|[Option 3]|[Option 4]

"""

# Zero-Shot Prompt
zeroshot_prompt = """
    Create {num_questions} questions from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    Each question should have 4 answers, three of them must be incorrect and one should be correct.
""" + format_instruction


# Few-Shot Prompt
fewshot_prompt = """
    Create {num_questions} questions from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    Each question should have 4 answers, three of them must be incorrect and one should be correct.

    Here are some examples of questions:

    Question: What is the color of the ocean?
    Answers: Red|Yellow|Green|Blue(o)

    Question: When was Avatar released?
    Answers: 2007|2001|2009(o)|1998

""" + format_instruction


# Chain-of-Thought Prompt
chain_of_thought_prompt = """
    Create {num_questions} questions from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    Each question should have 4 answers, three of them must be incorrect and one should be correct.

    First, identify key pieces of information in the text. 
    Then, formulate questions that would prompt someone to recall this information.
    Finally, provide the possible answers for each question containing 3 incorrect answers and 1 correct answer.

    Here are some examples of the thought process for creating questions:

    Example 1:
    Text: "The capital of France is Paris."
    Step 1: Identify key information - "capital of France"
    Step 2: Formulate a question - "What is the capital of France?"
    Step 3: Provide the answer - "Paris"
    Step 4: Come up with 3 incorrect answers - "Seoul", "Berlin", "Bangkok"

    Question: What is the capital of France?
    Answers: Seoul|Berlin|Paris(o)|Bangkok

    Example 2:
    Text: "Plants make food through the process called photosynthesis."
    Step 1: Identify key information - "process called photosynthesis"
    Step 2: Formulate a question - "What is the process by which plants make food?"
    Step 3: Provide the answer - "Photosynthesis"
    Step 4: Come up with 3 incorrect answers - "Microsynthesis", "Chromosome", "Transpiration"

    Question: What is the process by which plants make food?
    Answers: Photosynthesis(o)|Microsynthesis|Chromosome|Transpiration

""" + format_instruction

# Analogy-Based Prompt
analogy_based_prompt = """
    Create {num_cards} questions from the following text enclosed in triple backticks (```):

    ```
    {context}
    ```

    Each question should have 4 answers, three of them must be incorrect and one should be correct.

    Think of creating questions as similar to creating trivia questions based on a passage from a book.
    First, identify key pieces of information that are important to remember, similar to how you would pick out interesting facts for a trivia game.
    Then, formulate questions that would prompt someone to recall these key pieces of information, just like crafting trivia questions.
    Finally, provide the possible answers for each question containing 3 incorrect answers and 1 correct answer.

    Here are some examples of using analogies to create questions:

    Example 1:
    Text: "The capital of France is Paris."
    Analogy: Creating a trivia question about geography
    Step 1: Identify key information - "capital of France"
    Step 2: Formulate a trivia-like question - "What is the capital of France?"
    Step 3: Provide the answer - "Paris"
    Step 4: Come up with 3 incorrect answers - "Seoul", "Berlin", "Bangkok"

    Question: What is the capital of France?
    Answers: Seoul|Berlin|Paris(o)|Bangkok

    Example 2:
    Text: "Plants make food through the process called photosynthesis."
    Analogy: Creating a trivia question about biology
    Step 1: Identify key information - "process called photosynthesis"
    Step 2: Formulate a trivia-like question - "What is the process by which plants make food?"
    Step 3: Provide the answer - "Photosynthesis"
    Step 4: Come up with 3 incorrect answers - "Microsynthesis", "Chromosome", "Transpiration"

    Question: What is the process by which plants make food?
    Answers: Photosynthesis(o)|Microsynthesis|Chromosome|Transpiration

""" + format_instruction





