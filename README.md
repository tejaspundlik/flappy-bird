<h1 align="center">Flappy Bird</h1>
<div align="center">
  <video src="https://github.com/tejaspundlik/flappy-bird/assets/101443790/40d2d668-a620-4e8c-acc3-95ba85bd1584" />
</div>
<p>This is a simple implementation of the popular game "Flappy Bird" using the Pygame library in Python. The game involves controlling a bird to navigate through a series of pipes without colliding with them. The bird's movement is controlled by pressing the spacebar to make it flap its wings and avoid falling down due to gravity. The game keeps track of the player's score based on the number of pipes successfully passed. When the bird collides with a pipe or hits the top/bottom boundaries of the screen, the game ends and the player can restart by pressing the spacebar. The code also includes a feature to display the top score achieved.</p>
<h1 align="center">Documentation</h1>
<br/>
<ul>
  <li><code>create_pipe()</code>: This function randomly selects a height for the pipes and creates two pipe rectangles (one for the top pipe and one for the bottom pipe) with the specified positions.</li>
  <li><code>move_pipes(pipes)</code>: This function updates the positions of the pipes by moving them to the left by 5 pixels in each frame.</li>
  <li><code>blit_pipes(pipes)</code>: This function draws the pipes onto the screen. If a pipe's bottom position is below or equal to 1024, it is drawn normally. Otherwise, the pipe is flipped vertically and drawn.</li>
  <li><code>remove_pipes(pipes)</code>: This function removes any pipes that have reached a certain position (<code>centerx == -600</code>) from the list of pipes.</li>
  <li><code>check_collision(pipes)</code>: This function checks for collisions between the bird and the pipes. It returns <code>False</code> if there is a collision or if the bird hits the top or bottom boundaries of the screen. Otherwise, it returns <code>True</code>.</li>
  <li><code>bird_animation()</code>: This function handles the animation of the bird. It selects the appropriate bird image from the <code>bird_frames</code> list based on the <code>bird_index</code> and creates a new bird rectangle with the updated position.</li>
  <li><code>score_display(game_state)</code>: This function displays the score on the screen. If the <code>game_state</code> is set to 'main_game', it renders the current score during the gameplay. Otherwise, it displays the top score achieved on the start screen.</li>
</ul>
<br/>
<p>These functions collectively control the gameplay, movement of objects (bird and pipes), collision detection, and score display in the Flappy Bird game.</p>
