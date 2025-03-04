# Coding-Final
# Ping Pong advanced
#### Video Demo: <https://www.youtube.com/watch?v=eJ8zvZRxCaM>
#### Description:
The game itself is pretty self explanatory, you have to being by importing the turtle animation sequence and the winsound sequence.
After you do both you move onto the creating the screen and the boundaries for it in this we created the Ping Pong Game while estabilishing a boundary of 800x600.

After you create the screen you then use the paddles you set the speed of the paddles to be equal so that one person isn't faster than the other. After that you create the size of the paddle and what color it is. you will then set the start coordinates of the paddle. You can use the same coordinates for both paddles just remember to include the negative on one of the numebers to differentiate which is which.

When you finsih you create the ball, the ball can a little tricky but if you can create whatever kind of ball you want in our code we decided to go with a circle. Using the dx and the dy you can modify the speed at which the ball is moving either up or down.

We then moved on to defining the sounds, this is where the winsound function comes into play luckily, it wasn't that bad as we only had 3 different sound strings we had to insert.
We then move on to the score display system and its almost the same thing as the title scree except the key difference is that there isn't a border for it rather we just respect the original.
Then we move on to the winner, whichever side scored the most is what the game recognizes as the winner with maximum cap of 5 there is no time limt or minimum amount you score.
The next set of prompts is descrining what each keybind does in the game and what the computer will recognize, you can press any other buttons but they have no effect on the gameplay.
After that we move onto defining the game loop as a whole. If the game is running then it is constantly updating itself at a rate of about 10 miliseconds. It will go into detail about moving the ball by using the ball set with the x and y planes. When you hit a border it will make a noisee and invert the ball we acheive this by change the balls y direction by -1.
When you score it will play a sound and reset, it will then proceed to keep the game running until one side reaches 5.
Then we described the game over conditions which was already discussed. one player reaches 5. The paddle collison is if the ball hits the paddle. but you have to be percise otherwise the ball will go through the paddle and score.
We then set the refresh rate for the on timer at 10 milliseconds. The define the start screen and the start message. The last line of  code is the win main loop that is defined ealier in the code.
TODO 
