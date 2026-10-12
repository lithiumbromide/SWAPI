---
title: "Set and Get Maximum Extension Line Length Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_and_Get_Maximum_Extension_Line_Length_Example_VB.htm"
---

# Set and Get Maximum Extension Line Length Example (VBA)

This example shows how to set and get the maximum extension line length for a display dimension.

```
'--------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\lesson2\tutor1.sldprt.
' 2. Right-click Annotations and click Show Feature Dimensions.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Selects a dimension.
' 2. Sets the maximum length for the selected dimension's
'    witness extension lines to the specified value.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDim As SldWorks.DisplayDimension
Dim swModelView As SldWorks.ModelView
Dim selType As Long
Dim maxLineLength As Double
Dim status As Boolean
Dim rect As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swModelDocExt = swModelDoc.Extension
    Set swSelMgr = swModelDoc.SelectionManager
    status = swModelDocExt.SelectByID2("D2@Sketch2@tutor1.SLDPRT", "DIMENSION", 2.29248368227093E-03, 6.41116623573457E-02, 5.51580671328052E-02, False, 0, Nothing, 0)
    selType = swSelMgr.GetSelectedObjectType3(1, -1)
    If selType = swSelDIMENSIONS Then
      Set swDisplayDim = swSelMgr.GetSelectedObject6(1, -1)
      swDisplayDim.MaxWitnessLineLength = 130
   End If
   maxLineLength = swDisplayDim.MaxWitnessLineLength
   Debug.Print "New maximum witness extension line length: " & maxLineLength
```

```
   Set swModelView = swModelDoc.ActiveView
   Set rect = Nothing
   swModelView.GraphicsRedraw (rect)
```

```
End Sub
```
