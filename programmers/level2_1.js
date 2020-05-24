/*
    Level2 : 쇠막대기
    URL = https://programmers.co.kr/learn/courses/30/lessons/42585
*/

class stack {
    constructor() {
        this.store = []
    }

    push(item) {
        this.store.push(item)
    }

    pop() {
        return this.store.pop()
    }
}

const bar = new stack
let answer = 0

const arrangement = "()(((()())(())()))(())"

function solution(arrangement) {
    let i
    for (i = 0; i < arrangement.length; i++) {
        if (arrangement[i] == "(") {
            if (arrangement[i + 1] == ")") {
                i += 1
                answer += bar.store.length
            } else {
                bar.push(1)
                answer += 1
            }
        } else {
            bar.pop()
        }
    }

    return answer;
}

solution(arrangement)