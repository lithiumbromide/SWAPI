---
title: "Insert and Save Virtual Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Save_Virtual_Assembly_Example_VBNET.htm"
---

# Insert and Save Virtual Assembly Example (VB.NET)

This example shows how to create and save a virtual sub-assembly.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Open an Immediate Window.
 ' 3. Run this macro.
 '
 ' Postconditions:
 ' 1. First, Tools > Options > System Options > Assemblies > Save new components
'     to external files is selected, and InsertNewAssembly is called, passing in
 '     FileName to save the sub-assembly:
 '    a. MyTestValveAssembly<1> displays in the FeatureManager design tree.
 '    b. MyTestValveAssembly.sldasm is saved in the assembly's directory.
 ' 2. Next, Tools > Options > System Options > Assemblies > Save new components
'      to external files is de-selected, and InsertNewAssembly is called,
'      passing in FileName to save the sub-assembly.
 '    a. A virtual sub-assembly displays in the FeatureManager design tree.
 '    b. The FileName parameter is ignored, and the virtual sub-assembly
'        is not saved.
 ' 3. The Immediate Window displays the error codes
'      as defined in swInsertNewAssemblyErrorCode_e.
 '------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swAssy As AssemblyDoc
     Dim tmpPath As String
     Dim boolstat As Boolean
     Dim longstatus As Long
     Dim longwarnings As Long

     Sub Main()

         ' Turn on Tools > Options > System Options > Assemblies > Save new components to external files
         swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSaveNewComponentsToExternalFile, True)

         swModel = swApp.ActiveDoc
         boolstat = True
         Dim strCompModelname As String
         strCompModelname =  "MyTestValveAssembly.sldasm"

         ' Save the new assembly in the same folder as the original assembly
         tmpPath = Left(swModel.GetPathName, InStrRev(swModel.GetPathName, "\"))
         swAssy = swModel

         ' Create a virtual sub-assembly and print the error code as defined in swInsertNewAssemblyErrorCode_e
         Debug.Print("First virtual sub-assembly created and saved? " & swAssy.InsertNewAssembly(tmpPath + strCompModelname))

         ' Turn off Tools > Options > System Options > Assemblies > Save new components to external files
         swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSaveNewComponentsToExternalFile, False)

         ' Create another virtual sub-assembly and print the error code as defined in swInsertNewAssemblyErrorCode_e
         Debug.Print("Second virtual sub-assembly created but not saved? " & swAssy.InsertNewAssembly(tmpPath + strCompModelname))
     End Sub

     Public swApp As SldWorks

 End  Class
```
