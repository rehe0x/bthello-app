LANG="zh_CN.UTF-8"
pid=`ps ax | grep main | grep python | grep -v grep | head -1 | awk '{print $1}'`
if [ "$pid" != "" ]; then
	echo $pid
	kill $pid
fi
echo '服务停止成功,开始重启服务...'
rm -rf nohup.out
touch nohup.out

if [ ! $1 ]; then  
    $1='-a'
fi
if [ ! $2 ]; then  
    $2=80
fi

echo $1
echo $2
nohup python3 main.py $1 -port=$2 > nohup.out 2>&1 &
tail -f nohup.out
