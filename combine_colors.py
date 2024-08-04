class Colors_Remix:
      """
      A class to manage color codes by combining styles and colors.
      In the scripts where you want to use the'Colors_Remix' class,

      (1)  Include the following statement at the top:

      >>>    from combine_colors import Colors_Remix

      (2)  Create dictionaries for text styling and color codes:

      >>>    styles = {
      >>>        'reg': '\033[0m',  # Regular
      >>>        'drk': '\033[1m',  # Dark
      >>>        'itl': '\033[3m',  # Italic
      >>>    }
      >>>    colors = {
      >>>        'blk': '\033[30m',  # Black
      >>>        'red': '\033[31m',  # Red
      >>>        'gre': '\033[32m',  # Green
      >>>        'mos': '\033[33m',  # Moss
      >>>        'blu': '\033[34m',  # Blue
      >>>        'prp': '\033[35m',  # Purple
      >>>    }

      (3)  Create a dictionary of all possible style and color combinations:

      >>>    combinations = Colors_Remix.create_combo(styles, colors, False)
      >>>    combinations.update(Colors_Remix.create_combo(styles, colors, True))

      (4)  Define an object for resetting special formatting to default:

      >>>    reg = Colors_Remix(styles['reg'], styles, colors)

      (5)  Make each combination available as a global variable by iterating through 'combinations':

      >>>    for combo_name in combinations.keys():
      >>>        globals()[combo_name] = combinations[combo_name]

      For an example on implementing steps (2) to (5) in your scripts, see lines 141 to 154 of this module. It
      will demonstrate how you can integrate this 'Colors_Remix' class to generate simplified formatted output.
      """


      def __init__(his   ,   code: str   ,   styles: str   ,   colors: str):
            his.decode   =   code
            his.styles   =   styles
            his.colors   =   colors


      def __add__ (  his  ,  her  ):
            if  not  isinstance(her , Colors_Remix):
                     return  NotImplemented

            if  not( his.decode.startswith( '\033[' )   and   her.decode.startswith( '\033[' ) ):
                     return  NotImplemented  # Ensure both objects have a common prefix '\033['

            # Extract the numeric parts from both codes
            his_digits   =   ''.join( filter( str.isdigit  ,  his.decode ) )
            her_digit    =   ''.join( filter( str.isdigit  ,  her.decode ) )
            mutatation   =   f'{      his_digits      };{     her_digit     }'  # Combine the numeric parts with a semicolon separator

            return   Colors_Remix(    f'\033[{mutatation}m' , his.styles , his.colors    )  # Returns a newly formattied object as a combined color code


      def __repr__(  his  ):
            return ( f"ColorsRemix(code = {his.decode!r} , styles = {his.styles!r} , colors = {his.colors!r})" )


      def __str__(   his   ):
            return   his.decode


      @classmethod
      def   create_combo(  cls  ,  styling: str  ,  colors: str  ,  highlight: bool  )  ->  dict:
            """
            Creates and returns every possible styling & color combinations. Three
            combinable 'styling' with six 'colors' allow for 18 unique concoctions.

            Args:
               styling (dict):           Dictionary of style names and their codes.
               colors (dict):            Dictionary of color names and their codes.

            Returns:
               dict:     The updated dictionary of combinations and their mixtures.
            """
            combinations = {   }

            for      style_names , style_syntax    in      styling.items(   ):
                     for   color_names , color_syntax  in   colors.items(   ):
                           if    highlight:
                                 color_names  =  color_names  +  'bg'
                                 color_syntax =  color_syntax.replace('[3'  ,  '[4')
                           combo_name  =  f"{    style_names    }{    color_names    }"
                           style_obj   =  cls(   style_syntax  ,  styling  ,  colors   )
                           color_obj   =  cls(   color_syntax  ,  styling  ,  colors   )
                           mutations   =  style_obj    +    color_obj
                           combinations[  combo_name  ]  =  mutations

            return         combinations


      @staticmethod
      def   cleanup_combo( combinations: dict )  ->  None:
            """
            Cleanup the dynamically created global variables for combinations.
    
            Args:
               combinations (dict): Dictionary of combination names to remove.
            """
            for      name  in      combinations:
                     if    name    in    globals(   ):
                           del     globals(   )[name]


      @staticmethod
      def   show_example(  colors: str  ,  styling: str  ,  highlight: bool  )  ->  None:
            """
            Explains how styling and colors fuse together to create a combination.
            This method will demonstrate each possible combination of styling and
            colors to produce and display all formatted colored text in terminals.

            Args:
               colors (dict):           Dictionary of color names and their codes.
               styling (dict):          Dictionary of style names and their codes.
            """
            combinations = Colors_Remix.create_combo(styling , colors , highlight)

            for    combo_name , combo_obj  in  combinations.items(   ):
                   if      not  highlight:
                           print(f"  {  combo_obj  }This line of text is written in script as '{'{'}"
                                 f"{    combo_name    }{'}'}'{styling['reg']}    using an f-string. ")
                   else:
                           print(f"  {  combo_obj  }This line of text is written in script as '{'{'}"
                                 f"{    combo_name    }{'}'}'{styling['reg']}  using an f-string.   ")

            Colors_Remix.cleanup_combo( combinations )  # Cleaning up global variables


