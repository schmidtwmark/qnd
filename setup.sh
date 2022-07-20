if [ -z "$1" ]; then
  echo "Provide a day number."
  echo "usage: $0 <DAY>"
  exit 1
fi

touch solutions/day$1.py
touch presentations/day$1.md