function pairMatch(arr, sum) {
    var pairSum;
    var i = 0;
    var j = arr.length-1
    do {
        pairSum = arr[i] + arr[j]

        if(pairSum === sum) {
            return sum
        } else if(pairSum > sum) {
            j--
        } else {
            i++
        }
    } while(i < j)

    return []
}

console.log(pairMatch([], 8))


