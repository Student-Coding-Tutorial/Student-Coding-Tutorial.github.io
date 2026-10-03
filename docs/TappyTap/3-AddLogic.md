# Adding Logic
In this part of the tutorial, we will focus on adding game logic to the circles and the score  
## Change the score when the circles are clicked  
1. In the Code Editor, add this code:  
   ```
   onEvent("your_blue_circle_id","click",function() {
     score = score + 1;
   });
   ```  
2. Repeat the same for the red circle. Remember to decrease instead of increase the score!

## Displaying the score
1. Go back to the design tab.
2. Add a text label in the top left of the phone screen and call it ScoreDisplay (or something similar).
3. Go to the Code Editor and add this code to the event listeners, underneath score = score + 1;
   ```
   setText("YOUR_SCORE_DISPLAY_ID","click",score)
   ```
> [!note]
> Do NOT put double quotation marks around the score, because this will become a string, displaying the word 'score'
> Without the double quotation marks, it will display the value of the variable 'score'.
