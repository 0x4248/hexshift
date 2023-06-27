# hexshift
```
 **      ** ******** **     **  ******** **      ** ** ******** **********
/**     /**/**///// //**   **  **////// /**     /**/**/**///// /////**/// 
/**     /**/**       //** **  /**       /**     /**/**/**          /**    
/**********/*******   //***   /*********/**********/**/*******     /**    
/**//////**/**////     **/**  ////////**/**//////**/**/**////      /**    
/**     /**/**        ** //**        /**/**     /**/**/**          /**    
/**     /**/******** **   //** ******** /**     /**/**/**          /**    
//      // //////// //     // ////////  //      // // //           //     
```


Hexshift is a encryption algorithm that uses shifters to cipher hex.

> **Warning**
>
> Do not use this algorithm for anything important as it may not be as secure. Use more secure algorithms like AES or RSA.

The algorithm creates a shifter e.g `["F", "E", "7", "0", "5", "6", "1", "A", "3", "B", "4", "D", "8", "9", "C", "2"]` then uses that to shift the hex. If i have the hex number `F` and the shifter of `["F", "E", "7", "0", "5", "6", "1", "A", "3", "B", "4", "D", "8", "9", "C", "2"]` the algorithm gets the place of `F` from a upshifted list of hex numbers `["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]` and gets the value of `F` which is `15` then gets what place `15` is in the shifted list which is `2` so then `F` becomes `2`. This process is repeated a number of set times and each iteration has a new shifter.

## Licence

This project is licensed under the GPL-3.0 License - see the [LICENCE](LICENCE) file for details
