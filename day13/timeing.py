import cProfile
from part2np import main as np  # Assuming your code is in your_script.py
from part2my import main as my

cProfile.run('np()')
cProfile.run('my()')