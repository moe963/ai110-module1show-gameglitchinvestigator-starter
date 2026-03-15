# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I first ran the game, it worked, but the logic had clear bugs. 
  The hint direction was wrong: if my guess was too high, it told me to go higher instead of lower. 
  Also, the game sometimes compared different data types, which made hint behavior inconsistent between turns. 
  The attempts counter also started at 1, so the “attempts left” message was not accurate.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used AI chat to review app.py and explain the guessing flow.
  One correct AI suggestion was to keep comparisons as integer to integer every turn. 
  I verified this by running the app and checking that hint behavior stayed consistent.
  One misleading suggestion was to do a full refactor right away, which was more than needed for this debug task. 
  I chose a smaller fix and confirmed it solved the issue.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I treated each bug as fixed only after testing it in the app. 
  I made high and low guesses and checked that the hint direction was correct each time. 
  I also checked that attempts were counted correctly after changing the starting value.
   After that, I ran pytest to make sure tests still passed and no new issues were added.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  I learned that Streamlit session state is the app’s memory between reruns. 
  If values are handled inconsistently, the game can look random or broken. 
  The fix was to keep the secret value handling consistent and correct the attempts counter logic.  
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  
  A habit I will keep is making small, 
  focused fixes and testing after each one. 
  Next time, I will give AI more specific prompts so suggestions stay within scope. 
  This project showed me that AI is useful for speed, but I still need to check logic and confirm behavior myself.
---
