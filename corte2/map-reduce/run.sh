hadoop-streaming -files mapper_1_5.py,reducer_1_5.py -numReduceTasks 2 -input s3://bigdatajuansierra/houseprices/price_paid_records.csv -output s3://bigdatajuansierra/houseprices/data/punto_5/mr_1 -mapper "python3 mapper_1_5.py" -reducer "python3 reducer_1_5.py"

hadoop-streaming -files mapper_2_5.py,reducer_2_5.py -numReduceTasks 2 -input s3://bigdatajuansierra/houseprices/data/punto_5/mr_1 -output s3://bigdatajuansierra/houseprices/data/punto_5/mr_2 -mapper "python3 mapper_2_5.py" -reducer "python3 reducer_2_5.py"

hadoop-streaming -files mapper_1_6.py,reducer_1_6.py -numReduceTasks 2 -input s3://bigdatajuansierra/houseprices/price_paid_records.csv -output s3://bigdatajuansierra/houseprices/data/punto_6/mr_1 -mapper "python3 mapper_1_6.py" -reducer "python3 reducer_1_6.py"

hadoop-streaming -files mapper_2_6.py,reducer_2_6.py -numReduceTasks 2 -input s3://bigdatajuansierra/houseprices/data/punto_6/mr_1 -output s3://bigdatajuansierra/houseprices/data/punto_6/mr_2 -mapper "python3 mapper_2_6.py" -reducer "python3 reducer_2_6.py"
