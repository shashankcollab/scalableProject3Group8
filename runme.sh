envset=$1
comment=$2
if [ "$envset" ]
then # if/then branch
  echo 'Setting up environment ... It may take some time.'
  sh ./env_create.sh
  source ~/envp/bin/activate
  pip3 install matplotlib
fi

if [ "$comment" ]
then
git pull
fi
nohup python3 dataprovider.py > output.log &
nohup python3 app.py > output.log &
python3 server.py

if [ "$comment" ]
then
git add .
git commit -m $comment
git push origin main
deactivate
fi
