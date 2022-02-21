echo "runing mapper reducer testing"

head -1000000 ~/price_paid_records.csv | python3 ./mapper.py | sort | python3 ./reducer.py
