---
title: "Get Tolerance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tolerance_Example_VB.htm"
---

# Get Tolerance Example (VBA)

This example shows how to get the tolerance of a model.

```vb
'---------------------------------------------
Option Explicit
Public Enum swTolerances_e
    swBSCurveOutputTol = 0
    swBSCurveNonRationalOutputTol = 1
    swUVCurveOutputTol = 2
    swSurfChordTessellationTol = 3
    swSurfAngularTessellationTol = 4
    swCurveChordTessellationTol = 5
End Enum
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModeler               As SldWorks.Modeler

    Set swApp = Application.SldWorks
    Set swModeler = swApp.GetModeler

    Debug.Print "Modeler Tolerances:"
    Debug.Print "  BSCurveOutputTol             = " & swModeler.GetToleranceValue(swBSCurveOutputTol) * 1000# & " mm"
    Debug.Print "  BSCurveNonRationalOutputTol  = " & swModeler.GetToleranceValue(swBSCurveNonRationalOutputTol) * 1000# & " mm"
    Debug.Print "  UVCurveOutputTol             = " & swModeler.GetToleranceValue(swUVCurveOutputTol) * 1000# & " mm"
    Debug.Print "  SurfChordTessellationTol     = " & swModeler.GetToleranceValue(swSurfChordTessellationTol) * 1000# & " mm"
    Debug.Print "  SurfAngularTessellationTol   = " & swModeler.GetToleranceValue(swSurfAngularTessellationTol) * 1000# & " mm"
    Debug.Print "  CurveChordTessellationTol    = " & swModeler.GetToleranceValue(swCurveChordTessellationTol) * 1000# & " mm"
End Sub
'---------------------------------------------
```
