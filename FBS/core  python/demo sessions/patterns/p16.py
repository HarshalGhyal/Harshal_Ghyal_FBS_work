for i in range(1,6):
    for j in range(1,6):
        if(j==5 or i==5 or i+j==6):
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()  



#         * 
#       * * 
#     *   * 
#   *     * 
# * * * * * 
         