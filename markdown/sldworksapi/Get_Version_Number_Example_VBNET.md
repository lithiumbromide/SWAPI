---
title: "Get Version Number Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_Number_Example_VBNET.htm"
---

# Get Version Number Example (VB.NET)

This example shows how to the version number of SOLIDWORKS Design.

'-----------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions: Examine the Immediate
' window.
'------------------------------------

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim BaseVersion As String = Nothing
        Dim CurrentVersion As String = Nothing
        Dim HotFixes As String = Nothing

        Debug.Print("Version = " & swApp.RevisionNumber)
        swApp.GetBuildNumbers2(BaseVersion, CurrentVersion, HotFixes)
        Debug.Print("Major revision number: " & BaseVersion)
        Debug.Print("Build number: " & CurrentVersion)
        Debug.Print("Hot fix numbers: " & HotFixes)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
