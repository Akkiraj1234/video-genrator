
cd ~/Desktop/video-genrator
source venv/bin/activate
cd ..

python3 -m video-genrator video-genrator/assets/script.txt --video video-genrator/assets/video1.mp4

deactivate
cd video-genrator