---
title: "Set Table Anchors in Sheet Formats Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Table_Anchors_Example_VB.htm"
---

# Set Table Anchors in Sheet Formats Example (VBA)

This example shows how to set a hole table anchor in a sheet format of a drawing.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified drawing to open exists.
 ' 2. Open and Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the drawing.
 ' 2. At Stop, examine the position of the hole table in the drawing.
 ' 3. Press F5.
 ' 4. Edits the sheet format.
 ' 5. Creates a point.
 ' 6. Sets the position of the hole table's anchor at the new point.
 ' 7. Examine the new position of the hole table
 '    and the Immediate window.
 '
 ' NOTE: If prompted, do not save changes when closing the drawing.
 '----------------------------------------------------------------------------
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swDrw As DrawingDoc
 Dim swSheet As Sheet
 Dim swModel As ModelDoc2
 Dim swSkPoint As SketchPoint
 Dim oldTableAnchor As TableAnchor
 Dim newTableAnchor As TableAnchor
 Dim vPosition As Variant
 Dim filename As String
 Dim errors As Long
 Dim warnings As Long
Sub main()

    Set swApp = Application.SldWorks
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SimpleHole.slddrw"
     Set swDrw = swApp.OpenDoc6(filename, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)

    If swDrw Is Nothing Then Exit Sub

    Stop
    Set swSheet = swDrw.GetCurrentSheet()
     Set swModel = swDrw

    swModel.Extension.SelectByID2 swSheet.GetName(), "SHEET", 0, 0, 0, False, 0, Nothing, 0

    swDrw.EditTemplate
     swModel.EditSketch

    Set swSkPoint = swModel.SketchManager.CreatePoint(0.2, 0.07, 0)
     swSkPoint.Select4 False, Nothing

    ' If an anchor for the hole table already exists, move it to the selected sketch point
     Set oldTableAnchor = swSheet.TableAnchor(swTableAnnotation_HoleChart)
     Set newTableAnchor = swSheet.SetAsTableAnchor(swTableAnnotation_HoleChart)

    If Not newTableAnchor Is Nothing Then

        vPosition = newTableAnchor.Position
         Debug.Print "Table Anchor at (" & vPosition(0) & ", " & vPosition(1) & ")"

    End If

    swDrw.EditSheet
     swModel.EditSketch
     swModel.ForceRebuild3 True

End Sub
```
