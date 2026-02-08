# Sokoban Game Implementation

## Project Overview

This project is a complete implementation of the classic puzzle game **Sokoban**, built from scratch using **Python** and **Pygame**. The objective was to design a robust game engine capable of handling grid-based movement, collision detection, and state management, while adhering to clean code practices.

It features a modular architecture separating the game loop, level data parsing, and rendering logic, making it easily extensible for new features or levels.

## Tech Stack & Key Concepts

*   **Language**: Python 3
*   **Library**: Pygame (for rendering and event handling)
*   **Key Attributes**:
    *   **2D Array Manipulation**: The game grid is represented and manipulated as a matrix of characters.
    *   **File I/O**: Custom parser to read level designs from text files (`.txt`).
    *   **Algorithm Design**: Logic for player movement, box pushing rules, and win condition verification.
    *   **Data Structures**: Utilization of lists and dictionaries for efficient state tracking.
    *   **Object-Oriented Programming**: encapsulation of game state in `Level` and `Environment` classes.

## Features

*   **Classic Gameplay**: all standard rules of Sokoban implemented faithfully.
*   **Level Loading System**: Dynamically loads levels from text files, supporting standard Sokoban level formats.
*   **Undo Functionality**: Implements a standard undo feature allowing players to revert mistakes.
*   **Theme Support**: Architecture supports multiple visual themes (currently set to 'default').
*   **Responsive Rendering**: Auto-scales game tiles based on window size and level dimensions.

## Project Structure

*   `main.py`: **Entry Point**. Contains the main game loop, event listening (keyboard inputs), and high-level game logic.
*   `Level.py`: **Data Model**. Manages the state of the current level, including the grid matrix and player/box positions.
*   `Environment.py`: **View/Display**. Handles Pygame window initialization and asset path management.
*   `levels/`: Directory containing level set files.
*   `themes/`: Directory containing graphical assets (sprites).

## How to Play

### Controls
*   **Arrow Keys**: Move Player (Up, Down, Left, Right)
*   **U**: Undo last move
*   **R**: Restart current level
*   **ESC**: Quit game


## Future Improvements

*   **Pathfinding Algorithm (A*)**: To implement an "auto-walk" feature for the player.
*   **Level Editor**: A GUI to allow users to create and save their own levels.
*   **Score System**: Tracking move counts and time to add a competitive element.


