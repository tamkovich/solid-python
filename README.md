# Solid principles with python

Read more:
- https://github.com/heykarimoff/solid.python/
- https://towardsdatascience.com/solid-coding-in-python-1281392a6a94


## Structure:

- On the 1st stage we had a simple file [srp/bad.py](srp/bad.py)
- Then I learned how to improve this code with SR principle [srp/good.py](srp/good.py)
- But I noticed that it doesn't follow the Open-closed principle, and I implemented [ocp.py](ocp.py)
- It was hard to remember, but I implemented also [lsp/good.py](lsp/good.py) which follows The Liskov substitution principle (LSP)
- A few moments later and with the new example based on [mamals](isp/bad.py)
  I learned The Interface Segregation Principle (ISP) [isp/good.py](isp/good.py)
- The Dependency Inversion Principle (DIP) - the most funny because I think that most of my code 
  looks like [dip/bad.py](dip/bad.py) and it would be great to improve this to the [good](dip/good.py) version
