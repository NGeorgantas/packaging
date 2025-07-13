from pycounts.pycounts import count_words
from pycounts.datasets import get_flatland

# from pycounts.src.pycounts.pycounts import count_words
# from pycounts.src.pycounts.datasets import get_flatland

flatland_path = get_flatland()
result = count_words(flatland_path)
print(flatland_path)

print(result)
