from  threading  import Thread
from  pprint     import pprint
from  queue      import  Queue
from  time       import   time

class SymGrp:
      """
      Recursively generating subgroups of all symmetric groups on X = {x₁ , x₂ , ... , xₙ₋₁ , xₙ}. A group
      isomophism is a function between two groups that sets up a bijection between elements of the groups
      in a way that respects the given group operations. Two groups are called isomorphic if there exists
      a bijective homomorphism between them. Homomorphisms are transformations of one set into some other
      set that preserves in the second set the relations between elements of the first. On the other hand,
      a homeomorphism is a correspondence between two topologically equivalent shapes, where one shape is
      transformed into another shape by deformations eg. twisting, stretching, extending, and smoothening.
      """

      @ staticmethod
      def   nxt_lvl(matrix: list , item: list)  ->  list:
            """
            Generates a new dictionary of matrices based on the input 'matrix' ny inserting one
            of every item from list 'item' at every possible position in each row of the matrix.

            Returns:
               list: Updated matrices where the keys represent modified row indice from 'matrix'
                     and the values represent all order 'n' permutations on elements from 'item'
            """
            max_len  =  len(matrix[-1])  if matrix else  0
            new_matrix  =  [   ]

            for   perm  in  matrix:
                  for   j   in  range(max_len + 1):
                        new_perm = perm[ : ]
                        new_perm.insert(j  ,  item)
                        new_matrix.append(new_perm)

            return      new_matrix

      def   handle_input(q: Queue)  ->  None:
            """
            Prompts the user to enter the amount of items in {1,2, ... ,n}
            and stores the result (or exception) into a private queue 'q'.

            Args:
            - q (queue.Queue): a queue object where all user data is kept.

            If the user enters a valid integer, it puts the integer value
            into the queue `q`. If the user enters a value that cannot be
            converted to an integer, it puts the ValueError exception obj
            into queue `q`. If the user interrupts with keyboard (Ctrl+C),
            it puts the KeyboardInterrupt exception object into the queue.
            """
            try:
                num = int(input( "\nHow many items in {1, 2, ..., n}? n = " ).strip(   ))
                q.put(num)
            except    ValueError as  ve:
                               q.put(ve)
            except    KeyboardInterrupt:
                q.put(KeyboardInterrupt)

def   main(   ):
      q = Queue(   )
      input_thread = Thread( target = SymGrp.handle_input , args = (q , ) )
      input_thread.start(   )
      input_thread.join( timeout = 7 )  # default waiting time is 7 seconds

      if    input_thread.is_alive(   ):
            print( "\n Error: Timeout occurred. Please try again later. \n" )
            quit(   )

      result  =  q.get(   )

      if    isinstance( result , Exception ):
            print( f"\nException: {result}\n" )
      elif  isinstance( result , KeyboardInterrupt ):
            print( "\n Error: Program interrupted. Please try again later. \n" )
      else:
            num = result
            permutations  =   [[[1]]]

            while   True:
                     try:
                         if   num   <   0:
                              raise     ValueError( "\nNumber of items cannot be negative.\n" )
                         elif num   ==  0:
                              print( "\nContains only 1 permutation on the empty set,\n  "
                                     "  which is a part of the symmetric group S₀.\n  "
                                     "  S₀ is one of the trivial groups and is given as follows:\n  "
                                    f"  {[[ ]]}\n  " )
                              break
                         elif num   ==  1:
                              print( "\nContains only 1 permutation on the singleton set,\n  "
                                     "  which is a part of the symmetric group S₁.\n  "
                                     "  S₁ is one of the trivial groups and is given as follows:\n  "
                                    f"  {[[1]]}\n  " )
                              break
                         else:
                              items = [[x]  for x in  range(2 , num + 1)]
                              order = {'0': '₀' , '1': '₁' , '2': '₂' , '3': '₃' , '4' : '₄' , '5' : '₅' ,
                                       '6': '₆' , '7': '₇' , '8': '₈' , '9': '₉' , '10': '₁₀', '11': '₁₁' }

                              for   _  in  range(len(items)):
                                    item = items.pop(0)
                                    permutations = SymGrp.nxt_lvl(permutations , item)
                                    remaining    = num - len(items)
                                    len_perms    = len(permutations)
                                    print( f"\nContains the {len_perms} permutations on the set with {remaining} elements,\n  "
                                           f"  which are a part of the symmetric group S{order.get(f'{remaining}' , str(remaining))}. Extended\n  "
                                           f"  permutations in the S{order.get(f'{remaining}' , str(remaining))} group are given below:\n  " )
                                    pprint( permutations , indent  = 2 )
                              
                              return

                     except   ValueError      as      ve:
                              print( f"\nValueError: {ve}\n" )
                     except   Exception       as      e:
                              print( f"\n Exception: {e} \n" )

if  __name__  ==  '__main__':
      main(   )