/*
    Level3 : 기능개발
    URL = https://programmers.co.kr/learn/courses/30/lessons/42586
*/

const progresses = [5, 5, 5]

const speeds = [21, 25, 20]

function solution(progresses, speeds) {
    let len = progresses.length,
        result = []
    for (let i = 0; i < len; i++) {
        result.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    console.log(result)

    var answer = []
    let cnt = 0,
        check = result[0]


    for (let i = 0; i < len; i++) {
        if (result[i] > check) {
            check = result[i]
            answer.push(cnt)
            cnt = 0
            if (i == len - 1) {
                answer.push(cnt + 1)
                break
            }
        }
        cnt++
        if (i == len - 1) {
            answer.push(cnt)
            break
        }
    }
    console.log(answer)


    return answer;
}

solution(progresses, speeds)