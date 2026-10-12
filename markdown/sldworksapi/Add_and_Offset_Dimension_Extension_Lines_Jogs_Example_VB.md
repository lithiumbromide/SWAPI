---
title: "Add and Offset Dimension Extension Lines Jogs (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm"
---

# Add and Offset Dimension Extension Lines Jogs (VBA)

This example shows how to jog the selected dimension's extension lines and to then offset the jogs.

```
'-------------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Selects a linear dimension.
' 2. Jogs the selected dimension's extension lines.
' 3. Offsets the jogs.
' 4. Select the highlighted dimension in the drawing.
' 5. Click anywhere outside the drawing view in the drawing
'    and examine the extension lines of the dimension.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDim As SldWorks.DisplayDimension
Dim swModelView As SldWorks.ModelView
Dim boolstatus As Boolean
Dim index As Integer
Dim jogged As Boolean
Dim offset1 As Double, offset2 As Double, offset1to2 As Double
Dim rect As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelView = swModel.ActiveView
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    boolstatus = swModel.ActivateView("Drawing View1")
    boolstatus = swModelDocExt.SelectByID2("RD9@Drawing View1", "DIMENSION", 0.214177376160146, 0.307386295566502, 0, False, 0, Nothing, 0)
    Set swDisplayDim = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Add jogs to the dimension's extension lines
    boolstatus = swModelDocExt.JogDimension(True, 0)
    boolstatus = swModelDocExt.JogDimension(True, 1)
```

```
    ' Offset the jogs
    index = 0
    boolstatus = swDisplayDim.GetJogParameters(index, jogged, offset1, offset2, offset1to2)
    offset1 = offset1 + offset1 * 0.1
    offset2 = offset2 + offset2 * 0.2
    offset1to2 = offset1to2 + offset1 * 0.2
    boolstatus = swDisplayDim.SetJogParameters(index, jogged, offset1, offset2, offset1to2)
```

```
    index = 1
    boolstatus = swDisplayDim.GetJogParameters(index, jogged, offset1, offset2, offset1to2)
    offset1 = offset1 + offset1 * 0.1
    offset2 = offset2 + offset2 * 0.2
    offset1to2 = offset1to2 + offset1 * 0.2
    boolstatus = swDisplayDim.SetJogParameters(index, jogged, offset1, offset2, offset1to2)
```

```
    swModelView.GraphicsRedraw ((rect))
```

```
End Sub
```
