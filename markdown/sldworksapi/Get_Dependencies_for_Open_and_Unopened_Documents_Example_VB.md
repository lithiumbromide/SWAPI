---
title: "Get Dependencies for Open and Unopened Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dependencies_for_Open_and_Unopened_Documents_Example_VB.htm"
---

# Get Dependencies for Open and Unopened Documents Example (VBA)

This example shows how to get the names of any dependencies for an open or unopened document.

```
'----------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the dependencies for the specified drawing
'    document.
' 2. Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    ' Name of unopened document
    Const sDefaultName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim sDocName As String
    Dim vDepend As Variant
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    If Not swModel Is Nothing Then
        sDocName = swModel.GetPathName
    Else
        sDocName = sDefaultName
    End If
```

```
    vDepend = swApp.GetDocumentDependencies2(sDocName, True, True, False)
    Debug.Print sDocName
    If IsEmpty(vDepend) Then
        Debug.Print "    No dependencies."
        Exit Sub
    End If
```

```
    For i = 0 To (UBound(vDepend) - 1) / 2
        Debug.Print "    " + vDepend(2 * i) + " --> " + vDepend(2 * i + 1)
    Next i
```

```
End Sub
```
