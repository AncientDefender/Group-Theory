class Colors_Remix:
      """
      A class to manage color codes by combining shades and colors.
      """


      def __init__(his   ,   code   ,   shades   ,   colors):
            his.decode   =   code
            his.shades   =   shades
            his.colors   =   colors


      def __add__ (  his  ,  her  ):
            if       not     isinstance(her  ,  Colors_Remix):
                     return  NotImplemented

            if       not(    his.decode.startswith('\033[')  and  her.decode.startswith('\033[')    ):
                     return  NotImplemented  # Ensure both objects have a common prefix \033[

            # Extract the numeric parts from both codes
            his_digits   =   ''.join(filter(str.isdigit   ,   his.decode))
            her_digit    =   ''.join(filter(str.isdigit   ,   her.decode))
            mutatation   =   f'{      his_digits      };{     her_digit     }'  # Combine the numeric parts with a semicolon separator

            return   Colors_Remix(f'\033[{ mutatation }m'  ,  his.shades  ,  his.colors)  # Return a new formatting object in its combined color code


      def __repr__(  his  ):
            return ( f"ColorsRemix(code = {his.decode!r} , "
                     f"shades = {his.shades!r} ,           "
                     f"colors = {his.colors!r})            " )


      def __str__(   his   ):
            return   his.decode


      def   get_code(his , shade , color):
            shade_code  =  his.shades.get(shade , '')
            color_code  =  his.colors.get(color , '')

            return   shade_code  +  color_code


shades   =   {  'end' : '\033[0m' ,  # Define shades
                'drk' : '\033[1m' ,
                'lgt' : '\033[2m' ,
                'itl' : '\033[3m' ,  }
colors   =   {  'blk' : '\033[30m' ,  # Define colors
                'red' : '\033[31m' ,
                'gre' : '\033[32m' ,
                'brw' : '\033[33m' ,
                'blu' : '\033[34m' ,
                'prp' : '\033[35m' ,  }


def   create_combo(  shades     ,    colors  ):
      """
      Creates and returns every possible shade and color combination.Three
      combinable 'shades' and six 'colors' allow for 18 unique concoctions.

      Args:
         shades (dict):          Dictionary of shade names and their codes.
         colors (dict):          Dictionary of color names and their codes.

      Returns:
         dict: Dictionary of combined names and their corresponding colors.
      """
      combinations = {   }
      for      shade_names , shade_syntax    in    shades.items(   ):
               for   color_names , color_syntax in colors.items(   ):
                     if      shade_names  ==  'end':
                             continue  # Skip 'end' as it doesn't combine
                     combo_name =  f"{ shade_names }{ color_names }"
                     shade_obj  =  Colors_Remix(shade_syntax , shades , colors)
                     color_obj  =  Colors_Remix(color_syntax , shades , colors)
                     mutations  =  shade_obj  +  color_obj
                     combinations[ combo_name ]   =   mutations

                     globals(   )[ combo_name ]   =   mutations  # Dynamically create global variables for each combination

      return   combinations


def   cleanup_combo( combinations ):
      """
      Cleanup the dynamically created global variables for combinations.
    
      Args:
         combinations (dict): Dictionary of combination names to remove.
      """
      for  name in   combinations:
           if   name in   globals(   ):
                del  globals(   )[name]


def   show_example(  shades  ,  colors  ):
      """
      Explanations on how shades and colors fuse to create combos.

      Args:
         shades (dict): Dictionary of shade names and their codes.
         colors (dict): Dictionary of color names and their codes.
      """
      combinations = create_combo(shades , colors)
    
      for    combo_name , combo_obj   in   combinations.items(   ):
             print(  f"\n    - {combo_obj}This line of text is printed in script as {'{'}"
                     f"{combo_name}{ shades['end'] }{'}' } formatted using f-strings - "  )

      cleanup_combo( combinations )  # Clean up global variables


combinations    =    create_combo(shades , colors)  # Generate all combinations

end = Colors_Remix(  shades['end'] , shades , colors  )  # Define end variable for resetting special formatting

print( f"\nExamples on how formatted statements will appear on screen"
       f"\n { lgtprp }The text is printing in light purple  { end }. "
       f"\n { itlblu }The text is printing in   italic blue { end }. "
       f"\n { itlbrw }The text is printing in italic brown  { end }. "
       f"\n { drkblu }The text is printing in   dark  blue  { end }. "
       f"\n { lgtblu }The text is printing in   light blue  { end }. " )  # Example usage: Access and print combined formats directly

show_example(shades , colors)  # Print all 18 combinations
