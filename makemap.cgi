#!/bin/bash
# Create png file from SVG map
# and return URL head
#  2013/10/26 N.Kawaguchi

echo "Content-Type: text/plain"
echo

HBASE=/var/www/html
SDIR=map/$(date +%Y%m%d)
TMP=/tmp/mkmap$$.svg
awk -f /var/www/cgi-bin/cgi.awk |\
perl -e 'use URI::Escape; print uri_unescape(<STDIN>);'|\
sed 's/+/ /g' | sed 's/^svg=//' > $TMP

MD5=`md5sum $TMP | awk '{print $1}'`

if [ ! -d $HBASE/$SDIR ]; then 
    mkdir $HBASE/$SDIR
fi

if [ ! -e $HBASE/$SDIR/$MD5.png ];then
    /usr/local/bin/phantomjs /var/www/cgi-bin/mapit.js  $TMP  $HBASE/$SDIR/$MD5.png >> /tmp/makemap.log
fi

#xrm $TMP

echo $SDIR/$MD5.png



