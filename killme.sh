ps aux  |  grep -i dataprovider.py  |  awk '{print $2}'  |  xargs  kill -9
ps aux  |  grep -i server.py  |  awk '{print $2}'  |  xargs  kill -9
ps aux  |  grep -i app.py  |  awk '{print $2}'  |  xargs  kill -9