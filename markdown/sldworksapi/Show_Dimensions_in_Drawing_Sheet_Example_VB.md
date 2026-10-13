---
title: "Show Dimensions in Drawing Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Show_Dimensions_in_Drawing_Sheet_Example_VB.htm"
---

# Show Dimensions in Drawing Sheet Example (VBA)

This example shows how to show all of the dimensions in a drawing sheet whether the dimensions are hidden or visible.

**NOTE:** In the SOLIDWORKS Design user interface, you can hide a dimension in a drawing view using the shortcut menu. The corresponding method to do this is in the SOLIDWORKS API is IModelDoc2::HideDimension. However, there is no ready way to show a hidden dimension in the user interface without first selecting the dimension. This example shows how to traverse all display dimensions in a drawing sheet and show them.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open install\samples\tutorial\api\advdrawings\foodprocessor.sldprt.
' 2. Box-select all dimensions in DrawingView1, right-click any
'    extension line, and click Hide.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Iterates all drawing views and shows all dimensions
'    in DrawingView1.
' 2. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'----------------------------------------------------------
Option Explicit
```

```
Sub ProcessDrawing(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swView As SldWorks.View)
    Dim swAnn As SldWorks.Annotation
```

```
    Debug.Print "  " & swView.Name
    Set swAnn = swView.GetFirstAnnotation2
    Do While Not Nothing Is swAnn
        If swDisplayDimension = swAnn.GetType Then
            Debug.Print "    " & swAnn.GetName
            swAnn.Visible = swAnnotationVisible
        End If
        Set swAnn = swAnn.GetNext2
    Loop
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Debug.Print "File = " & swModel.GetPathName
```

```
    Set swView = swDraw.GetFirstView
    Do While Not Nothing Is swView
        ProcessDrawing swApp, swDraw, swView
        Set swView = swView.GetNextView
    Loop
```

```
    swModel.GraphicsRedraw2
```

```
End Sub
```
