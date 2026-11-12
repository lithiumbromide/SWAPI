---
title: "Get Paths and Titles of Parents of Virtual Component (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_CSharp.htm"
---

# Get Paths and Titles of Parents of Virtual Component (C#)

This example shows how to get the paths and titles of the parent assembly components of a virtual component.

```vb
 //-----------------------------------------------------------
 / Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\assem2.sldasm
 // 2. Open the Immediate window.
 //
 // Postconditions: The paths and titles of the parent
 // assembly components, up to and including the first non-virtual
 // parent assembly component, are printed in the Immediate Window.
 //------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;
 using System;

 namespace IsVirtualComponent3CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 doc = default(ModelDoc2);
             doc = (ModelDoc2)swApp.ActiveDoc;
             if (doc == null)
                 return;
             if (doc.GetType() != (int)swDocumentTypes_e.swDocASSEMBLY)
                 return;

             AssemblyDoc asm = default(AssemblyDoc);
             asm = (AssemblyDoc)doc;

             object[] components = null;
             components = (object[])asm.GetComponents(false);
             // Get all components

             if (components != null)
             {
                 Debug.Print("Virtual components in this assembly:");

                 foreach (Object compt in components)
                 {
                     Component2 comp =  default(Component2);
                     comp = (Component2)compt;

                     ModelDoc2 compDoc =  default(ModelDoc2);
                     compDoc = (ModelDoc2)comp.GetModelDoc2();
                     if ((compDoc != null))
                     {
                         bool result3 = false;
                         object pathChain = null;
                         object titleChain = null;
                         result3 = compDoc.Extension.IsVirtualComponent3(out pathChain, out titleChain);

                         object[] pathChainArray = null;
                         object[] titleChainArray = null;
                         pathChainArray = (object[])pathChain;
                         titleChainArray = (object[])titleChain;

                         if (result3 != false)
                         {
                             Debug.Print("  Virtual component name: " + comp.Name2);

                             Debug.Print("    " + "Paths:");
                             foreach (Object path in pathChainArray)
                             {
                                 Debug.Print("      " + path);
                             }

                             Debug.Print("    " + "Titles:");
                             foreach (Object title in titleChainArray)
                             {
                                 Debug.Print("      " + title);
                             }
                         }
                     }
                     else
                     {
                         Debug.Print(comp.Name2 + " <<< NOT LOADED >>>");
                     }
                 }
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
