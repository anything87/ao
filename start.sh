echo "Cloning Repo...."
git clone https://github.com/anything87/ao.git /ao
cd /ao
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
