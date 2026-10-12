---
title: "Insert Hatch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hatch_Example_VB.htm"
---

# Insert Hatch Example (VBA)

This example shows how to insert a hatch on a closed sketch in a drawing. The following image demonstrates the example.

```vb
'------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing containing a closed sketch similar to the
 '    sketch shown.
 ' 2. Select an arc.
 ' 3. Change the name of the arc in this code to match name of
 '    of the arc selected in step 2 (e.g., record selecting the
 '    arc, save the recording to a new macro, open and inspect
 '    that macro, and make note of the name of the selected arc).
 '
 ' Postconditions:
 ' 1. Inserts and scales the hatch.
 ' 2. Examine the drawing.
 '------------------------------------------------------------
 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim SelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean

 Sub main()
```

```vb
Set swApp = Application.SldWorks

 Set Part = swApp.ActiveDoc
 Set SelMgr = Part.SelectionManager
 boolstatus = Part.Extension.SelectByID2("Arc29", "SKETCHSEGMENT", 0.08421725979537, 0.08635799134766, 0, False, 0, Nothing, 0)

 Dim selSkSeg As SldWorks.SketchSegment
 Dim selSk As SldWorks.Sketch
 Set selSkSeg = SelMgr.GetSelectedObject6(1, -1)
Set selSk = selSkSeg.GetSketch

 Part.InsertHatchedFace

 Dim hatchArr As Variant
 Dim vobj As Variant
 Dim skHatch As SldWorks.SketchHatch

 hatchArr = selSk.GetSketchHatches
 For Each vobj In hatchArr
     Set skHatch = vobj
     skHatch.Scale2 = 4
 Next vobj
```

```vb
 End Sub
```
