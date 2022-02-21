$HADOOP_HOME/bin/hadoop jar hadoop-streaming.jar -files mapper.py,reducer.py -numReduceTasks 2 -input /data -output /test -mapper "python3 mapper.py" -reducer "python3 reducer.py"
