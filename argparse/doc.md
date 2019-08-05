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


python sa_app.py --operation backup --host host1 --digit 888 --type s