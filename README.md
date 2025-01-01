## iterative hashing or recursive hashing

# USAGE?? (THIS IS THE BIGGEST QUESTIONS OF ALL TIMES...)
1. USE SHA.PY TO GET THE KEYS....
2. USE SHAADD.PY TO GET THE ADDRESSES AT HIGHEST SPEED AND ACCURATE ADDRESSES OF ALL TYPE BETTER THAN
HD WALLETS
3. USE REBTC.PY TO SPLIT THEM
4. USE BAL.PY TO FETCH/CHECK REALTIME BALANCE OF THE ACCOUNTS

   ‼️ ...DONATIONS ARE WELCOME HERE.... ‼️

    contact us on our channels given in end
===========================================================================================

# HAD TO EXPLAIN !! 
DATE: 19/12/2024 

SHATHECUREV1.ZIP WORKFLOW IF YOU DONT LIKE TO FETCH ADDRESSES ONLINE !!

1. Python sha.py 1/2 "sting"  DEFINED::
   
> 1~ doing sha of given sting!! And sha256 it again and again!!
> 
> 2~ doing sha512 and then 256 of given sting!! And the same process  again and again!!
> 
> Sting~ it will be better to use the weakest stings to get the desired curve!!
> 

# COMMAND  of SHA.PY

YOU HAVE NOTHING TO DO.... 
ONLY 
[ python sha.py 1/2 (sting key hex anything)

then steps followed as GIVEN IN USAGE 

[ python3 sha.py 1  0000000000000000000000000000000000000000000001 ]

Or 

[ python3 sha.py 2  0000000000000000000000000000000000000000000001 ]

# HOW SHAADD??

1. using CMD

[ g++ -std=c++17 -O3 -pthread -o shaadd.exe shaadd.cpp -lsecp256k1 -lcrypto -lssl ]

2. Using Visual Studio Command Line
   
[ cl /EHsc /std:c++17 /O2 shaadd.cpp /link secp256k1.lib libcrypto.lib libssl.lib ] 

3. using LINUX
   
[ g++ -std=c++17 -pthread -o shaadd shaadd.cpp -lsecp256k1 -lssl -lcrypto ]

# Performance
1. For 1 million keys and 8 threads, processing time is proportional to the number of keys and cores. 
Using optimized hashing and elliptic curve operations:
> Average Keys Processed Per Second (KPS): ~100,000+ per thread.
> 
> Scales linearly with the number of cores.
>

2. THATS TOOO GOOD TO GO ?? OR MODIFY

> size_t numThreads = std::thread::hardware_concurrency();
        if (numThreads == 0) numThreads = 4;
> 

# Process??

> 1. Pythonn sha.py will save the privatekeys into file : (Infinitesha.txt)
>
>2. ./shaadd OR shaadd.exe to match keys outputs with your data base!!!
>
> All we Doing is bouncing on the weakest curves of the provided sting!!!
> 

HOPE SO YOU WILL FIND SOMETHING SUPER SOON AND DONATE SOME 

# DOORS are always open for DONATIONS 
 thank you !.....

# HOPE IT WILL HELP
[FOR ANY QUESTIONS TEXT US AT]

> CLOUDHUNTERS :: https://t.me/code_Crusaders0
> 
> KEYFOUND ::  https://t.me/privatekeydirectorygroup
> 
> ALSO FOR TRADING WITH BOTS :: https://t.me/+ggaun3gLB900MGY0
> 
> GITHUB LINK FOR MORRE :: https://github.com/Shubsaini08
> 
FOR DONATIONS : 

# CONTACT :: 
> US THROUGH DRIECT MESSAGES OR BY MAILING US :: keyfoundhunt4ever@gmail.com
> 
> OR DIRECT MESSAGE ON TELE : @Shub_saini08
>
> THANK YOU FOR READING THIS DOCUMENTATION

HAVE A WONDERFULL DAY STAY BLESSED HOPE YOU WILL HIT SOME(MONEY) SOON......
BYE !!
