Command

1. sacli
   1. backup
      1. host
      2. digit
      3. type
   2. restore
      1. host
      2. digit
      3. type
      4. backupLocation
   3. build
      1. branch
      2. type [clean, optimize]
   4. update
      1. host
      2. version



usage: sacli -o [backup, restor, build, update]


backup(host, digit, type)



python sacli.py backup -H=host2.cmd2.bitmascot.com -D=12654892 -T=s

python sacli.py restore -H=host2.cmd2.bitmascot.com -D=12654892 -T=s -L=sa_location

python sacli.py update -H host3.cmd3.bitmascot.com -V 3.0.7

python sacli.py build -B master -T clean