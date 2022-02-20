echo "coping map-reduce jar"
cp /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar hadoop-streaming.jar

echo "Downloading dataset"
wget -P ~ https://objectstorage.us-ashburn-1.oraclecloud.com/n/idvvpwer9msp/b/bucket-20220209-1358/o/archive.zip

hdfs dfs -mkdir /data
