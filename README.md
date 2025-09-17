# Word Search Puzzle Solver 🧩

This project is a simple **Word Search Puzzle Solver** written in Python.  
It takes a puzzle grid and a word list from text files, finds the words inside the grid, and produces an output file highlighting the found words.  

---

## 📌 Features
- Reads puzzle grids and word lists from text files.  
- Finds words in four directions:
  - Horizontal (→)  
  - Vertical (↓)  
  - Diagonal Down-Right (↘)  
  - Diagonal Up-Right (↗)  
- Marks found words in the solution grid (letters converted to uppercase and `*` added).  
- Saves the solved puzzle to a new text file.  
- Prints words that were **not found** in the puzzle.

---

## 📂 File Structure
```
.
├── bulmaca1.txt        # Puzzle grid file (example)
├── kelimeler1.txt      # Word list file (example)
├── cozum1.txt          # Generated solution file
├── solver.py           # Main Python code
└── README.md           # Project description
```

- **bulmacaX.txt** → Contains the puzzle grid (each row in a separate line).  
- **kelimelerX.txt** → Contains the words to be searched (one per line).  
- **cozumX.txt** → Generated solution file after running the program.  

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/username/word-search-solver.git
   cd word-search-solver
   ```
2. Make sure you have **Python 3** installed.  
3. Run the program:
   ```bash
   python solver.py
   ```
4. Enter the puzzle number when prompted:
   ```
   Enter the number for the puzzle you want to solve : 1
   ```

---

## ✅ Example

### Input (bulmaca1.txt)
```
abcd
efgh
ijkl
mnop
```

### Word List (kelimeler1.txt)
```
abc
gh
no
xyz
```

### Output (cozum1.txt)
```
A* B* C* d  
e  f  G* H*  
i  j  k  l  
m  N* O* p  
```

Console Output:
```
Words which are not in the table :
xyz
```




