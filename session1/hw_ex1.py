# 1. How to check a variable’s type?
  #To check which class the variable is, we can use type(x) with x for the variable you want to check
   #For example:
    a = "name"
    print (a,"is a type of",type(a))
  #To check whether the variable belongs to a particular class, we can use isinstance(x,#nameofclass) with x for the variable
   #For example: to check if a ="name" is an integer or not, we can do like this:
      print (a,"is an integer or not?",isinstance(a,int))
# 2. In what cases, you will get SyntaxError from the compiler telling you that some of your variables have invalid names?
  #Case1: the variable does not begin with letters 
     #For example: 123name = "abc"
  #Case2: the variable contains illegal characters
     #For example: name& = "abc" -- & is an illegal character
  #Case3: the variable contains Python keywords which define the Python's rules and structers
     #For example: class = "abc" -- class is the Python keywords


