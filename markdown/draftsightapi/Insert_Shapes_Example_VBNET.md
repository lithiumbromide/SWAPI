---
title: "Insert Shapes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Shapes_Example_VBNET.htm"
---

# Insert Shapes Example (VB.NET)

This example shows how to load a shape file and insert the shapes in the loaded shape file into a drawing.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add references to System and System.Windows.Forms.
' 5. Start DraftSight and open a document.
' 6. Start debugging the project.
'
' Postconditions:
' 1. Gets the Shape Manager.
' 2. Loads a shape file.
' 3. Gets the shapes in the loaded shape file.
' 4. Inserts the shapes, with an obliquing angle of 30, in the drawing.
' 5. Examine the drawing.
'----------------------------------------------------------------

Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        If dsApp Is Nothing Then
            Return
        End If

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get the Shape Manager
        Dim dsShapeMgr As ShapeManager = dsDoc.GetShapeManager()

        'Load shape file LTypeShp.shx
        Dim dsSysFile As SystemFiles = dsApp.GetSystemFiles()
        Dim FontsPathObj As Object() = DirectCast(dsSysFile.FontsPaths, Object())
        Dim fontPath As String = ""
        If FontsPathObj.Length > 0 Then
            fontPath = FontsPathObj(0).ToString()
        End If

        Dim shapeFileName As String = System.IO.Path.Combine(fontPath, "LTypeShp.shx")

        dsShapeMgr.Load(shapeFileName)

        'Get shapes
        Dim shapesStrList As Object() = DirectCast(dsShapeMgr.GetAvailableShapes(), Object())
        Dim shapesCount As Integer = shapesStrList.Length

        'Get Sketch Manager
        Dim dsSketchMgr As SketchManager = dsDoc.GetModel().GetSketchManager()

        'Insert shapes
        Dim PositionX As Double = 0.0, PositionY As Double = 0.0, PositionZ As Double = 0.0
        For i As Integer = 0 To shapesCount - 1
            Dim dsShape As Shape = dsSketchMgr.InsertShape(shapesStrList(i).ToString(), PositionX, PositionY, PositionZ, 1, 0.0)

            'Change obliquing property
            dsShape.Obliquing = 30 * Math.PI / 180

            Dim X1 As Double, Y1 As Double, Z1 As Double, X2 As Double, Y2 As Double, Z2 As Double
            dsShape.GetBoundingBox(X1, Y1, Z1, X2, Y2, Z2)

            PositionX += (X2 - X1) + 5
        Next
    End Sub

End Module
```
