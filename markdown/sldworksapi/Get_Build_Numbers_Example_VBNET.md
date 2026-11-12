---
title: "Get Build Numbers Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Build_Numbers_Example_VBNET.htm"
---

# Get Build Numbers Example (VB.NET)

This example shows how to get the build, major revision, and hot fix numbers of the SOLIDWORKS Design application.

```vb
 '-------------------------------------------------------
 ' Preconditions: Open SOLIDWORKS Design.
 '
 ' Postconditions: Inspect the Immediate window for build,
 ' major revision, and hot fix numbers.
 '-------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim BaseVersion As String
     Dim CurrentVersion As String
     Dim HotFixes As String

     Sub main()

         swApp.GetBuildNumbers2(BaseVersion, CurrentVersion, HotFixes)
         Debug.Print("SOLIDWORKS major revision number: " & BaseVersion)
         Debug.Print("SOLIDWORKS build number: " & CurrentVersion)
         Debug.Print("SOLIDWORKS hot fix numbers: " & HotFixes)

     End Sub

     Public swApp As SldWorks

 End  Class
```
