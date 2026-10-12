---
title: "Traverse Feature Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Feature_Dimensions_Example_VB.htm"
---

# Traverse Feature Dimensions Example (VBA)

This example shows how to traverse all of the DisplayDimension objects belonging to the feature, get the underlying Dimension object, and query its value.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a feature.
'
' Postconditions:
' 1. Gets the display dimensions for the selected feature.
' 2. Click OK to close each message box.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim Feature As SldWorks.Feature
Dim theDimen As SldWorks.Dimension
Dim theDispDimen As SldWorks.DisplayDimension
Dim thevalue As Double
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
```

```
    Set Feature = Part.SelectionManager.GetSelectedObject6(1, -1)
    If (Feature Is Nothing) Then
        Exit Sub
    End If
```

```
    Set theDispDimen = Feature.GetFirstDisplayDimension
    i = 0
    While (Not theDispDimen Is Nothing)
        i = i + 1
        Set theDimen = theDispDimen.GetDimension
        thevalue = theDimen.Value
        swApp.SendMsgToUser "Dimension Value " + Str(i) + " = " + Str(thevalue)
        Set theDispDimen = Feature.GetNextDisplayDimension(theDispDimen)
    Wend
```

```
End Sub
```
