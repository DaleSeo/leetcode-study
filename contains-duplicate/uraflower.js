/**
 * 입력 배열 내 값 중복 여부를 반환하는 함수
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function (nums) {
  const set = new Set();

  for (const num of nums) {
    if (set.has(num)) return true;
    else set.add(num);
  }

  return false;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
