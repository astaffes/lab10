#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(i for i in input("Введите первую строку: ").lower())
    b = set(i for i in input("Введите вторую строку: ").lower())
    print(f"Общие символы в двух строках: {a.intersection(b)}")
