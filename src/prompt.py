def chatbot_prompt():
    return """
Answer briefly for the question {question} 

based on the following chunks of context 
{context}.

If you do not get answer from the context, you have to answer as
'I do not know the answer' but you should not answer creatively using your knowledge.

"""