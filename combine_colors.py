class   Colors_Remix:
        """
        A class to manage color codes by combining styles and colors.
        In the script where you want to use the 'Colors_Remix' class,

        (1)  Include the following statement at the top:

        >>>    from combine_colors import Colors_Remix

        (2)  Create dictionaries for text styling and color codes:

        >>>    styles = {
        >>>        'reg': '\033[0m',  # Regular
        >>>        'drk': '\033[1m',  # Dark
        >>>        'itl': '\033[3m',  # Italic
        >>>        'und': '\033[4m',  # Underline
        >>>        'stk': '\033[9m',  # Strikethrough
        >>>    }
        >>>    colors = {
        >>>        'red': '\033[31m',  # Red
        >>>        'gre': '\033[32m',  # Green
        >>>        'mos': '\033[33m',  # Moss
        >>>        'blu': '\033[34m',  # Blue
        >>>        'prp': '\033[35m',  # Purple
        >>>        'cyn': '\033[36m',  # Cyan
        >>>        'blk': '\033[37m',  # Black
        >>>    }

        (3)  Create a dictionary of all possible style and color combinations:

        >>>    combinations = Colors_Remix.create_combo(styles, colors, False)
        >>>    combinations.update(Colors_Remix.create_combo(styles, colors, True))

        (4)  Define an object for resetting special formatting to default:

        >>>    reg = Colors_Remix(styles['reg'], styles, colors)

        (5)  Make each combination available as a global variable by iterating through 'combinations':

        >>>    for combo_name in combinations.keys():
        >>>        globals()[combo_name] = combinations[combo_name]

        For an example on implementing steps (2) to (5) in your scripts, see lines 144 to 161 of this module. It
        will demonstrate how you can integrate this 'Colors_Remix' class to generate simplified formatted output.
        """


        def __init__(his   ,   code: str   ,   styles: str   ,   colors: str):
              his.decode   =   code
              his.styles   =   styles
              his.colors   =   colors


        def __add__ (  his   ,    her  ):
              if  not  isinstance(her , Colors_Remix):
                       return     NotImplemented

              if  not( his.decode.startswith( '\033[' )   and   her.decode.startswith( '\033[' ) ):
                       return     NotImplemented  # Ensure both objects have a common prefix '\033['

              # Extract the numeric parts from both codes
              his_digits   =   ''.join( filter( str.isdigit  ,  his.decode ) )
              her_digit    =   ''.join( filter( str.isdigit  ,  her.decode ) )
              mutations   =   f'{       his_digits       };{    her_digit    }'  # Combine the numeric parts with a semicolon separator

              return   Colors_Remix(    f'\033[{mutations}m' , his.styles , his.colors    )  # Returns a newly formattied object as a combined color code


        def __repr__(  his  ):
              return ( f"ColorsRemix(code = {his.decode!r} , styles = {his.styles!r} , colors = {his.colors!r})" )


        def __str__(   his   ):
              return   his.decode


        @classmethod
        def   create_combo(  cls  ,  styling: str  ,  colors: str  ,  highlight: bool  )  ->  dict:
              """
              Create and return every possible styling with color combinations. Five
              combinable 'styling' with seven 'colors' allow for 35 distinct remixes.

              Args:
                 styling (dict):           Dictionary of style names and their codes.
                 colors (dict):            Dictionary of color names and their codes.

              Returns:
                 dict:            The updated dictionary of style and color mixtures.
              """
              combinations = {   }

              for      style_names , style_syntax  in        styling.items(   ):
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
            for      name    in    combinations:
                     if      name  in       globals(   ):
                             del   globals(   )[   name   ]


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

              for    combo_name ,  combo_obj  in   combinations.items(   ):
                     if      not   highlight:
                             print(f"  {    combo_obj  }This line of text is written in script as '{'{'}"
                                   f"{      combo_name    }{'}'}'{styling['reg']}    using an f-string. ")
                     else:
                             print(f"  {    combo_obj  }This line of text is written in script as '{'{'}"
                                   f"{      combo_name    }{'}'}'{styling['reg']} using an f-string.    ")

              Colors_Remix.cleanup_combo(   combinations   )  # Cleaning up global variables


# Define 'styles' and 'colors' dictionary
styles  =  { 'reg'  :  '\033[0m'  ,  # Some modern terminals no longer support faint text style ('\033[2m') i.e., like the
             'drk'  :  '\033[1m'  ,  # terminal I'm currently on — it's missing both FAINT and INVERSE formats ('\033[7m')
             'itl'  :  '\033[3m'  ,
             'und'  :  '\033[4m'  ,
             'stk'  :  '\033[9m'    }
colors  =  { 'red'  :  '\033[31m' ,
             'gre'  :  '\033[32m' ,
             'mos'  :  '\033[33m' ,
             'blu'  :  '\033[34m' ,
             'prp'  :  '\033[35m' ,
             'cyn'  :  '\033[36m' ,
             'blk'  :  '\033[37m'   }
combinations        =    Colors_Remix.create_combo( styles  ,  colors  ,  False )  # Create combinations without background highlights
reg                 =    Colors_Remix(      styles['reg']  ,  styles  ,  colors )  # Define a variable for resetting format to default
combinations.update(     Colors_Remix.create_combo(styles  ,  colors  ,  True ) )  # Include combinations with highlighted backgrounds

for   combo_name    in   combinations.keys(   ):
      globals(   )[      combo_name      ]    =    combinations[ combo_name ]  # Dynamically create global variables for all possible combinations


def   main(   ):
      print(  "\n  A display of formatted text statements on screen:           \n" )  # Example usage on demonstrating how to access and
      print( f"  {undprp}The text below is printing in normal red{reg}.        \n"  #   print different styling and color mixtures using
             f"  {regred}The text above is printing in underlined purple{reg}. \n"  #   simplified three-letter abbreviations on objects
             f"  {stkred}This text is printing in strikethrough red{reg}.      \n"
             f"  {drkredbg}Now here, the text has dark red highlights{reg}.    \n"
             f"  {stkblu}This text is printing in strikethrough blue{reg}.     \n"
             f"  {regblu}While the text here is printing in normal blue{reg}.  \n"
             f"  {itlredbg}This is the text with italic red highlights{reg}.   \n"
             f"  {undgrebg}And this text has underlined green highlights{reg}. \n"
             f"  {drkmosbg}This text is printing in dark moss highlights{reg}. \n"
             f"  {regprp}The text here is printing in normal purple{reg}.      \n" )
      print(  "\n  Demonstrating how styles and colors come together in          "
              "\n  code to create some visual representation on screens:       \n" )
      Colors_Remix.show_example(   colors   ,   styles   ,   False   )  # Prints 35 combinations (no highlighting)
      Colors_Remix.show_example(   colors   ,   styles   ,    True   )  # Prints 35 combinations (w  highlighting)


if  __name__   ==   '__main__':
      main(   )
