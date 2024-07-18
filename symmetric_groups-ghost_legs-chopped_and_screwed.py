class SymGrp:
      def __init__(  self  ):
           while True:
                 try :  # Prompts user for input and validates the population and sample
                     population =  int(   input( "\n  Enter  amount of objects in group (N):  \033[1mN\033[0m  =  " )   )  ;  sample = int(   input( "  Enter  size   of   the   subgroup (r):  \033[1mr\033[0m  =  " )   )
                     if population<0:     raise  ValueError("\n Invalid input: Population size must be a positive integer. \n")
                     elif  sample<0  or   sample>population: raise  ValueError(f"\n Invalid input: Sample size should be inbetween 0 and {population}. \n")
                     else: self.samp  =   sample  ;  self.size  =   population  ;  self.shelf  =   [[0] for _ in range(self.size)]  ;  self.items  =   [[x] for x in range(1, self.samp+1)]  ;  self.matrx  =   {i: self.shelf[:] for i in range(1, self.size+1)}  ;  break
                 except ValueError as E:  print(E)
      def form_foundation( self ) ->  dict:
           if    not self.items:   raise  Exception("\n No items are available to form foundation. \n")
           current_item =  self.items.pop(0)  # Forms the initial foundation of the matrix
           for i in  range(self.size):    self.matrx[ i+1 ][i] = current_item  ;  continue
           return    self.matrx
      def extension( self ) ->  dict:
           last_key = max( self.matrx.keys() )  ;  quantify_zeros = self.matrx[last_key].count([0])  ;  item = self.items.pop(0) if self.items else max(self.matrx.values())
           for i in  range(last_key):  # Extends arrangement matrix by duplicating rows
                 left_lim =last_key+1+quantify_zeros*i  ;  right_lim = last_key+1+quantify_zeros*(i+1)
                 for j in  range(  left_lim, right_lim  ): self.matrx[j]  =  self.matrx[i+1][:]
                 self.fill_hole(   left_lim, right_lim, item   )  # Fills empty positions
           self.matrx = {k-last_key: v    for k, v in self.matrx.items() }  # Adjusts row indexes for the new rows
           for   key in    list(self.matrx.keys()):
                 if  key<1:del  self.matrx[key]  # Removes all rows that were not updated
           return    self.matrx
      def fill_hole( self, start: int, end: int, item: list, idx: int = -1 ) ->  dict:
           for   i in range(start, end):
                 j = idx+1
                 while   j<self.size:  # Holes are denoted as '[0]' entries within the matrix
                     if    self.matrx[i][j] == [0]:   self.matrx[i][j] = item  ;  idx = j  ;  break
                     j+=1  # Increments column index so items will appear in unique positions
           return    self.matrx
def main():  # Define 'spacing' dictionary  # Define 'replace' dictionary
      spacing = {    0: ':  ', 1: ' :  ', 2: '  :  ', 3: '   :  ', 4: '    :  ', 5: '     :  ', 6: '      :  '    }  ;  rst = '\033[0m'
      replace = {  '[0]': f'\033[30m[0]{rst}', '[1]': f'\033[31m[1]{rst}', '[2]': f'\033[32m[2]{rst}', '[3]': f'\033[33m[3]{rst}', '[4]': f'\033[34m[4]{rst}', '[5]': f'\033[35m[5]{rst}', '[6]': f'\033[30m[6]{rst}', '[7]': f'\033[1;31m[7]{rst}', '[8]': f'\033[1;32m[8]{rst}', '[9]': f'\033[1;30m[9]{rst}'  }
      SG = SymGrp()
      SG.form_foundation()
      for _ in range(SG.samp-1):   SG.extension() # Performs row by row extensions  # Define colors codes
      gap =  len(str(len(SG.matrx.keys( ))))-len(str( SG.size ))-len(str(SG.samp))  ;  Bld = '\033[1;44m'  ;  bld = '\033[1m'
      print(f"\n We find {bld}{len(SG.matrx.keys())}{ rst } unique configurations when arranging\n {' '*gap}{bld}{SG.samp}{rst} objects from an available total of {bld}{SG.size}{rst} elements.")  ;  print('') if max(SG.matrx.keys())<=1000 else None
      for  k, v  in  SG.matrx.items():  # Determines amount of sections needed to fit all items
           i = 1  ;  sections = max(SG.matrx.keys())//1000+1  # Default interval width is set to 1000
           if    max(SG.matrx.keys())<=1000:  # Rows are in groups for better readability
                 outputs = f'{SG.matrx[k]}'  # Not all rows will print to screen if rows are placed into groups
                 for n, v  in   replace.items():      outputs =  outputs.replace(n, v)  # Prints the first 1000 formatted rows
                 print(    f'   {bld}{k}{rst}{spacing[max( 7-len(str(k) ), 0)]}{outputs}'    )
           else:
                 while i<= sections:  # Prints the other rows in groups of 1000 per iteration
                       print('')
                       for j in range((i-1)*1000+1, i*1000+1):
                             if j  in     list( SG.matrx.keys() ):
                                   outputs = f'{SG.matrx[j]}'
                                   for n, v in  replace.items():     outputs =  outputs.replace(n, v)
                                   print( f'   {bld}{j}{rst}{spacing[max( 7-len(str(j)), 0 )]}{outputs}   ' )
                             else: return  # Program quits normally after all rows print to screen
                       while True:  # Program can end before the entire matrix prints to screen
                             order =   { '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉', '0': '₀' }  # Define 'order' dictionary
                             sub   =  str.maketrans(  order  )  # Creates a translation table
                             if SG.size is SG.samp:   msg = f'symmetric group S{str(SG.size).translate(sub)}'
                             else: msg = 'permutation group'
                             try :  # Prompts user to force quit or proceed to another section
                                   opt =  input( f"\n View more entries from interval {i*1000+1} to {(i+1)*1000}?\n Enter {Bld} 1 {rst} for {bld}MORE{rst}  or  {Bld} 0 {rst} to {bld}QUIT{rst}.  {bld}Option{rst}: " )
                                   if     opt.upper() == '1'   or   'Y' in  opt.upper(): i+=1  ;  break  # Exit current iteration and goes to next section
                                   elif   opt.upper() == '0'   or   'N' in  opt.upper(): print(f"\n Omitting {len(SG.matrx.keys())-i*1000} arrangements from {msg}. \n")  ;  return
                                   else:  raise       ValueError(f"\n Invalid input: Type in {Bld} 1 {rst}, {Bld} 0 {rst}, {Bld} Yes {rst}, or {Bld} No {rst}.  ")
                             except       ValueError  as E:  print(E)
if __name__ == '__main__':   main()