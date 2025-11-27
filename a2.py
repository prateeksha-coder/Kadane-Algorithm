# standard kadane's algorithm to find maxium subarray sum
def kadane(a):
  n = len(a)
  max_ending_here = 0
  max_so_far=0
  for i in range(0,n):
    max_ending_here = max_ending_here + a[i]
    if (max_ending_here < 0):
      max_ending_here = 0

    if (max_so_far < max_ending_here):
      max_so_far = max_ending_here

  return max_so_far

# the function returns maxium circular contiguous dum in
# a[]
def maxcircularsum(a):

   n = len(a)

   # apply kadane algo if no circular is needed
   max_kadane = kadane(a)

   # find sum of all element and invert them 
   max_wrap = 0
   for i in range(0, n):
    max_wrap += a[i]
    a[i] = -a[i]
    print(a)

  # apply kadance algo to find minium inverted subarray
   max_wrap = max_wrap + kadane(a)

  #the maxium circular sum will be a maxium of two sums
   if max_wrap > max_kadane:
      return max_wrap


a=[8, -1, 3, 4]
print("maxium circular sum is", maxcircularsum(a))