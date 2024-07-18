class SymGrp:
      """
      The set of all permutations of n objects {1, 2, 3, ... , n} form a group of order n!
      The following example demonstrates the creation of S₄, the degree 4 symmetric group:
                                                           __ __ __ __ __ __ __ __ __ __  
      P(4,1) represents the 1st permutation of 4 elements.|
                                                          |For each permutation in P(4,1),
                  [1], [0], [0], [0]                      |we extend it by placing item 2
                  [0], [1], [0], [0]                      |in each of the empty positions
                  [0], [0], [1], [0]                      |while keeping item 1 unchanged.
                  [0], [0], [0], [1]                      |
                                                          |From first row [1],[0],[0],[0]:
      Each line in the group corresponds to a permutation |Place [2] in each of the empty
      where each sublist [ ] represents a position in the |positions:  [1], [2], [0], [0]
      permutation, with the number 1 indicating the first |            [1], [0], [2], [0]
      position occupied in the arrangements corresponding |            [1], [0], [0], [2]
      to each row and the 0s representing empty positions.|
                                                          |Repeat the process with second
                                                          |row and place [2] in each free
      P(4,2) represents the 2nd permutation of 4 elements.|position:   [2], [1], [0], [0]
                                                          |            [0], [1], [2], [0]
                  [1], [2], [0], [0]                      |            [0], [1], [0], [2]
                  [1], [0], [2], [0]                      |
                  [1], [0], [0], [2]                      |From third row [0],[0],[1],[0]:
                  [2], [1], [0], [0]                      |            [2], [0], [1], [0]
                  [0], [1], [2], [0]                      |            [0], [2], [1], [0]
                  [0], [1], [0], [2]                      |            [0], [0], [1], [2]
                  [2], [0], [1], [0]                      |
                  [0], [2], [1], [0]                      |And finally, processing on the
                  [0], [0], [1], [2]                      |last row:   [2], [0], [0], [1]
                  [2], [0], [0], [1]                      |            [0], [2], [0], [1]
                  [0], [2], [0], [1]                      |            [0], [0], [2], [1]
                  [0], [0], [2], [1]                      |
                                                          |Combining all of the new lists 
      By systematically extending row entries from P(4,2) |found from row transformations
      and placing item [3] in each of the empty positions |in P(4,1) creates the required  
      while maintaining the order of items already placed,|entries in P(4,2), on the left.
      we can construct P(4,3). Further extensions to rows |__ __ __ __ __ __ __ __ __ __ 
      of P(4,3) with item [4] being placed in each row's empty position will yield P(4,4).

      To construct P(n,n): Start with P(n,1) where each permutation in P(n,1) has exactly
      one element in one position. For r=2,3,...,n extend the permutation tree by placing
      the (r+1)th element in each free position while keeping the already placed elements
      in their respective positions. This is an application of an ancient technique known
      as 'ghost legs', where you imagine extending each row of some permutation tree (the
      leg) by placing the next item in queue (the ghost) on each available empty position.

      After every ghost leg is summoned, an ancient permeation ritual will unfold through
      whispered incantations, as arcane symbols shimmer into existence. Within the depths
      of your mind's eye, permutations being emerging upon spectral pathways. Pay heed to
      secrets of order and chaos; Radiate our eldritch glow; Embrace humility; Find peace.
      """

      def __init__(self):
            while  True:
                    try:          # Prompts user for input and validates the population and sample
                        population  =  int(input("\n Enter  amount of objects in group (N):  \033[1mN\033[0m  =  "))
                        sample      =  int(input( " Enter  size   of   the   subgroup (r):  \033[1mr\033[0m  =  " ))

                        if    population < 0:
                              raise    ValueError("\n Invalid input: Population size must be a positive integer. \n")
                        elif  sample < 0  or  sample > population:
                              raise    ValueError(f"\n Invalid input: Sample size should be inbetween 0 and {population}. \n")
                        else:               # Initializes necessary attributes and data structures
                              self.samp  =  sample
                              self.size  =  population
                              self.shelf =  [[0]   for _ in   range(self.size)]
                              self.items =  [[x]   for x in   range(1 , self.samp + 1)]
                              self.matrx =  { i : self.shelf[ : ]   for i in   range(1 , self.size + 1) }
                              break

                    except    ValueError  as  E:
                                       print( E )

      def   form_foundation(  self  )  ->  dict:
            """
            Distributes the first item from available 'items' to successive rows in a diagonal pattern.

            Picks the first item '[1]' from 'items' list and assigns it to each row of a square matrix,
            incrementally moving to the next row and next column until all rows receive the first item.
            After placing first item, the matrix is still a square matrix with dimension = 'self.size'.

            Returns:
               dict: The updated matrix where adjacent rows are filled along a diagonal with obj '[1]'.
            """
            if      not       self.items:
                    raise     Exception("\n No items are available to form foundation. \n")

            current_item  =   self.items.pop(0)

            for     i     in  range(self.size):       # Forms the initial foundation of the matrix
                    self.matrx[i + 1][i] = current_item

            return  self.matrx

      def   extension(   self   )  ->  dict:
            """
            Extends and augments the matrix following specified rules and boundary conditions.

            Determines the max key in the 'matrx' matrix, calculates the total occurrences of
            '[0]' in its corresponding row, and makes clones of that row as new key-values in
            the matrix based on the amount of [0]s that were found in that specified row. The
            leftmost item from 'items' list is selected and then distributed into each of the
            new rows by replacing the first '[0]' in the first row, incrementally moving onto
            the next row next column until every new row contains a copy of the selected item.

            Returns:
               dict: The updated matrix with complete extensions is a deg n permutation group.
            """
            last_key       =  max( self.matrx.keys(   ) )
            quantify_zeros =  self.matrx[last_key].count([0])
            item = self.items.pop(0)   if self.items else   max(self.matrx.values(   ))

            for  i  in  range(last_key):          # Extends arrangement matrix by duplicating rows
                 left_lim  =  last_key + 1 + quantify_zeros * i
                 right_lim =  last_key + 1 + quantify_zeros * (i + 1)

                 for  j   in  range(left_lim , right_lim):
                      self.matrx[j] = self.matrx[i + 1][ : ]

                 self.fill_hole(left_lim , right_lim , item)               # Fills empty positions
                                                            # Adjusts row indexes for the new rows
            self.matrx = {k - last_key : v   for k , v in   self.matrx.items(   )}

            for  key  in list(self.matrx.keys(   )):
                 if   key < 1:
                      del     self.matrx[key]             # Removes all rows that were not updated

            return    self.matrx

      def   fill_hole(self , start: int , end: int , item: list , idx: int = -1)  ->  dict:
            """
            Methodologically fills empty slots in the 'matrix' with a specified object from 'item'.
            Iterates through rows from 'start' to 'end' in the 'matrx' matrix and assigns all rows
            starting from column 'idx' where the value is [0], with an 'item'. Update 'idx' to the
            last column filled in each row to continue filling from there in subsequent iterations.

            Args:
               start (int):                    The starting row index (inclusive) to begin filling.
               end   (int):                       The ending row index (exclusive) to stop filling.
               idx   (int):                 The starting column index to begin filling in each row.
               item (list):           The list to fill into the matrix where empty slots are found.

            Returns:
               dict: The updated matrix after filling '[1]' into holes from a preset range of rows.
            """
            for i  in range(start , end):
                j  =  idx + 1

                while j   <   self.size:    # Holes are denoted as '[0]' entries within the matrix
                      if      self.matrx[i][j] == [0]:   # Identifies a potential hole from row 'i'
                              self.matrx[i][j]  = item              # Replaces the hole with 'item'
                              idx = j              # Updates 'idx' to reflect current column index
                              break
                      j += 1    # Increments column index so items will appear in unique positions

            return    self.matrx

