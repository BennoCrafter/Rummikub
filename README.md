# Rummikub

## Description

Rummikub is a tile-based game for 2 to 4 players, combining elements of the card game Rummy and Mahjong. Players draw and play tiles to form sets and runs, aiming to be the first to play all their tiles.

## Installation
Clone the repository and run the game:
```bash
git clone https://github.com/BennoCrafter/rummikub.git
cd Rummikub
python main.py
```
For default parameters, run the game with:
```bash
python main.py --default
```

## Game Components

### Tiles
- **Colors**: Red, Blue, Yellow, Black
- **Numbers**: 1 to 13
- **Special Tiles**: Joker tiles that can represent any number and color

Each tile appears twice, resulting in a total of 106 tiles (including 2 jokers).

### Players
- **Number of Players**: 2 to 4
- **Hand**: Each player starts with 14 tiles.

### Sets and Runs
- **Set**: A group of three or four tiles of the same number but different colors.
- **Run**: A sequence of three or more consecutive numbers of the same color.

## Game Rules

1. **Gameplay**:
    - Players take turns to play tiles from their hand to the table to form sets or runs.
    - On their turn, a player can:
        - Play tiles from their hand to form new sets/runs.
        - Add tiles to existing sets/runs on the table.
        - Draw a tile from the draw pile if they can't make a valid move.
    - The first play for each player must have a total value of at least 30 points (sum of tile numbers).
    - Jokers can be used as substitutes for any tile.
2. **Winning**: The first player to play all their tiles wins the game.

## Commands

- **create** - Create a new tile set.
- **next** - Next player's turn.
- **draw** - Draw a tile from the deck.
- **split** - Split a run or set into two separate groups.
- **pull** - Pull a tile from a run or set.
- **put** - Put a tile into a run or set.

## Code Structure

### Classes

- `Tile`: Represents a tile with a number and color.
- `Deck`: Represents the deck of tiles, including methods to shuffle and draw tiles.
- `Player`: Represents a player with a hand of tiles.
- `Game`: Manages the overall game flow, including player turns and game rules.
