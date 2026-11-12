---
title: "Divide Surface into 3D Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Divide_Surface_into_3D_Sketches_Example_VB.htm"
---

# Divide Surface into 3D Sketches Example (VBA)

This example:

- Shows how to divide the selected face into 3D sketches.
- Uses IModelDoc2::SketchConvertIsoCurves to extract ISO-parametric (UV) curves from a face and creates a set of evenly spaced sections in the U and V directions.

```
'-------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Generates 3D sketches.
' 2. Evenly divides the 3D sketches on the selected
'    face in the UV directions.
' 3. Examine the graphics area, FeatureManager design
'    tree, and the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const nNum_U As Long = 3
    Const nNum_V As Long = 4
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    Debug.Print "  U percent ratios:"
    For i = 0 To nNum_U
        ' Start from 0%, finish at 100%
        Debug.Print "    " & i * 100# / nNum_U & " %"
        swModel.SketchConvertIsoCurves i * 100# / nNum_U, False, True, True
    Next i
```

```
    Debug.Print "  V percent ratios:"
```

```
    For i = 0 To nNum_V
        ' Start from 0%, finish at 100%
        Debug.Print "    " & i * 100# / nNum_V & " %"
        swModel.SketchConvertIsoCurves i * 100# / nNum_V, True, True, True
    Next i
```

```
End Sub
```
