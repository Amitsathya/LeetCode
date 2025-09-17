class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float('-inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')
            
            if ALeft <= Bright and BLeft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(ALeft, BLeft)) / 2
            elif ALeft > Bright:
                r = i - 1
            else:
                l = i + 1

        