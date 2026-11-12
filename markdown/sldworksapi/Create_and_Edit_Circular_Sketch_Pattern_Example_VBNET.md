---
title: "Create and Edit Circular Sketch Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm"
---

# Create and Edit Circular Sketch Pattern Example (VB.NET)

This example shows how to create and edit a circular sketch pattern.

'------------------------------------------------------------
' Preconditions: Verify that the specified part document template
' exists.
'
' Postconditions:
' 1. Opens a new part document and creates a sketch.
' 2. Inserts a circular sketch pattern of four instances.
' 3. Closes the sketch.
' 4. Opens the circular sketch pattern for editing.
' 5. Deletes an instance of circular sketch pattern, leaving
' three instances.
' 6. Examine the graphics area.
'------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

```vb
Partial Class SolidWorksMacro
    Public Sub main()
        Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swSketchMgr As SketchManager
         Dim swSketchSegment As SketchSegment
         Dim vSkLines As Object
         Dim boolstatus As Boolean
         Dim longstatus As Long

         ' Reset the counts for untitled documents for this macro
         swApp.ResetUntitledCount(0, 0, 0)

         ' Create and activate a part document
         swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2008\templates\Part.prtdot", 0, 0, 0)
         swApp.ActivateDoc2("Part1", False, longstatus)
         swModel = swApp.ActiveDoc

         swSketchMgr = swModel.SketchManager
         swModelDocExt = swModel.Extension

         ' Sketch a circle
         swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.045549, 0.013926, 0.0#)

         ' Clear any selections and change
         ' the view orientation to Front
         swModel.ClearSelection2(True)
         swModel.ShowNamedView2("*Front", 1)

         ' Create a rectangle
         vSkLines = swSketchMgr.CreateCornerRectangle(-0.005867589431389, 0.03694408160504, 0, 0.004563680668858, 0.02673012963188, 0)

         ' Create a circular sketch pattern
         ' using the rectangle
         boolstatus = swSketchMgr.CreateCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 4, 1.570796326795, True, "", True, True, True)
         swModel.ClearSelection2(True)

         ' Close the sketch and rebuild
         swSketchMgr.InsertSketch(True)

         ' Select an entity in the circular sketch pattern
         ' and open the circular sketch pattern to edit it
         boolstatus = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.002390499397973, 0.03694408160504, 0, False, 0, Nothing, 0)
         swModel.EditSketch()

         ' Delete an instance of the circular
         ' sketch pattern and close the sketch
         boolstatus = swSketchMgr.EditCircularSketchStepAndRepeat(0.03184378021964, 4.732863934409, 3, 1.570796326795, True, "", True, True, True, "Line2_Line1_Line4_Line3_")
         swModel.ClearSelection2(True)
         swSketchMgr.InsertSketch(True)

     End Sub

     ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
