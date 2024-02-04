# The Garden Of Sinners Trivia Game
#### Video Demo:  https://youtu.be/1PH5puOp5tE
#### Description:
Hello. My project is a trivia game focused around the anime series, The Garden of Sinners. I chose this series since it’s my favorite anime series. The Garden of Sinners focuses around nonlinear, intriguing mysteries, creative philosophies, awesome action, and complex characters. I decided to create three difficulties for the game with each difficulty having six questions because having so many questions could result in subjectivity and repetitiveness. Also, this can leave extra questions for a question bank used as the possible bonus question near the end of the game.

I decided to store the questions in a multiple layered dictionary format because this makes accessing various questions and answers very simple as the program would only need to know three things: the difficulty, question number, and whether the question or answer is being presented. It also allows me to access data in a manner similar to 2D arrays in other languages like Java and C++.

The function valid_diff allows for an easy check on whether the user typed in a valid difficulty or not. It also fits nicely in the while loop to make sure the user can type in a valid difficulty. Otherwise, the game won’t start.

I made sure that answering the questions would be flexible by allowing various whitespaces around the letter answer and allowing the user to type in the corresponding uppercase letter or lowercase letter as an answer. Thus, this can avoid confusion and controversy with formatting issues.

When the user gets correct answers, the function nscore would reward the user with more points as the game goes on. The user would also get rewarded with more points on average if the user chose a higher difficulty. This is shown by the coefficient of the problem number increasing from one to three to five with the difficulty choice going from easy to hard. Thus, the game offers a fun risk vs reward system.

After six questions, the user has the opportunity to sacrifice 4 points for a bonus question. I decided to include this as a way to mess with the user for fun. This idea took inspiration for how the original anime series messed with the viewers a lot through nonlinear storytelling and weird power schemes. This bonus question can help the user get the opportunity to earn even more points. The amount of points earned by this question depends on how the user feels about the game on a scale from 1 to 10 and what number they picked from 1 to 8.

This allowed me to define more functions. One function, order(num), converted the number between 1 to 8 to another number between 1 to 8. This function depended on two factors: the chronological order of the movie of the corresponding number and the general consensus of the movie of the corresponding number. Thus, the function order(num) gives a complicated answer after the user types in a number from 1 to 8. It even gave a nice opportunity to include a bit of recursion if the user chose a number in the upper half, except for 6. Since the sixth movie was the weakest movie, I decided to make a joke where the user would lose more points if they chose the number 6. This also results in the 87% success rate mentioned in the warning for the bonus question.

The other function, funalg, is designed to punish people who gave invalid ratings of the game, with the rating being outside the range (1,10). If the user gave a valid rating, it would then return a product between order(num) and the user’s feeling about the game. This product would then be the added number of points to the player’s score if they get the bonus question correct.

With these functions and design choices, I made sure to keep the game simple to understand and unpredictable enough to bring fun replayability to the trivia game.
