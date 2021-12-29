if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/rayner074/kurupp.git /DonLee-Robot-V2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DonLee-Robot-V2
fi
cd /DonLee-Robot-V2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
