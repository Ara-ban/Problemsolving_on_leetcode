class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return result
        visited=[[False for col in row]for row in matrix]
        position = (0, -1)
        direction=(0,1)
        i=0
        while i < len(matrix)*len(matrix[0]):
            row=position[0]+direction[0]
            col=position[1]+direction[1]
            if not self.inBounds(matrix, row, col) or visited[row][col]:
                direction = self.turnRight(direction)
                continue
            position = (row, col)
            visited[row][col] = True
            result.append(matrix[row][col])
            i += 1
            
        return result
    def inBounds (self,matrix,row,col):
        return row >= 0 and col >= 0 \
            and row < len(matrix) and col < len(matrix[0])
    def turnRight(self, vector):
        return (vector[1], -1 * vector[0])
#main thing that i should be mentioning in this solution is that direction determines the direction of the advancement, which should be (0,1) when going right
#(1,0) when going up, (0,-1) when going left and (-1,0) when going down. 
