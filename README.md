# OS-Guesser
This was created originally to be a windows 7 host detector but eventually took a direction toward becoming a broader utility that guesses any host's operating system the user decides to scan.

 _____ _____   _____                                
|  _  /  ___| |  __ \                               
| | | \ `--.  | |  \/_   _  ___  ___ ___  ___ _ __  
| | | |`--. \ | | __| | | |/ _ \/ __/ __|/ _ \ '__| 
\ \_/ /\__/ / | |_\ \ |_| |  __/\__ \__ \  __/ |    
 \___/\____/   \____/\__,_|\___||___/___/\___|_|0.1[uber-alpha]    
                                                  
---Developed by Mario Pereira

  ___                            
 | _ \_  _ _ _ _ __  ___ ___ ___ 
 |  _/ || | '_| '_ \/ _ (_-</ -_)
 |_|  \_,_|_| | .__/\___/__/\___|
              |_|                

---The notion of an OS Guesser was conceived (and later designed) half way through coding/testing a different script which was intended to detect Windows 7
---operating systems in an internal network. This was then put aside as the thought and the appeal of a selective OS Guesser became stronger.
---
---The OS Guesser is designed for scanning a network with an installed Nmap package to take an educated guess as to what Operating Systems
---might be running on any host IP address that is in your network.
---
---For more details including flowchart and pseudocode please check OS Guess User and Technical Documentation available in the documents folder on GITHUB
  ___               _                       _      
 | _ \___ __ _ _  _(_)_ _ ___ _ __  ___ _ _| |_ ___
 |   / -_) _` | || | | '_/ -_) '  \/ -_) ' \  _(_-<
 |_|_\___\__, |\_,_|_|_| \___|_|_|_\___|_||_\__/__/
            |_|                                    

---Python 3.7 or later
---Nmap 7.70 or later
---Internal Network connection
---other hosts to scan
---runs on any OS platform which has the above requirements.

   ___ _   _ ___ ___  ___ 
  / __| | | |_ _|   \| __|
 | (_ | |_| || || |) | _| 
  \___|\___/|___|___/|___|
                          
---Main menu is presented like so ---> [1/SUB] | [2/SCAN] | [3/CHECK] | {4/DETAILS]
---
---If you type 1 or SUB - Scan your subnet first.
---YOU MUST RUN THE ABOVE STEP BEFORE PROCEEDING OR THE SCRIPT WILL CRASH
---
---If you type 2 or SCAN - Secondly scan each host individually.
---If you type 3 or CHECK - Thirdly create Operating System Guess summary in hostprocessed.txt file for each
---host (this is where we can compare hosts)
---
---For a more in-depth User Guide refer to the User Documentation Video (https://youtu.be/B4TzRxVQRdE)

                                    
