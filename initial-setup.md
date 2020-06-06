# Getting Statred

The initial setup for LFS is slightly complicated. You need to have an empty partition on your drive.

### Setting up the hard drive

I statrted my journey with a completely fresh install of ubuntu linux and so had the luxury of being able to repartition the hardrive as neccesary.

#### Some notes:

1. When partitioning the drives for starting your build. You should do all the partioning of disks form 
a live bootable usb as there is no chance that your partioning interferes with the root partition or 
any other mounted partition on your system.

2. Downloading the tarball using links on the webpage is very complicated and an alternative is to use get-packages.py
to write the name to a file and then use 
```wget --input-file="filename.txt"```
 to download the files.
 
 3. To extract all the downloaded archives use ``extract-packages.py``.
