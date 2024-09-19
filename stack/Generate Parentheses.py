# beats 98% in runtime
class Solution:    
    def generateParenthesis(self, n: int) -> List[str]:
        output=[]
        def generate_combination(comb,leng,leftnum,av_left_num):
            if av_left_num==0:
                return(generate_combination(comb+'(',leng+1,leftnum+1,1))
            if leftnum==n:
                output.append(comb + ')' * (2 * n - leng))
                return
            return(generate_combination(comb+'(',leng+1,leftnum+1,av_left_num+1),generate_combination(comb+')',leng+1,leftnum,av_left_num-1))

        generate_combination('(',1,1,1)
        return output