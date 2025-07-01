#progress indicator

from tqdm import tqdm

pbar = tqdm(total=100, unit="elements", unit_scale= True)

for i in range(100):
    pbar.update()
