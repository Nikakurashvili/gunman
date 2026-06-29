# this is a text based shooter 
# where you are shooting the Ai
x = ["""
----------       ##########

 O                       O         
 |--+                 +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+                 +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+*                +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+ *               +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+  *              +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+   *             +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+    *            +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+     *           +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+      *          +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+      *          +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+       *         +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+        *        +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+         *       +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+          *      +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+           *     +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+            *    +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+             *   +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+              *  +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+               * +--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+                *+--|      
---                     ---
| |                     | |

""",
"""
##########       ##########

 O                       O         
 |--+                 +--|      
---                     ---
| |                     | |

""",
"""
##########       ----------

 O                       O         
 |--+                 +--|      
---                     ---
| |                     | |

"""]
copy_list = x.copy()

import time
import os
import random

def player_wins_p1():
    for i in x[1:]:
        os.system('cls')
        print(i)
        time.sleep(0.2)
    time.sleep(0.5)
    os.system('cls')
    print('\n\n\n🔪🔪congradulations your oponent is dead!🔪🔪\n\n\n')

def pc_wins_p1():
    for i in x[-2::-1]:
        os.system('cls')
        print(i)
        time.sleep(0.2)
    time.sleep(0.5)
    os.system('cls')
    print('\n\n')
    print('😭😭you\'re dead(r.i.p)!😭😭'.center(40))
    print('\n\n')

def player_wins_p2():
    for i in x[-2::-1]:
        os.system('cls')
        print(i)
        time.sleep(0.2)
    time.sleep(0.5)
    os.system('cls')
    print('\n\n\n🔪🔪congradulations your oponent is dead!🔪🔪\n\n\n')

def pc_wins_p2():
    for i in x[1:]:
        os.system('cls')
        print(i)
        time.sleep(0.2)
    time.sleep(0.5)
    os.system('cls')
    print('\n\n')
    print('😭😭you\'re dead(r.i.p)!😭😭'.center(40))
    print('\n\n')

while True:
    x = copy_list.copy()
    while (player := input('choose the player(p1/p2): ')).casefold() not in ('p1', 'p2'):
        print('incorrect player name!')
    while True:
        while (damage := int(input('enter the damage(1-10): '))) not in range(1,11):
            print('incorrect damage!')
        if player.casefold() == 'p1':
            time.sleep(0.4)
            os.system('cls')
            print("\n\n\n"+"your turn!".center(40)+"\n\n\n")
            time.sleep(1.5)
            if damage == 10:
                player_wins_p1()    
                break
            else:
                if damage >= x[1][11:].count('#'): 
                    player_wins_p1()
                    break
                else:
                    x[-2] = x[-2][:11]+x[-2][11:].replace('#','-',damage)
                    os.system('cls')
                    for i in x[1:-1]:
                        os.system('cls')
                        print(i)
                        time.sleep(0.2)
                    time.sleep(1.5)
                    os.system('cls')
                    for i in range(len(x[:-2])):
                        x[i] = x[i][:11]+x[i][11:].replace('#','-',damage)
            pc_damage = random.randint(1,10)
            print("\n\n\n"+"computers turn!".center(40)+"\n\n\n")
            time.sleep(1.5)
            if pc_damage == 10:
                pc_wins_p1()
                break
            else:
                if pc_damage >= x[-2][:11].count('#'): 
                    pc_wins_p1()
                    break
                else:
                    x[1] = x[1][:11].replace('#','-',pc_damage)+x[1][11:]
                    os.system('cls')
                    for i in x[-2:0:-1]:
                        os.system('cls')
                        print(i)
                        time.sleep(0.2)
                    time.sleep(1.5)
                    os.system('cls')
                    for i in range(len(x)-1, 1, -1):
                        x[i] = x[i][:11].replace('#','-',pc_damage)+x[i][11:]
        elif player.casefold() == 'p2':
            time.sleep(0.4)
            os.system('cls')
            print("\n\n\n"+"your turn!".center(40)+"\n\n\n")
            time.sleep(1.5)
            if damage == 10:
                player_wins_p2()
                break
            else:
                if damage >= x[-2][:11].count('#'): 
                    player_wins_p2()
                    break
                else:
                    x[1] = x[1][:11].replace('#','-',damage)+x[1][11:]
                    os.system('cls')
                    for i in x[-2:0:-1]:
                        os.system('cls')
                        print(i)
                        time.sleep(0.2)
                    time.sleep(1.5)
                    os.system('cls')
                    for i in range(len(x)-1, 1, -1):
                        x[i] = x[i][:11].replace('#','-',damage)+x[i][11:]
            pc_damage = random.randint(1,10)
            print("\n\n\n"+"computers turn!".center(40)+"\n\n\n")
            time.sleep(1.5)
            if pc_damage == 10:
                pc_wins_p2()    
                break
            else:
                if pc_damage >= x[1][11:].count('#'): 
                    pc_wins_p2()
                    break
                else:
                    x[-2] = x[-2][:11]+x[-2][11:].replace('#','-',pc_damage)
                    os.system('cls')
                    for i in x[1:-1]:
                        os.system('cls')
                        print(i)
                        time.sleep(0.2)
                    time.sleep(1.5)
                    os.system('cls')
                    for i in range(len(x[:-2])):
                        x[i] = x[i][:11]+x[i][11:].replace('#','-',pc_damage)
    while (play := input('play again?(y/n): ')).casefold() not in ('y', 'n'):
        print('you should choose y or n')
    if play.casefold() == 'n':
        print('bye!')
        break
    os.system('cls')

