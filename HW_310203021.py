# -*- coding: utf-8 -*-
"""
Created on Fri May 30 12:41:27 2025

@author: eray-
"""
def dosya_oku(puzzle_num):
    file1 = open(f"bulmaca{puzzle_num}.txt", "r") 
    grid = [line.strip() for line in file1]
        
    file2 = open(f"kelimeler{puzzle_num}.txt","r")
    words = [line.strip() for line in file2]
        
    return grid, words

def cikti_hazirla(grid,found_words):
    new_grid = [list(satir) for satir in grid]
    
    for word, noktalar in found_words.items():
        for (satir, sutun) in noktalar:           
            if not new_grid[satir][sutun].endswith('*'):
                new_grid[satir][sutun] = new_grid[satir][sutun].upper() + '*'           
    S = []
    for satir in new_grid:
        string_satir = ""
        for a in satir:
            if "*" in a:
                string_satir += a + " "
            else:
                string_satir += a + "  "
        S.append(string_satir)
    
    return S

def dosya_yazdir(cozum, puzzle_num):
    file3 = open(f"cozum{puzzle_num}.txt","w")
    for satir in cozum:
        file3.write(satir + "\n")
    
def ekrana_yazdir(not_found):
    if not not_found:
        print("All words exist in the table.")
    elif len(not_found) == 1:
        print("Words which are not in the table :")
        print(not_found[0])
    else:
        print("Words which are not in the table :")
        for word in not_found:
            print(word)

def find_word(grid,word):
    yonler = [(1,0),(0,1),(1,1),(-1,1)] 
    
    satirlar = len(grid)    
    if len(grid) > 0:
        sutunlar = len(grid[0])
    else:
        sutunlar = 0
    
    for i in range(satirlar):
        for j in range(sutunlar):
            for i1, j1 in yonler:
                eslesme = True
                noktalar = []
                for k in range(len(word)):
                    i2, j2 = i + k*i1, j + k*j1
                    if i2 < 0 or i2 >= satirlar or j2 < 0 or j2 >= sutunlar:
                        eslesme = False
                        break
                    if grid[i2][j2].lower() != word[k].lower():
                        eslesme = False
                        break
                    noktalar.append((i2,j2))
                if eslesme:
                    return noktalar
    return None
        
puzzle_num = input('Enter the number for the puzzle you want to solve : ')
grid, words = dosya_oku(puzzle_num)

found_words= {}
not_found = []

for word in words:
    noktalar = find_word(grid, word)
    if noktalar:
        found_words[word] = noktalar
    else:
        not_found.append(word)

cozum = cikti_hazirla(grid, found_words)
dosya_yazdir(cozum, puzzle_num)
ekrana_yazdir(not_found)