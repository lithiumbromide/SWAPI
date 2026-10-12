---
title: "Smart Pointers"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Smart_Pointers.htm"
---

# Smart Pointers

Microsoft's Active Template Library (ATL) contains helper classes that simplify the use of commonly used COM interfaces, components, and structures, such as BSTRs, interface pointers, and variants.

The ATL CComPtr helper class provides a smart pointer wrapper around COM interface pointers. In this context, a smart pointer is a pointer that properly releases its reference counts toward COM interfaces when it goes out of scope.

To instantiate the interface types that you will be accessing, you use CComPtr with the interface type. For example:

CComPtr<ISldWorks> swApp

CComPtr<IModelDoc2> swModel

CComPtr<ISelectionMgr> swSelMgr

You can assign an interface pointer to your smart pointer in any of the following ways:

- Call the smart pointer's CoCreateInstance member function.
- Pass the interface's raw interface pointer to CoCreateInstance.
- Call the smart pointer's Attach member function to assign a previously created interface pointer to the smart pointer. This does not cause the smart pointer to call the smart pointer's AddRef function through the new interface pointer.
- Simple assignment through the smart pointer's assignment operator causes the smart pointer to call AddRef through the new interface pointer.

Calling the smart pointer's CoCreateInstance member function is the simplest way to create a new interface pointer. For example, to attach to the currently running instance of the sldworks.exe COM server on your local computer, use:

hres = swApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER);

Like most other smart pointers, CComPtr overrides C++ operators to make the smart pointers act like normal C++ pointers.

To set a smart pointer to the value of a pointer returned from a function, you can use the & operator, which works just like a non-smart pointer. If you need to decrement a reference count, use the smart pointer's Release member function.

To use ATL helper classes in your program, include atlbase.h in stdafx.h. For an example of using smart pointers, see [Access Assembly Example (C++ COM)](sldworksAPI.chm::/Access_Assembly_Example_CPlusPlus_COM.htm).

For more information about using smart pointers with container classes, see [STL Container Classes and Smart Pointers](STL_Container_Classes_and_Smart_Pointers.htm).

For more information about CComPtr and smart pointers, see MSDN.

Source: Williams, Mickey and Bennett, David. Visual C++ Unleashed. Sams Publishing, 2000.
