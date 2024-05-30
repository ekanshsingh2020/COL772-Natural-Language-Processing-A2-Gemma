# Assignment 2.1 : Table Question Answering with Large Language Models
### Goal
- We had question,table pairs along with the gold labels in the training data same as the second assignment
- We are supposed to filter out the correct cells from the table which correspond to the answer of the given question but this time we need to use Google's new Gemma model (gemma-7b-it-quant) to solve the problem instead of any neural methods by using prompt engineering

### Idea Overview
- The idea was to somehow give the prompt where the model firstly knows the output structure so that we can then parse our required output from that
- Secondly we need to prompt it in a way that it outputs in a way which it feels easier and print small chunks of the information along the way
- I wanted to set the temperature as something non-zero but with that I was facing issues as at times it just followed a random thread and have random outputs and hence fixed the temperature as 0
- The output length was also set to 25 because I prompted it in a way where the initial part of the output would be containing all the information I need to parse
- Now I'll explain the implementation
  - Constructor (init(self))
    - This method sets the generation parameters for Gemma
    - Parameters include output len, temperature, and top p
  - Prompt creator (create_prompt(self,sample))
    - This was the main function where the prompt was created
    - The input sample contained the table and question
    - I decided to go with 2 shot prompts where two samples are already answered and the LLM would learn (in context learning) how to answer from those samples in the prompt
    - You can see the complete prompt how it was designed, one of the highlights what that the model was able to understand it really well when I added row numbers in front of every row and column name in front of the row which had column names
  - Post-processing (post process(self, gen text))
    - Gemma model generates a response to the prompt as text
    - The post process method converted the answer from the generated model response to (row, column) format, as in the case of main Assignment 2
  
### Result
The column accuracy with the given prompt was 82% and row accuracy was 77% which landed me 7th in the class

Please let me know if there is anything to ask in the code :) 