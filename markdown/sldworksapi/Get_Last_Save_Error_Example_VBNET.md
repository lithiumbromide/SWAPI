---
title: "Get Last Save Error Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Last_Save_Error_Example_VBNET.htm"
---

# Get Last Save Error Example (VB.NET)

```
This example shows how to get the last save error issued by Microsoft in the current SOLIDWORKS Design session.
'-------------------------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS Design session and cause Microsoft to issue a save error.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the last save error issued by Microsoft.
' 2. Examine the Immediate window.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
Partial Class SolidWorksMacro
    Dim varPath As Object
     Dim varError As Object
     Dim varMessage As Object
    Sub main()
        varMessage = swApp.GetLastSaveError(varPath, varError)
         If Not varError = 0 Then
             Debug.Print("Document generating the save error: " & varPath)
             Debug.Print("Error code: " & varError)
             Debug.Print("Error message: " & varMessage)
         Else
             Debug.Print("This SOLIDWORKS Design session has not experienced a save error.")
         End If

     End Sub
    Public swApp As SldWorks
End Class
```
