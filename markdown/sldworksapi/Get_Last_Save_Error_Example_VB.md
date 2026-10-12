---
title: "Get Last Save Error Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Last_Save_Error_Example_VB.htm"
---

# Get Last Save Error Example (VBA)

This example shows how to get the last save error issued by Microsoft in the current SOLIDWORKS Design session.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS Design session and cause Microsoft to issue a save error.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the last save error issued by Microsoft.
' 2. Examine the Immediate window.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim varPath As String
Dim varError As Long
Dim varMessage As String
Sub main()
```

```
    Set swApp = Application.SldWorks
    varMessage = swApp.GetLastSaveError(varPath, varError)
    If Not varError = 0 Then
        Debug.Print "Document generating the save error: " & varPath
        Debug.Print "Error code: " & varError
        Debug.Print "Error message: " & varMessage
    Else
        Debug.Print "This SOLIDWORKS Design session has not experienced a save error."
    End If
```

```
End Sub
```
