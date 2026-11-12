---
title: "Create and Name Planes Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Name_Plane_Example_VB.htm"
---

# Create and Name Planes Example (VBA)

This example shows how to create five planes that are offset from each other and change each of their names.

```
'---------------------------------------------------------
' Preconditions: Open a part that has three planes and
' one of the planes is named Plane1.
'
' Postconditions:
' 1. Creates five offset planes: MyPlane1, MyPlane2,
'    MyPlane3, MyPlane4, and MyPlane5.
' 2. Examine the FeatureManager design tree and graphics
'    area.
'--------------------------------------------------------
Option Explicit
```

```
Public Sub CreateOffsetPlanes()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim Part As SldWorks.PartDoc
    Dim Model As SldWorks.ModelDoc2
    Dim planeName As String
    Dim newPlaneName As String
    Dim planeFeature As SldWorks.Feature
    Dim i As Long
    Dim planeCount As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Get the active document
    Set Model = swApp.ActiveDoc
    If Model Is Nothing Then
        Exit Sub
    End If
```

```
    ' Set name of plane for SelectByID for
    ' first pass through the loop
    newPlaneName = "Plane1"
```

```
    ' Currently three planes in the part
    planeCount = 3
```

```
    ' If your model has more than three planes or you are not
    ' sure how many planes exist in your part, then immediately
    ' after loading the part you can traverse the FeatureManager design
    ' tree (see IPartDoc::FirstFeature) and count the reference plane
    ' features using IFeature::GetTypeName to determine which
    ' features are reference planes and add them up
```

```
    ' Loop five times and create five planes offset from each other
    For i = 1 To 5
        Model.ClearSelection
        ' Select the plane from which to offset
        Model.SelectByID newPlaneName, "PLANE", 0, 0, 0
        ' Create plane offset from selected plane
        Model.CreatePlaneAtOffset 0.1, 0
        ' Increment the plane number
        planeCount = planeCount + 1
        ' Increment the plane name
        planeName = "Plane" & planeCount
        newPlaneName = "MyPlane" & i
        ' Get the Plane feature by its name
        Set planeFeature = Model.FeatureByName(planeName)
        ' Change the Plane name
        planeFeature.Name = (newPlaneName)
```

```
        Model.EditRebuild
   Next
```

```
End Sub
```
