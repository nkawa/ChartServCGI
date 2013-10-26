#!/bin/bash
echo "Content-Type: text/html"
echo

cat << __END__
<!DOCTYPE HTML>
<HTML lang="ja_JP">
<HEAD>
<meta name="viewport" content="width=device-width,initial-scale=1">
<TITLE>
Happy Chart
</TITLE>
</HEAD
<BODY>
<center>
<h2> Happy Chart </h2>
<a href="http://hc.lisra.jp/mobile">
<IMG src=
__END__

FN=`echo $QUERY_STRING | sed 's/%2F/\//g'`

echo \"http://chart.lisra.jp/${FN}\"

cat << __NEXT__
/>
<br>
あなたの地域はありました?<br>
なければ、ぜひHappyChartをお試しください。
</a>
</center>
</BODY>
</HTML>

__NEXT__

