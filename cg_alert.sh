#!/usr/local/bin/bash

PY=/usr/local/bin/python3.7
HOME=/home/drunkbatya/scripts/cg_alert
#SERVERS
CG_ORA=
CG_CCTV=
CG_ASTERISK=
CG_SER=
CG_WWW=

#PING SERVERS
O=$(ping -c 2 $CG_ORA | grep ttl | awk '{print $4}')
C=$(ping -c 2 $CG_CCTV | grep ttl | awk '{print $4}')
A=$(ping -c 2 $CG_ASTERISK | grep ttl | awk '{print $4}')
S=$(ping -c 2 $CG_SER | grep ttl | awk '{print $4}')
W=$(ping -c 2 $CG_WWW | grep ttl | awk '{print $4}')

if [[ -z $O ]]
	then $PY $HOME/cg_alert.py ora  
fi
if [[ -z $C ]]
	then $PY $HOME/cg_alert.py cctv
fi
if [[ -z $A ]]
	then $PY $HOME/cg_alert.py asterisk
fi
if [[ -z $S ]]
	then $PY $HOME/cg_alert.py ser
fi
if [[ -z $W ]]
	then $PY $HOME/cg_alert.py www
fi
