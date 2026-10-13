---
title: "Get and Set Dimension Extension Lines Gaps (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Dimension_Extension_Lines_Gaps_Example_VB.htm"
---

# Get and Set Dimension Extension Lines Gaps (VBA)

This example shows how to get and set the gaps for the extension lines of a display dimension.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\replaceview.slddrw.
' 2. Select a vertical edge in the model in DrawingView1.
'
' Postconditions:
' 1. Modifies the selected edge's dimension's line
'    extension gaps to the specified value.
' 2. Examine the drawing.
'
' NOTE: Because this drawing is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDisplayDim As SldWorks.DisplayDimension
retBool as Boolean
Dim UseDoc As Boolean
Dim Gap As Double
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Programmatically add a dimension to the selected edge
    Set swDisplayDim = swModel.AddDimension2(0.07991695284535, 0.1237274983129, 0)
```

```
    Debug.Print "Dimension Extension Lines"
    Debug.Print ""
```

```
    ' Get document default value for extension lines' gaps
    Debug.Print "Value of document default gap:  " & swModel.GetUserPreferenceDoubleValue(swDetailingWitnessLineGap)
    Debug.Print " "
```

```
    ' Get a dimension's extension line's gap
    retBool = swDisplayDim.GetWitnessLineGap(1, UseDoc, Gap)
    Debug.Print "Get Gap Operation:"
    Debug.Print "  Use document default for gap: " & UseDoc
    Debug.Print "  Gap value in system units:    " & Gap
    Debug.Print " "
```

```
    ' Set the dimension's extension line's gaps
    Gap = 0.005
    retBool = swDisplayDim.SetWitnessLineGap(0, False, Gap)
    retBool = swDisplayDim.SetWitnessLineGap(1, False, Gap)
    Debug.Print "Set Gap Operation: "
    Debug.Print "  Gap value in system units:    " & Gap
    Debug.Print " "
```

```
    ' Get the dimension's extension gap again
    retBool = swDisplayDim.GetWitnessLineGap(1, UseDoc, Gap)
    Debug.Print "Get Gap Operation:"
    Debug.Print "  Use document default for gap: " & UseDoc
    Debug.Print "  Gap value in system units:    " & Gap
    Debug.Print " "
```

```
    swModel.GraphicsRedraw
```

```
End Sub
```
