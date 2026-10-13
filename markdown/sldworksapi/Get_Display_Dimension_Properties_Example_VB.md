---
title: "Get Display Dimension Properties(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Display_Dimension_Properties_Example_VB.htm"
---

# Get Display Dimension Properties(VBA)

## Get Display Dimension Properties Examples (VBA)

This example shows how to get the display dimension properties for a dimension in a drawing view.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through the display dimensions in DrawingView1.
' 2. If the display dimension's name is RD19, then
'    gets its properties.
' 3. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not make changes.
'-------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swDrawingView1 As SldWorks.View
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim swDimension As SldWorks.Dimension
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawingDoc = swModel
    'First view is sheet
    Set swView = swDrawingDoc.GetFirstView
    'So, get next view, which is DrawingView1
    Set swDrawingView1 = swView.GetNextView
```

```
    'Iterate through the display dimensions in DrawingView1
    Set swDisplayDimension = swDrawingView1.GetFirstDisplayDimension()
    While Not swDisplayDimension Is Nothing
     'Check if display dimension is RD19
     Set swDimension = swDisplayDimension.GetDimension
     If swDimension.Name = "RD19" Then
      'Get the properties of display dimension RD19
      Debug.Print "Display dimension RD19's properties:"
      Debug.Print " Arrow side: " & swDisplayDimension.ArrowSide
      Debug.Print " Broken leader: " & swDisplayDimension.BrokenLeader
      Debug.Print " Leader visibility: "; swDisplayDimension.LeaderVisibility
      Debug.Print " Show dimension value: " & swDisplayDimension.ShowDimensionValue
      Debug.Print " Show parenthesis: " & swDisplayDimension.ShowParenthesis
      Debug.Print " Smart witness: " & swDisplayDimension.SmartWitness
      Debug.Print " Witness visibility: " & swDisplayDimension.WitnessVisibility
     End If
     Set swDisplayDimension = swDisplayDimension.GetNext()
    ' Get next display dimension
    Wend
```

```
End Sub
```
