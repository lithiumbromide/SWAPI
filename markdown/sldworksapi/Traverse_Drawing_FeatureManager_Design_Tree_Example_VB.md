---
title: "Traverse Drawing FeatureManager Design Tree Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Drawing_FeatureManager_Design_Tree_Example_VB.htm"
---

# Traverse Drawing FeatureManager Design Tree Example (VBA)

This example shows how to get a reference to the model underlying the drawing view and then how to traverse the FeatureManager design tree from there.

```
'---------------------------------------------
' Preconditions:
' 1. Open a drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the reference to the model underlying
'    the drawing view.
' 2. Traverses the rest of the FeatureManager
'    design tree.
' 3. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDrawModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim sModelName As String
    Dim nDocType As Long
    Dim nErrors As Long
    Dim nWarnings As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    ' Drawing sheet
    Set swView = swDraw.GetFirstView
```

```
    ' First view on the sheet
    Set swView = swView.GetNextView
```

```
    ' Determine if this is a view of a part or assembly
    sModelName = swView.GetReferencedModelName
    sModelName = LCase(sModelName)
    If InStr(sModelName, ".sldprt") Then
        nDocType = swDocPART
    Else
        nDocType = swDocASSEMBLY
    End If
```

```
    ' Get reference to underlying model
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  View = " & swView.Name
    Debug.Print "    Model = " & sModelName
```

```
    Debug.Print "Continue traversing the FeatureManager design tree"
    Set swView = swView.GetNextView
    Do While Not swView Is Nothing
        Debug.Print "  View = " & swView.Name
        Set swView = swView.GetNextView
    Loop

End Sub
```
