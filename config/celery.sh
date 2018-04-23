#!/bin/bash
APP_LOCATION=/home/likun/app/blockcashflow
cd $APP_LOCATION
source /home/likun/env/bin/activate

function start(){
    python manage.py celery worker -B -l info >> $APP_LOCATION/logs/task.log 2>&1 &
    echo "Start celery services [OK]"
    ps aux|grep celery
}
function stop(){
    killall -ulikun -9 python
    echo "Stop celery services [OK]"
    ps aux|grep celery
}
function restart(){
    killall -ulikun -9 python
    python manage.py celery worker -B -l info >> $APP_LOCATION/logs/task.log 2>&1 &
    echo "Restart celery services [OK]"
    ps aux|grep celery
}
case $1 in 
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        restart
    ;;
    *)
        echo "Usages: [start|stop|restart]"
    ;;
esac
