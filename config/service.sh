#!/bin/bash
function start(){
    uwsgi --ini /home/likun/app/blockcashflow/config/uwsgi.ini
    echo "Start uwsgi services [OK]"
    ps aux|grep uwsgi
}
function stop(){
    killall -ulikun -9 uwsgi
    echo "Stop uwsgi services [OK]"
    ps aux|grep uwsgi
}
function restart(){
    killall -ulikun -9 uwsgi
    uwsgi --ini /home/likun/app/blockcashflow/config/uwsgi.ini
    echo "Restart uwsgi services [OK]"
    ps aux|grep uwsgi
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