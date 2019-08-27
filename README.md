<a href="https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjAnLy686HkAhVEc98KHfEaAMgQjRx6BAgBEAQ&url=https%3A%2F%2Fdev.to%2Fwiaio%2Fplay-rock-paper-scissors-using-the-esp8266-1h7&psig=AOvVaw0fbnYL94zEj6Zdhq3pCZ5p&ust=1566955818955940" title="RPS" alt="RPS"></a>

# Rock Paper Scissors (w/ Computer Vision)

> Play rock paper scissors with your computer and let the camera determine your move!

## How To Play

1) Run script
2) Remove hand/ moving objects from frame and press 'b' key to capture background
3) Place hand in frame and press 's' key to play against computer
4) Press 'l' key to see score log
5) Press 'esc' to exit game

---

## How It Works

- When you play, script captures frame and analyzes the number of fingers that are held up. Number of fingers correspond to respective move (although this method can be flawed if fingers are miscounted). Computer move is randomly selected.

## Versioning
### Version 1.0.1
> Bug fixes/ new features
- Fully functioning/compilable code

> Features to Come
- Web or GUI interface for visualization
- CNN (with Keras) approach so move detection is not limited by finger detection
- Impossible mode where AI attempts to determine user's move in advance so user always loses

---
