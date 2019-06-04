#/bin/bash
EXT=svg
for i in *.${EXT}; do
	filename="${i%.*}"
	inkscape --export-area-drawing --export-dpi=1000 --export-pdf=$filename.pdf $i 

done
	

