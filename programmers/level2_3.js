/*
    Level2 : 괄호 변환
    URL = https://programmers.co.kr/learn/courses/30/lessons/60058
    *2020 kakao blind recruitment
*/

class stack {
    constructor() {
        this.store = []
    }

    push(data) {
        this.store.push(data)
    }

    pop() {
        return this.store.pop()
    }
}

const p = "()))((()"
const result = new stack


function solution(p) {
    let str = p

    recursive(str)
    console.log(result)

    var answer = "";
    result.store.forEach(element => {
        answer += element
    })
    console.log(answer)
    return answer;
}

function recursive(str) {
    let split
    if (right(str) == 1) {
        result.push(str)
    } else {
        split = balance(str)
        let u = str.slice(0, split + 1),
            v = str.slice(split + 1, str.length)

        if (right(u) == 1) {
            result.push(u)
            recursive(v)
        } else {
            result.push("(")
            recursive(v)
            result.push(")")
            u = str.slice(1, u.length - 1)
            let reverseStr = ""
            for (let i = 0; i < u.length; i++) {
                if (u[i] == "(") {
                    reverseStr += ")"
                } else {
                    reverseStr += "("
                }
            }
            result.push(reverseStr)
        }

    }
}

function right(str) {
    let tmp = new stack
    for (let i = 0; i < str.length; i++) {
        if (str[i] == "(") {
            tmp.push(1)
        } else {
            if (tmp.store.length == 0) {
                return 0
            }
            tmp.pop()
        }
    }
    //result = tmp
    return 1
}

function balance(str) {
    let cnt = 0,
        i
    for (i = 0; i < str.length; i++) {
        if (i != 0 && cnt == 0) {
            i -= 1
            break
        }
        if (str[i] == "(") {
            cnt += 1
        } else {
            cnt -= 1
        }
    }
    return i
}
solution(p)