---
title: "Get Scale Factor of Each Model View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Scale_of_Each_Model_View_Example_VB.htm"
---

# Get Scale Factor of Each Model View Example (VBA)

This example shows how to get the scale factor of each model view in a part document.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Click Window > Viewport > Four View.
' 3. Click a model view and spin the middle-mouse
'    button forward or back.
' 4. Open the Immediate Window.
'
' Postconditions:
' 1. Gets the number of model views in the part document.
' 2. Gets the scale factor of each model view.
' 3. Examine the Immediate Window.
'-----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim SwModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swModView As SldWorks.ModelView
Dim swModViews As Variant
Dim index As Long
Dim Count As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set SwModel = swApp.ActiveDoc
    Set swModelDocExt = SwModel.Extension
```

```
    ' Get model views
    swModViews = swModelDocExt.GetModelViews
```

```
    ' Get number of model views
    Count = swModelDocExt.GetModelViewCount
    Debug.Print "Number of model views: " & Count
```

```
    ' Get the scale factor of each model view
    For index = LBound(swModViews) To UBound(swModViews)
        Set swModView = swModViews(index)
        Debug.Print "Scale of this model view is: " & swModView.Scale2
    Next index
```

```
End Sub
```
