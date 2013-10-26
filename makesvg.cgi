#!/bin/bash
# Create png file from SVG
#  2013/10/25 N.Kawaguchi

echo "Content-Type: text/plain"
echo

HBASE=/var/www/html
SDIR=img/$(date +%Y%m%d)
TMP=/tmp/mksvg$$.svg
awk -f /var/www/cgi-bin/cgi.awk |\
perl -e 'use URI::Escape; print uri_unescape(<STDIN>);'|\
sed 's/+/ /g' | sed 's/^svg=//' > $TMP

MD5=`md5sum $TMP | awk '{print $1}'`

if [ ! -d $HBASE/$SDIR ]; then 
    mkdir $HBASE/$SDIR
fi

if [ ! -e $HBASE/$SDIR/$MD5.png ];then
    /usr/local/bin/phantomjs /var/www/cgi-bin/highcharts-convert.js -infile $TMP -outfile  $HBASE/$SDIR/$MD5.png > /dev/null
fi

rm $TMP

echo $SDIR/$MD5.png



