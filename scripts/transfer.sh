for file in ../generated/*.mpy
do
  cp $file /Volumes/CIRCUITPY/
done

cp ../src/boot.py /Volumes/CIRCUITPY/
cp ../src/main.py /Volumes/CIRCUITPY/