# Define 'styles' and 'colors' dictionary
styles  =  { 'reg'  :  '\033[0m'  ,  # Some modern terminals no longer support faint text style ('\033[2m') i.e., like the
             'drk'  :  '\033[1m'  ,  # terminal I'm currently on — it's missing both 'dim' and 'inverse' style ('\033[7m')
             'itl'  :  '\033[3m'  , }
colors  =  { 'red'  :  '\033[31m' ,
             'gre'  :  '\033[32m' ,
             'mos'  :  '\033[33m' ,
             'blu'  :  '\033[34m' ,
             'prp'  :  '\033[35m' ,
             'blk'  :  '\033[37m' , }
combinations        =    Colors_Remix.create_combo(styles  ,  colors  ,  False)  # Create combinations without any highlighting
reg                 =    Colors_Remix(   styles['reg']  ,  styles  ,  colors   )  # Define a variable to reset special formatting
combinations.update(     Colors_Remix.create_combo( styles , colors , True )     )  # Include combinations with highlighted backgrounds
for   combo_name    in   combinations.keys(   ):
      globals(   )[      combo_name      ]  =  combinations[ combo_name ]  # Dynamically create global variables for all possible combinations


def   main(   ):
      print(  "\n  A display of formatted text statements on screen:          \n"  )  # Example usage demonstrating how to access
      print( f"  {drkprp}The text below is printing in normal red{reg}.       \n"  # and print different style and color mixtures
             f"  {regred}The text above is printing in dark purple{reg}.      \n"  # using simple three-letter code abbreviations
             f"  {drkred}This text is printing in dark red{reg}.              \n"
             f"  {drkredbg}Now here, the text has dark red highlights{reg}.   \n"
             f"  {drkblu}This text is printing in dark blue{reg}.             \n"
             f"  {regblu}While the text here is printing in normal blue{reg}. \n"
             f"  {regredbg}This is the text with normal red highlights{reg}.  \n"
             f"  {reggre}And this text is printing with normal green{reg}.    \n"
             f"  {drkmosbg}This text is printing in dark moss highlights{reg}.\n"
             f"  {regprp}The text here is printing in normal purple{reg}.     \n" )

      print( "\n  Demonstrating how styles and colors come together as          "
             "\n  code to create their visual representations on screen:      \n" )

      Colors_Remix.show_example(   colors   ,   styles   ,   False   )  # Prints 18 combinations (no highlighting)
      Colors_Remix.show_example(   colors   ,   styles   ,    True   )  # Prints 18 combinations (w  highlighting)


if    __name__  ==  '__main__':
        main(   )
