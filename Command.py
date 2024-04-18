hadoop jar /opt/homebrew/Cellar/hadoop/3.4.0/libexec/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
    -files /Users/sebastianlopez/Downloads/mapper.py,/Users/sebastianlopez/Downloads/reducer.py \
    -mapper 'python3 mapper.py' \
    -reducer 'python3 reducer.py' \
    -input /Users/sebastianlopez/Downloads/airbnb_nyc_clean.csv \
    -output /Users/sebastianlopez/Downloads/output