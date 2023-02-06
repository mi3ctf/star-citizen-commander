mkdir -p ../generated
rm -f ../generated/*.mpy

for file in ../src/*.py
do
  if [[ "$file" == *"boot.py" || "$file" == *"main.py" || "$file" == *"code.py" ]] 
  then
    echo "skipping file $file"
  else
    ./mpy-cross-macos-catalina-7.3.2 $file
  fi
done

for file in ../src/*.mpy
do
  mv $file ../generated
done