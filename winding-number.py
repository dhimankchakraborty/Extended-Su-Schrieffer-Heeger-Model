import numpy as np
import matplotlib.pyplot as plt
from functions import *



v = 1.5
w = 1
p = 1
q = 1
print(f"v: {v}, w: {w}, p: {p}, q: {q} =======>>> Winding Number: {winding_number(v, w, p, q, rounding_place=1)}")

v = 1
w = 1
p = 1
q = 1
print(f"v: {v}, w: {w}, p: {p}, q: {q} =======>>> Winding Number: {winding_number(v, w, p, q)}")

v = 0.5
w = 1
p = 1
q = 1
print(f"v: {v}, w: {w}, p: {p}, q: {q} =======>>> Winding Number: {winding_number(v, w, p, q)}")