---
title: "Passing SafeArrays in C++"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SafeArrays.htm"
---

# Passing SafeArrays in C++

Be careful when managing SafeArray memory. If you receive a SafeArray from SOLIDWORKS, you are responsible for destroying it. Also, if you pass a SafeArray to SOLIDWORKS, then SOLIDWORKS does not destroy the SafeArray. You are responsible for destroying the SafeArray.

See:

- [Return Values](Return_Values.htm) for information and examples of handling SafeArray and Variant return values.
- [STL Container Classes and Smart Pointers](STL_Container_Classes_and_Smart_Pointers.htm) for information about using smart pointers with container classes.
- [ISafeArrayUtility Interface Overview](ISafeArrayUtility_Interface_Overview.htm) for an overview of this interface.
