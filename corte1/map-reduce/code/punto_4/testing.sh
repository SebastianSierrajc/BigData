echo "runing mapper reducer testing"

cat ~/price_paid_records.csv | python3 ./mapper.py | sort | python3 ./reducer.py

