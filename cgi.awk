BEGIN {
    for (i = 0; i < 16; i++) {
        hexc[sprintf("%c", i + (i > 9 ? 55 : 48))] = i
    }
    for (i = 32; i < 127; i++) {
        ++charset[sprintf("%c", i)]
    }
}
function urldecode(s,   a, b, c, d, i)
{
        d = ""
        for (i = 1; i <= length(s); i++) {
            c = substr(s, i, 1)
            if (c == "%") {
                a = toupper(substr(s, ++i, 1))
                b = toupper(substr(s, ++i, 1))
                c = sprintf("%c", hexc[a] * 16 + hexc[b])
            }
            else {
                sub(/+/, " ", c)
            }
            d = d (c in charset ? c : " ")
        }
        return d
}

/svg/ {
    print  $0
}
