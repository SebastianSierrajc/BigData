cp BigData/corte1/map-reduce/code/punto_1/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_1/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_1 -mapper "python3 mapper.py" -reducer "python3 reducer.py"

cp BigData/corte1/map-reduce/code/punto_2/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_2/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_2 -mapper "python3 mapper.py" -reducer "python3 reducer.py"

cp BigData/corte1/map-reduce/code/punto_3/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_3/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_3 -mapper "python3 mapper.py" -reducer "python3 reducer.py"

cp BigData/corte1/map-reduce/code/punto_4/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_4/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_4 -mapper "python3 mapper.py" -reducer "python3 reducer.py"

cp BigData/corte1/map-reduce/code/punto_5/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_5/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_5 -mapper "python3 mapper.py" -reducer "python3 reducer.py"

cp BigData/corte1/map-reduce/code/punto_6/mapper.py mapper.py
cp BigData/corte1/map-reduce/code/punto_6/reducer.py reducer.py

$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /punto_6 -mapper "python3 mapper.py" -reducer "python3 reducer.py"
