# QuizLM

QuizLM leverages the power of LLMs to automate the process of creating effective study aids from any source text, helping users learn and retain knowledge efficiently.

## Main Features
- **FlashCard Generator**: Automatically creates flashcards from text input, helping users to quickly and efficiently generate study aids. This feature benefits users by breaking down complex information into manageable, question-and-answer pairs that facilitate better understanding and memorization.
- **Quiz Generator**: Generates quizzes based on the provided text, offering an interactive way for users to test their knowledge and reinforce learning. This feature is useful for both self-assessment and instructional purposes, making the learning process more engaging and effective.

## Technical Details
We use various prompt engineering techniques on top of OpenAI's GPT models to generate high-quality flashcards or quizzes. We share the various prompt engineering techniques we explored and share the results below:

1. Zero-shot:
- Zero-shot is when we simply ask the language model to perform the desired task. For us, this was simply a prompt similar to
```
Create X flashcards from the following text:
{context}
```
- This gave us flashcards that did {something}

2. Few-shot:
- Few-shot is when we provide some high-quality question/answer pairs to the langugae model as examples. For example,
```
Create X flashcards from the following text:
{context}

Each question should have 4 answers, three of them must be incorrect and one should be correct.

Here are some examples of flashcards:

Example 1:
Question: What is the capital of France?
Answer: Paris

Example 2:
Question: What is the process by which plants make food?
Answer: Photosynthesis
```
- Note that in the examples aboves, the answers are brief--a more suitable style for flashcards than full sentences. As such, the output we get from the LLM also has short answers. However, we noticed {something} is still lacking. (maybe flashcards did not contain all the critical info)

3. Chain-of-thought
- 