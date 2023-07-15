class Solution:    
    def propcontrol(self, center, res):
            #type center: int
            #type res: tuples of int
            #return type: float
            
            #TODO: Write code below to return a float with the solution to the prompt.
            #Kp= 0.6
            #remap camera to angle range 

            old_max= res[0]
            old_min= 0
            old_span=old_max-old_min
            
            new_max=1
            new_min=-1
            new_span= new_max-new_min
            return(new_min+new_span*float(center-old_min)/float(old_span))
        
        

def main():
    center = int(input().strip())
    resx = int(input().strip())
    resy = int(input().strip())
    res = (resx, resy)

    tc1 = Solution()
    ans = tc1.propcontrol(center, res)
    ans=format(ans, ".6f")
    print(ans)

if __name__ and "__main__":
    main()