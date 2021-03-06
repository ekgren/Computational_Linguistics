Computational_Linguistics
=========================

Git commandos
-------------
To add a remote repo use:

    git remote add origin url
    git branch --set-upstream master origin/master
    
To remove a remote branch:

    git push origin --delete <branchName>
    
------
Code guidelines - PEP 8 -- Style Guide for Python Code:
http://www.python.org/dev/peps/pep-0008/

Styleguide:

    Indentation:
        Always use 4 spaces as indentation ALWAYS!
        
        NEVER mix tabs and spaces.
        
    Maximum Line Length:
        All lines are limited to a maximum of 79 characters.
        
        Comment lines are a maximum of 72 characters.
        
        Use implied line continuation:
            Good:
            def mapper(self,beard_str,kilt_str,
                        shoes_int,horse_str,cat_str):
                math.random()
            Bad:
            def mapper(self,beard_str,kilt_str
                ,shoes_int,horse_str,cat_str):
                math.random()
                
    Blank lines:
        Separate top-level function and class definitions with two blank lines.
        
        Method definitions inside a class are separated by a single blank line.
        
        Extra blank lines may be used (sparingly) to separate groups of related functions.
        
        Use blank lines in functions, sparingly, to indicate logical sections.
        
        Use two blank lines after a sentence-ending period.
        
    Encoding:
        All the code is written in ASCII only
        
        All comments are in english ONLY
        
    Imports:
        Imports should usually be on separate lines, e.g.:
            Good: 
            import os
            import sys
            
            Bad:
            import sys, os
            
        Importing specific modules from package is OK though:
            from subprocess import Popen, PIPE
            
        Imports are always put at the top of the file, just after any module comments and 
        documentation strings,and before module globals and constants.
        
        Imports should be grouped in the following order:
            1. standard library imports
            2. related third party imports
            3. local application/library specific imports
        With a blank line put between each group of imports.
        
    Comments:
        #This is an example of a comment.
        #
        #Always comment your code!
        
        Always make a priority of keeping the comments up-to-date when the code changes!
        
        Comments that contradict the code are worse than no comments.
        
        Comments should be complete sentences. 
        If a comment is a phrase or sentence, its first word should be capitalized,
        unless it is an identifier that begins with a lower case letter 
        (never alter the case of identifiers!).
        
        Use two blank lines after a sentence-ending period.
        
        Block Comments:
            Block comments generally apply to some (or all) code that follows them,
            and are indented to the same level as that code.
            
            Each line of a block comment starts with a # and a single space 
            (unless it is indented text inside the comment).
            
            Paragraphs inside a block comment are separated by a line containing a single #.
        
        Inline Comments:
            Use inline comments sparingly.
            
            An inline comment is a comment on the same line as a statement.
            Inline comments should be separated by four spaces from the statement.
            They should start with a # and a single space.
            
            Inline comments are unnecessary if they state the obvious. Don't do this:
                x_int = x_int + 1    # Increment x
            But sometimes, this is useful:
                x_int = x_int + 1    # Compensate for border
        Documentation Strings:
            '''This is a documentation string
            '''
            
            Write docstrings for all public modules, functions, classes, and methods.
            Docstrings are not necessary for non-public methods, but you should have a comment 
            that describes what the method does. This comment should appear after the def line.
        
    Naming Conventions:
        All Variable_str, CONSTANT_str and function_name names should be informative.
            
        Style used for Variables is CapitalizedWords_str, that is VariableName followed by _type.
        
        CONSTANTS_str use capital letters only.
        
        Functions use lower_case_with_underscores.
            mixedCase is allowed only in contexts where that's already the prevailing style 
            (e.g. threading.py), to retain backwards compatibility.
        
        Class names use CapitalizedWords.
            
        All variables and CONSTANTS end with the variable type.
        The following types are used:
            str for string
            int for integer
            flt for float
            bol for boolean
                
    General Rules:
        Code should be written in a way that does not disadvantage other implementations of 
        Python (PyPy, Jython, IronPython, Cython, Psyco, and such).
            Never use x += 1, always write x = x + 1
        
            
            
            
        
        
        
        
        
        
        
        
        

