python get-packages.py
mkdir archives
cd archives || exit

wget --input-file="urls.txt"

python3 untar-packages.py

