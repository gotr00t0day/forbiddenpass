# INSTALLATION

```bash

git clone https://github.com/gotr00t0day/forbiddenpass.git

cd forbiddenpass

python3 forbiddenpass.y -h

```

# USAGE 

```bash

___________         ___.   .__    .___  .___           __________                                        
\_   _____/_________\_ |__ |__| __| _/__| _/____   ____\______   \_____    ______ ______                 
 |    __)/  _ \_  __ \ __ \|  |/ __ |/ __ |/ __ \ /    \|     ___/\__  \  /  ___//  ___/                 
 |     \(  <_> )  | \/ \_\ \  / /_/ / /_/ \  ___/|   |  \    |     / __ \_\___ \ \___ \                  
 \___  / \____/|__|  |___  /__\____ \____ |\___  >___|  /____|    (____  /____  >____  >                 
     \/                  \/        \/    \/    \/     \/               \/     \/     \/   v1.0           
                                                                                                         
                                                                                                         
                                                                                                         
usage: forbiddenpass.py [-h] [-p domain.com] [-d filename.txt] [-t site.com]                             
                                                                                                         
optional arguments:                                                                                      
  -h, --help            show this help message and exit                                                  
  -p domain.com, --path domain.com                                                                       
                        path to check                                                                    
  -d filename.txt, --domains filename.txt                                                                
                        domains to check                                                                 
  -t site.com, --target site.com                                                                         
                        domain to check 
 ```
 
 # EXAMPLE
 
 domains to check
 ```
 python3 forbiddenpass.py -d domains.txt
 ```
 domains to check with a path
 ```
 python3 forbiddenpass.py -d domains.txt --path login
 ```
 scan a single target
 ```
 python3 forbiddenpass.py -t https://site
 ```
 scan a single target with a path
 ```
  python3 forbiddenpass.py -t https://site --path login
 ````
