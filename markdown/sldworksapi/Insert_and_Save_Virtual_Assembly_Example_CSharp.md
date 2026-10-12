---
title: "Insert and Save Virtual Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Save_Virtual_Assembly_Example_CSharp.htm"
---

# Insert and Save Virtual Assembly Example (C#)

This example shows how to create and save a virtual sub-assembly.

```vb
 //-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly document.
 // 2. Rename the namespace of this macro to match your C# project's name.
 // 3. Open an Immediate Window.
 // 4. Run this macro.
 //
 // Postconditions:
 // 1. Tools > Options > System Options > Assemblies >
//      Save new components to external files is selected,
//      and InsertNewAssembly is called, passing in FileName
//      to save the sub-assembly:
 //    a. MyTestValveAssembly<1> displays in the FeatureManager design tree.
 //    b. MyTestValveAssembly.sldasm is saved in the assembly's directory.
 // 2. Next, Tools > Options > System Options > Assemblies >
//      Save new components to external files is de-selected,
//      and InsertNewAssembly is called, passing in FileName
//      to save the sub-assembly.
 //    a. A virtual sub-assembly displays in the FeatureManager design tree.
 //    b. The FileName parameter is ignored, and the virtual sub-assembly
//        is not saved.
 // 3. The Immediate Window displays the error codes
//      as defined in swInsertNewAssemblyErrorCode_e.
 //------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace InsertNewAssembly_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         AssemblyDoc swAssy;
         string tmpPath;

         public void Main()
         {

             // Turn on Tools > Options > System Options > Assemblies > Save new components to external files
             swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSaveNewComponentsToExternalFile, true);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             string strCompModelname = null;
             strCompModelname = "MyTestValveAssembly.sldasm";

             // Save the new sub-assembly to the same folder where the parent assembly resides
             tmpPath = swModel.GetPathName();
             string[] tok;
             tok = tmpPath.Split('\\');

             // reconstruct the assembly path without the file name
             int i;
             string virAssPath = "";
             for (i = 0; i < tok.Length - 1; i++)
             {
                 virAssPath = virAssPath + tok[i] +  "\\";
             }

             Debug.Print(virAssPath);
             swAssy = (AssemblyDoc)swModel;

             // Create a virtual sub-assembly and print the error code as defined in swInsertNewAssemblyErrorCode_e
             Debug.Print("First virtual sub-assembly created and saved? " + swAssy.InsertNewAssembly(virAssPath + strCompModelname));

             // Turn off Tools > Options > System Options > Assemblies > Save new components to external files
             swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSaveNewComponentsToExternalFile, false);

             // Create another virtual sub-assembly and print the error code as defined in swInsertNewAssemblyErrorCode_e
             Debug.Print("Second virtual sub-assembly created but not saved? " + swAssy.InsertNewAssembly(virAssPath + strCompModelname));
         }

         public SldWorks swApp;

     }
 }
```
