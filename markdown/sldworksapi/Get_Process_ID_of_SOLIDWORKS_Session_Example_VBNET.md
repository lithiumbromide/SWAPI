---
title: "Get Process ID of SOLIDWORKS Design Session Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Process_ID_of_SOLIDWORKS_Session_Example_VBNET.htm"
---

# Get Process ID of SOLIDWORKS Design Session Example (VB.NET)

This example shows how to get and verify the process ID of the current SOLIDWORKS Design session.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that only one SOLIDWORKS Design session is running.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the process ID of the SOLIDWORKS Design session.
' 2. Examine the Immediate window.
' 3. To verify the process ID, open a Command Prompt window,
'    type TASKLIST, and locate sldworks.exe in the Image Name
'    column and its process ID in the corresponding PID column.
' 4. Exit the Command Prompt window.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        ' Print the current SOLIDWORKS Design session's PID to the
        ' Immediate window
        Debug.Print("SOLIDWORKS Design process ID: " & swApp.GetProcessID)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
