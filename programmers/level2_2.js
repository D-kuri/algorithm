/*
    Level2 : 문자열압축
    URL = https://programmers.co.kr/learn/courses/30/lessons/60057
    *2020 kakao blind recruitment
*/

const s = "xababcdcdababcdcd"
resultString = s

function solution(s) {
    let len = parseInt(s.length / 2)
    while (len != 0) {
        solve(s, len)
        len -= 1
    }
    console.log(resultString)
    console.log(resultString.length)


    var answer = 0;
    return answer;
}

function solve(s, len) {
    let start = s.slice(0, len),
        str = s.slice(len, s.length)
    let cnt = 1
    let tmpStr = ""


    while (1) {
        if (str == "") {
            if (cnt == 1) {
                tmpStr += start
            } else {
                tmpStr += String(cnt) + start
            }
            break
        }

        if (str.slice(0, len) == start) {
            str = str.slice(len, str.length)
            cnt += 1
        } else {
            if (cnt == 1) {
                tmpStr += start
            } else {
                tmpStr += String(cnt) + start
            }
            cnt = 1
            start = str.slice(0, len)
            str = str.slice(len, str.length)
        }

    }
    if (tmpStr.length < resultString.length) {
        resultString = tmpStr
    }
    /* console.log("tmpStr = " + tmpStr)
    console.log("resultString = " + resultString)
    console.log("--------------") */
}

solution(s)