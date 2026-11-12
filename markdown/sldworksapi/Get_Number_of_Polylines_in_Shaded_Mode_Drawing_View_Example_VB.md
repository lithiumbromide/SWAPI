---
title: "Get Number of Polylines in Shaded Mode Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm"
---

# Get Number of Polylines in Shaded Mode Drawing View Example (VBA)

This example shows how to get the number of polylines in a drawing view displayed in Shaded and Wireframe modes.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Change Drawing View4 to Shaded mode (click
'    Drawing View4 in the drawing, click Shaded
'    in Display Style in the PropertyManager page, and
'    click OK.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of polylines in Shaded mode.
' 2. Switches mode to Wireframe and gets number of polylines
'    in Wireframe mode.
' 3. Switches mode back to Shaded.
' 4. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawDoc As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim retval As Long
Dim boolstatus As Boolean
Dim nCountShaded As Long
Dim nCount_WireFrame As Long
Dim retval2 As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swDrawDoc = swApp.ActiveDoc
```

```
    swDrawDoc.ClearSelection2 True
```

```
   ' Select Drawing View4
    boolstatus = swDrawDoc.Extension.SelectByID2("Drawing View4", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swView = swDrawDoc.SelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Get display mode for Drawing View4
    Set swView = swDrawDoc.ActiveDrawingView
    retval = swView.GetDisplayMode2
    Debug.Print "Drawing view in what display mode"
    Debug.Print "  swDisplayMode_e: swWIREFRAME = 0, swHIDDEN_GREYED = 1, swHIDDEN = 2, swSHADED = 3: " & retval
```

```
    ' Get number of polylines in drawing view in Shaded mode
    swView.GetPolyLineCount5 swCrossHatchFilter_e.swCrossHatchExclude, nCountShaded
    Debug.Print "Number of polylines in drawing view in Shaded mode = " & nCountShaded
```

```
    ' Switch to Wireframe mode because you can get number of polylines in Wireframe mode
    retval2 = swView.SetDisplayMode3(False, swDisplayMode_e.swWIREFRAME, False, False)
    Debug.Print "Display mode changed to Wireframe: " & retval2
```

```
    ' Get number of polylines in Wireframe mode
    swView.GetPolyLineCount5 swCrossHatchFilter_e.swCrossHatchExclude, nCount_WireFrame
    Debug.Print "Number of polylines in WireFrame = " & nCount_WireFrame
```

```
    ' Switch back to Shaded mode
    retval2 = swView.SetDisplayMode3(False, swDisplayMode_e.swSHADED, False, False)
    Debug.Print "Display mode changed back to Shaded: " & retval2
```

```
    swDrawDoc.ClearSelection2 True
```

```
End Sub
```
