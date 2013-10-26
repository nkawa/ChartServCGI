#!/usr/bin/perl

use URI::Escape;

print "Content-type: text/html\n";
print "Access-Control-Allow-Origin: http://hc.lisra.jp\n\n";


read(STDIN, $data, $ENV{'CONTENT_LENGTH'});

print "Request: $ENV{'REQUEST_METHOD'}<br>\n";
print "Content: $ENV{'CONTENT_LENGTH'}<br>\n";
print "DATA     ";
print uri_unescape($data);
