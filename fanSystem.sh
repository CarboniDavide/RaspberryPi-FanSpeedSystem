#!/bin/sh

### BEGIN INIT INFO
# Provides:          fan-control
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Fan cooler system for CPU
# Description:       Enable or Disable fan cooler cpu
### END INIT INFO

# Main folder for the scripts init.py and fanGO.py
# example /var/scripts/fan
DIR= ----->YOUR FOLDER HERE<-----

DAEMON=$DIR/fanGO.py
INIT=$DIR/init.py
DAEMON_NAME=fan-control

# Add any command line options for your daemon here
DAEMON_OPTS=""

# This next line determines what user the script runs as.
# Root generally not recommended but necessary if you are using the Raspberry Pi GPIO from Python.
DAEMON_USER=root

# The process ID of the script when it runs is stored here:
PIDFILE=/var/run/$DAEMON_NAME.pid

. /lib/lsb/init-functions

do_init () {
    python $INIT
}
do_start () {
    do_init
    log_daemon_msg "Starting system $DAEMON_NAME daemon"
    start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON -- $DAEMON_OPTS
    log_end_msg $?
}
do_stop () {
    log_daemon_msg "Stopping system $DAEMON_NAME daemon"
    start-stop-daemon --stop --pidfile $PIDFILE --retry 10
    do_init
    log_end_msg $?
}

case "$1" in

    start|stop)
        do_${1} &
        ;;

    restart|reload|force-reload)
        do_stop &
	sleep 3
        do_start &
        ;;

    status)
        status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
        ;;

    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status|reload|force-reload}"
        exit 1
        ;;

esac
exit 0
