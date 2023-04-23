ps -ef | grep "play s" | grep -v grep | awk '{print $2}' | xargs kill
