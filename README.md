### Introducing the **531 Weightlifting Calculator** for **Jim Wendler's 531 Program**
A Python script that calculates the monthly progression for inputted exercises and outputs it as a text file in a folder on the desktop (latest version).
___
 An **in-depth look into the program:** 
 <br>
https://www.lift.net/workout-routines/wendler-5-3-1/
___
### **IMPORTANT!**
**Version 5** uses **90%** of the training max (tm) whether tm was inputed or computed using "tm".<br>
**Version 4** uses **90%** for the "tm" option, but keeps the inputted value the same.<br>
**Version 3** uses **90%** for the "tm" option, but keeps the inputted value the same.<br>
**Version 2** uses **100%** for the "tm" option and keeps the inputted value the same.<br>
**Version 1** uses **100%** of the inputted value for the training max.<br>
___
### **Versions:**
___
### **Version 1:**
This script outputs the Jim Wendler's 531 program **directly in the terminal for 20 seconds**, providing users with their monthly training weights without any additional features.
___
### **Version 2:**
In this version, the script allows users to input their username and **generates the program as a text file in the directory where the script is executed**. This provides users with a convenient way to save and access their training plan. 

There are also "**tm**" and "**back**" options added.

<br>

"**tm**" calculates the training max using the formula Jim uses in his program: 

     (n_reps * weight_lifted * 0.0333 + weight_lifted) * 0.9 

(Currently uses 90% of the training max, some might prefer lower/higher percentage!)

<br>

"**back**" is used to rewrite the exercise or training max in case of a mistake. Not fully polished.
___
### **Version 3:**
For added convenience and organization, Version 3 of the script not only incorporates username input but also **creates a dedicated "Gym" folder on the desktop** if it doesn't already exist. The program is then generated and saved within this folder, ensuring easy access and tidy storage of the training plan.
___
### **Version 4:** 
This version enhances the script from its predecessor by **implementing comprehensive error prevention mechanisms**. It ensures that input data conforms to specified types and introduces a more polished "back" option to correct inaccurate inputs. There are also minor cosmetic changes to improve the experience.
___
### **Version 5:** 

Incorporates the inclusion of **floats as eligible input values**. **Adjusts** the **training max** and **training weights output** to **adhere to increments of 2.5**.
___
### **Future ideas:**
- Incorporate the possibility of choosing the percentage of a training max.
- Incorporate the possibility of continuing the previous entry (adding 5/2.5 to the training maxes and calculating again).
