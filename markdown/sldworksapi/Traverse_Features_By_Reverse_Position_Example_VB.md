---
title: "Traverse Features By Reverse Position Example Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Features_By_Reverse_Position_Example_VB.htm"
---

# Traverse Features By Reverse Position Example Example (VBA)

## Traverse Features By Reverse Position Example (VBA)

This example shows how to traverse backwards through the list of features in the FeatureManager design tree. Features are obtained by their position using IModelDoc2::FeatureByPositionReverse.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. A part document is open in SOLIDWORKS Design.
 ' 2. Open the Immediate window.
 ' 3. Run the macro.
 '
 ' Postconditions: Examine the Immediate window for
 ' the position and names of the features in the
 ' FeatureManager design tree in reverse
 ' chronological order.
 '--------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim theFeature As SldWorks.Feature
Dim featCount As Long
Dim featName As String
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
    featCount = Part.GetFeatureCount
    For i = featCount To 1 Step -1
        Set theFeature = Part.FeatureByPositionReverse(featCount - i)
        If Not theFeature Is Nothing Then
            featName = theFeature.Name
        Debug.Print "Feature " + Str(i) + " is " + featName
        End If
    Next
```

```
    Set Part = Nothing
```

```
End Sub
```
