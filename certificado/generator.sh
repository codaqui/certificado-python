#!/bin/sh

#Créditos pekman
#email: fervelinux@openboxmail.com
#Licença: BSD

clear

echo $0
echo $1
echo $2
echo $3

altura = 20

width=`identify -format %w in $( ls *.jpg )`; \
  convert -background '#000000d0' -fill gray74 -gravity center -font Titillium-Web-Regular -size ${width}x$altura \
          caption:"$0" \
          $( ls *.jpg *.png *.JPG *.jpeg ) +swap -gravity south -composite up.jpg;
