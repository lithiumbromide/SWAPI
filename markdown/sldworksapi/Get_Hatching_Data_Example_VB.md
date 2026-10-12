---
title: "Get Hatching Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hatching_Data_Example_VB.htm"
---

# Get Hatching Data Example (VBA)

This example shows how to get hatching data from a drawing view.

In a drawing view, hatching can be applied by the user to any face or, as in the case of a section view, automatically applied by the SOLIDWORKS Design software. Hatching applied by the user is accessed through the ISketchHatch object. In contrast, hatching in a section view is accessed through the IFaceHatch object.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Select Section View A-A in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets hatching data.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim swSketch As SldWorks.Sketch
    Dim vFaceHatch As Variant
    Dim swFaceHatch As SldWorks.FaceHatch
    Dim swFace As SldWorks.Face2
    Dim vSketchHatch As Variant
    Dim swSketchHatch As SldWorks.SketchHatch
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObjec6(1, -1)
    Set swSketch = swView.GetSketch
    Debug.Print "View   = " & swView.Name
    Debug.Print "  Type = " & swView.Type
    Debug.Print ""
    vFaceHatch = swView.GetFaceHatches
    If Not IsEmpty(vFaceHatch) Then
        Debug.Print "  Face hatches:"
        Debug.Print ""
        For i = 0 To UBound(vFaceHatch)
            Set swFaceHatch = vFaceHatch(i)
            Set swFace = swFaceHatch.Face
            ' Cannot select a face because a face is in model
            bRet = swFace.Select2(True, 0)
            ' Get sketch hatch data
            ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            Debug.Print "  Angle          = " & swFaceHatch.Angle * 57.3 & " degrees"
            Debug.Print "  Color          = " & swFaceHatch.Color
            Debug.Print "  Definition     = " + swFaceHatch.Definition
            Debug.Print "  Layer          = " & swFaceHatch.Layer
            Debug.Print "  Pattern        = " + swFaceHatch.Pattern
            Debug.Print "  Scale          = " & swFaceHatch.Scale2
            Debug.Print "  SolidFill      = " & swFaceHatch.SolidFill
            Debug.Print "  -----------------------"
        Next i
    End If
```

```
    vSketchHatch = swSketch.GetSketchHatches
    If Not IsEmpty(vSketchHatch) Then
        Debug.Print "  Sketch hatches:"
        Debug.Print ""
        For i = 0 To UBound(vSketchHatch)
            Set swSketchHatch = vSketchHatch(i)
            Set swFace = swSketchHatch.GetFace
            ' Cannot select a face because a face is in model
            bRet = swFace.Select2(True, 0)
            ' Get sketch hatch data
            Debug.Print "  Angle          = " & swSketchHatch.Angle * 57.3 & " degrees"
            Debug.Print "  Color          = " & swSketchHatch.Color
            Debug.Print "  ID             = [" & swSketchHatch.GetID(0) & ", " & swSketchHatch.GetID(1) & "]"
            Debug.Print "  Layer          = " & swSketchHatch.Layer
            Debug.Print "  LayerOverride  = " & swSketchHatch.LayerOverride
            Debug.Print "  Pattern        = " + swSketchHatch.Pattern
            Debug.Print "  Scale          = " & swSketchHatch.Scale2
            Debug.Print "  SolidFill      = " & swSketchHatch.SolidFill
            Debug.Print "  -----------------------"
        Next i
    End If
```

```
End Sub
```
