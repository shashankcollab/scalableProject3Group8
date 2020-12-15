envset=$1
comment=$2
if [ "$envset" ]
then # if/then branch
  echo 'Setting up environment ... It may take some time.'
  sh ./env_create.sh
  source ~/envp/bin/activate
fi

if [ "$comment" ]
then
git pull
fi
python dataprovider.py & 
python server.py

if [ "$comment" ]
then
git add .
git commit -m $comment
git push origin main
deactivate
fi