def   main(   ):
      spacing  =  {   0 :       ':  ' ,                              # Define 'spacing' dictionary
                      1 :      ' :  ' ,
                      2 :     '  :  ' ,
                      3 :    '   :  ' ,
                      4 :   '    :  ' ,
                      5 :  '     :  ' ,
                      6 : '      :  ' ,
                      }
      replace  =  { '[0]' :   '\033[30m[0]\033[0m' ,                 # Define 'replace' dictionary
                    '[1]' :   '\033[31m[1]\033[0m' ,
                    '[2]' :   '\033[32m[2]\033[0m' ,
                    '[3]' :   '\033[33m[3]\033[0m' ,
                    '[4]' :   '\033[34m[4]\033[0m' ,
                    '[5]' :   '\033[35m[5]\033[0m' ,
                    '[6]' :   '\033[30m[6]\033[0m' ,
                    '[7]' : '\033[1;31m[7]\033[0m' ,
                    '[8]' : '\033[1;32m[8]\033[0m' ,
                    '[9]' : '\033[1;30m[9]\033[0m' ,
                    }

      SG       =  SymGrp(   )
      SG.form_foundation(   )
      for   _  in  range(SG.samp - 1):
            SG.extension(   )                                     # Performs row by row extensions

      gap  =  len(str(len(SG.matrx.keys(   )))) - len(str(SG.size)) - len(str(SG.samp))
      Bld  =  '\033[1;44m'   ;   bld  =  '\033[1m'   ;   rst  =  '\033[0m'   # Define colors codes
      print( f"\n We find {bld}{len(SG.matrx.keys(   ))}{rst} unique configurations"
               f" when arranging\n {' ' * gap}{bld}{SG.samp}{rst} objects"
               f" from an available total of {bld}{SG.size}{rst} elements." )
      print('')   if  max(SG.matrx.keys(   )) <= 1000  else   None

      for   k , v in  SG.matrx.items(   ): # Determines amount of sections needed to fit all items
            i = 1  ;  sections = max(SG.matrx.keys(   )) // 1000 + 1       # Default width is 1000

            if   max( SG.matrx.keys(   ) ) <= 1000:    # Rows are in groups for better readability
                 outputs = f'{SG.matrx[k]}'   # Not all rows print to screen if rows are ungrouped
                 for   n , v  in replace.items(   ):
                       outputs = outputs.replace(n , v)     # Prints the first 1000 formatted rows
                 print(f'   {bld}{k}{rst}' , end = spacing[max(7 - len(str(k)) , 0)])
                 print(outputs)
            else:
                 while  i <=  sections:    # Prints the other rows in groups of 1000 per iteration
                        print('')

                        for   j    in    range((i - 1) * 1000 + 1 , i * 1000 + 1):
                              if   j  in  list( SG.matrx.keys(   ) ):
                                   outputs = f'{SG.matrx[j]}'
                                   for   n , v  in replace.items(   ):
                                         outputs = outputs.replace(n , v)
                                   print(f'   {bld}{j}{rst}' , end = spacing[max(7 - len(str(j)) , 0)])
                                   print(outputs)
                              else:
                                   return  # Program quits normally after all rows print to screen

                        while True:    # Program can end before the entire matrix prints to screen
                              order     = {'1' : '₁' ,                 # Define 'order' dictionary
                                           '2' : '₂' ,
                                           '3' : '₃' ,
                                           '4' : '₄' ,
                                           '5' : '₅' ,
                                           '6' : '₆' ,
                                           '7' : '₇' ,
                                           '8' : '₈' ,
                                           '9' : '₉' ,
                                           '0' : '₀' ,
                                           }
                              sub       =   str.maketrans(order)     # Creates a translation table

                              if   SG.size  is  SG.samp:
                                   msg  = f'symmetric group S{str(SG.size).translate(sub)}'
                              else:
                                   msg  =  'permutation group'

                              try :     # Prompts user to force quit or proceed to another section
                                   opt  =   input(f"\n View more entries from interval {i * 1000 + 1} to {(i + 1) * 1000}?"
                                                  f"\n Enter {Bld} 1 {rst} for {bld}MORE{rst}  or  {Bld} 0 {rst} to"
                                                   f" {bld}QUIT{rst}.  {bld}Option{rst}: ")

                                   if   opt.upper(   ) == '1'  or  'Y' in opt.upper(   ):
                                        i += 1                        # Increments section counter
                                        break    # Exit current iteration and goes to next section
                                   elif opt.upper(   ) == '0'  or  'N' in opt.upper(   ):
                                        print(    f"\n Omitting {len(SG.matrx.keys(   )) - i * 1000}"
                                                  f" arrangements from {msg}. \n"
                                              )
                                        return      # Gives feedback when program prematurely ends
                                   else:
                                        raise     ValueError(f"\n Invalid input: Type in {Bld} 1 {rst}, {Bld} 0 {rst},"
                                                             f" {Bld} Yes {rst}, or {Bld} No {rst}.  ")

                              except    ValueError  as  E:
                                                 print( E )

if __name__ == '__main__':
     main(   )
