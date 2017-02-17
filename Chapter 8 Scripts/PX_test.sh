for number in $(seq -f "%g" 1 5); do 
  test_file="P${number}_test.py"
  echo "Running ${test_file}..."
  echo "-----------------------"

  python3 $test_file
  echo
done
