---
title: "Get Parabolas in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parabolas_in_Sketch_Example_VB.htm"
---

# Get Parabolas in Sketch Example (VBA)

This example shows how to get information about all of the parabolas in a sketch.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part that contains one or more parabolas.
' 2. Edit the sketch that contains the parabolas.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim swFeat              As SldWorks.feature
    Dim swSketch            As SldWorks.sketch
    Dim vParabArr           As Variant
    Dim i                   As Long
    Dim bRet                As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSketch = swModel.GetActiveSketch2
    Set swFeat = swSketch
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name

    vParabArr = swSketch.GetParabolas2
    For i = 0 To swSketch.GetParabolaCount - 1
        Debug.Print "    Parabola[" & i & "]"
        Debug.Print "      Color           = " & vParabArr(18 * i + 0)
        Debug.Print "      Linetype         = " & vParabArr(18 * i + 1)

        ' Drawings only
        Debug.Print "      Font             = " & vParabArr(18 * i + 2)
        Debug.Print "      Width            = " & vParabArr(18 * i + 3)
        Debug.Print "      LayerID          = " & vParabArr(18 * i + 4)
        Debug.Print "      Layer Override   = " & vParabArr(18 * i + 5)

        Debug.Print "      Start Pt         = (" & vParabArr(18 * i + 6) * 1000# & ", " & vParabArr(18 * i + 7) * 1000# & ", " & vParabArr(18 * i + 8) * 1000# & ") mm"
        Debug.Print "      End   Pt         = (" & vParabArr(18 * i + 9) * 1000# & ", " & vParabArr(18 * i + 10) * 1000# & ", " & vParabArr(18 * i + 11) * 1000# & ") mm"
        Debug.Print "      Focus Pt         = (" & vParabArr(18 * i + 12) * 1000# & ", " & vParabArr(18 * i + 13) * 1000# & ", " & vParabArr(18 * i + 14) * 1000# & ") mm"
        Debug.Print "      Apex  Pt         = (" & vParabArr(18 * i + 15) * 1000# & ", " & vParabArr(18 * i + 16) * 1000# & ", " & vParabArr(18 * i + 17) * 1000# & ") mm"
    Next i
End Sub
```
