echo "installing and updating"
sudo apt install unzip vim
sudo apt update
sudo apt upgrade

echo "coping map-reduce jar\n"
cp /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar ~/hadoop-streaming.jar

echo "Downloading dataset\n"
wget -P ~ https://objectstorage.us-ashburn-1.oraclecloud.com/n/idvvpwer9msp/b/bucket-20220209-1358/o/archive.zip


echo "unzip dataset\n"
unzip ~/archive.zip

echo "creating input directory in cluster\n"
hdfs dfs -mkdir /data

echo "put dataset into cluster input\n"
hdfs dfs -put ~/price_paid_records.csv /data
