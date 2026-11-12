---
title: "Create Linear Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Linear_Pattern_Example_VBNET.htm"
---

# Create Linear Pattern Example (VB.NET)

This example shows how to create a linear pattern.

```vb
 '-------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this example into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a document.
 ' 6. Click Start Debugging.
 '
 ' Postconditions:
 ' 1. Draws a Circle.
 ' 2. Draws a 2D PolyLine.
 ' 3. Creates a linear pattern using the Circle and 2D PolyLine
 '    entities.
 ' 4. Zooms the drawing to fit.
 ' 5. Examine the drawing.
 '------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms

 Module Module1

     Sub Main()

         'Connect to DraftSight application
         Dim dsApp = GetObject(, "DraftSight.Application")
         dsApp.AbortRunningCommand() '  abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get Sketch Manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Draw a Circle
         Dim centerPoint As Double() = New Double() {5, 5, 0}
         Dim radius As Double = 3
         Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerPoint(0), centerPoint(1), centerPoint(2), radius)

         'Draw a 2D PolyLine
         Dim coordinatesArray As Double() = New Double() {10, 4, 10, 6, 14, 6, _
          14, 4}
         Dim closed As Boolean = True
         Dim dsPolyLine As PolyLine = dsSketchMgr.InsertPolyline2D(coordinatesArray, closed)

         'Linear pattern parameters
         Dim numberElementsOnVerticalAxis As Integer = 4
         Dim numberElementsOnHorizontalAxis As Integer = 5
         Dim spacingOnVerticalAxis As Double = 20
         Dim spacingOnHorizontalAxis As Double = 40
         Dim patternAngle As Double = Math.PI / 4 'In radians

         'Prepare list of entity types
         Dim dsEntityTypes As Integer() = New Integer() {CInt(dsObjectType_e.dsCircleType), CInt(dsObjectType_e.dsPolyLineType)}

         'Prepare list of entities
         Dim dsEntities As DispatchWrapper() = New DispatchWrapper() {New DispatchWrapper(dsCircle), New DispatchWrapper(dsPolyLine)}

         'Create linear pattern
         dsSketchMgr.PatternLinear(numberElementsOnVerticalAxis, numberElementsOnHorizontalAxis, spacingOnVerticalAxis, spacingOnHorizontalAxis, patternAngle, dsEntityTypes, _
          dsEntities)

         'Zoom to fit
         dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
     End Sub
 End  Module
```
