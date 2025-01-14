#!/usr/bin/env python3

import sqlite3

def create_database():
    conn = sqlite3.connect('finishes.db')
    c = conn.cursor()
    
    with open('finishes.sql', 'r') as f:
        sql_script = f.read()
    
    c.executescript(sql_script)
    conn.commit()
    conn.close()

def load_finishes():
    finishes = {}
    conn = sqlite3.connect('finishes.db')
    c = conn.cursor()
    for row in c.execute('SELECT score, finish FROM finishes'):
        finishes[row[0]] = row[1]
    conn.close()
    return finishes

if __name__ == '__main__':
    create_database()
