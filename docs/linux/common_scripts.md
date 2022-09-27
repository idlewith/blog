
# common scripts


## psh


put public key of jump server to business server


then put ip(user@1.1.1.1) to ~/ip file


psh.sh

```shell
#!/bin/sh

result=`cat ~/ip`

command=$1

for IP in $result
do
    printf "$IP: "
    ssh -o ConnectTimeout=3 -o ConnectionAttempts=3 -o StrictHostKeyChecking=no $IP "$command" 2>/dev/null
    echo
done 2>&1
```


only query cpu, memory or disk info for aliyun

```
sh psh.sh "lscpu|grep -E '^CPU:'|awk -F ' ' '{print \$2}'"
sh psh.sh "free -h|grep Mem|awk -F ' ' '{print \$2}'"
sh psh.sh "df -h|grep -E '/$'|awk -F ' ' '{print \$2}'"

sh psh.sh "netstat -lnpt"
sh psh.sh "netstat -lnpt|grep /|grep -v -i pid|awk -F ' ' '{print \$4}'|awk -F ':' '{print \$2}'|xargs echo"
```

query cpu, memory, disk and port together


```
sh psh.sh "lscpu|grep -E '^CPU:'|awk -F ' ' '{printf \"%sC/\",\$2}';free -h|grep Mem|awk -F ' ' '{printf \"%s/\",\$2}';df -h|grep -E '/$'|awk -F ' ' '{printf \"%s,\",\$2}';netstat -lnpt|grep /|grep -v -i pid|awk -F ' ' '{print \$4}'|awk -F ':' '{print \$2}'|xargs echo"
```