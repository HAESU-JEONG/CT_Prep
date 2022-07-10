function solution(arr) {
  // defined function
  var answer = 0; // initialize answer
  var dab = arr.length; // length of arr

  for (var i = 0; i < dab; i++) {
    // repeat until i < dab
    answer += arr[i];
  }
  return answer / dab; // return answer / dab
}
