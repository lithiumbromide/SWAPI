---
title: "Get Features in Reverse Order Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Features_in_Reverse_Order_Example_VB.htm"
---

# Get Features in Reverse Order Example (VBA)

This example shows how to get the names and types of features in the FeatureManager design tree in reverse chronological order.

```
'--------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names and types of features
'    in the FeatureManager design tree
'    in reverse chronological order.
' 2. Examine the Immediate window and
'    FeatureManager design tree.
'--------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swFeat                      As SldWorks.Feature
    Dim i                           As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print ""
    Debug.Print "Feature Name and Type"
    Debug.Print "====================="
    For i = 0 To swModel.GetFeatureCount - 1
        Set swFeat = swModel.FeatureByPositionReverse(i)
        If Not swFeat Is Nothing Then
            Debug.Print swFeat.Name & " [" & swFeat.GetTypeName & "]"
        End If
    Next i
```

```
End Sub
```
