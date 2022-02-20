echo "runing mapper reducer testing"

#head -2000000 ../../../../archive/price_paid_records.csv | python3 ./mapper.py | sort
head -2000000 ../../../../archive/price_paid_records.csv | python3 ./mapper.py | sort | python3 ./reducer.py

