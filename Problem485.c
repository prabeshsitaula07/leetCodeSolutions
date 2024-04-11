int findMaxConsecutiveOnes(int* nums, int numsSize) 
{
    int count=0, maxCount=0;
    
    if ((numsSize > 100000) || (numsSize <1))
    {
        return -1;
    }
    
    for (int i; i <numsSize ; i++)
    {
        if (nums[i] == 1)
        {
            count++;
            if (count > maxCount)
            {
               maxCount = count;
            }
        }
        else if (nums[i]==0)
        {
            count = 0;
        }
        else 
        {
            return -1;
        }
    }
    return maxCount;
}