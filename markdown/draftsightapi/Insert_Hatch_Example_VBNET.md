---
title: "Insert Hatch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Hatch_Example_VBNET.htm"
---

# Insert Hatch Example (VB.NET)

## Insert Hatch Example Example (VB.NET)

This example shows how to insert a Hatch in a drawing document.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a drawing document.
 ' 6. Start debugging the project.
 '
 ' Postconditions: A Hatch is inserted in the drawing document
 ' and zoomed to fit.
 '----------------------------------------------------------------

 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1

     Dim dsApp As DraftSight.Interop.dsAutomation.Application

     Sub Main()
         'Connect to DraftSight application
         dsApp = GetObject(,  "DraftSight.Application")
         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

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

         'Hatch parameters
         Dim boundaryPointCountArray As Integer() = New  Integer() {4}
         Dim boundaryPoints As Double() = New  Double() {0, 0, 2, 0, 2, 2, 0, 2}
         Dim patternName As String = "ANSI31"
         Dim patternScale As Double = 1.0
         Dim patternAngle As Double = Math.PI / 4 ' In radians

         'Insert Hatch
         Dim dsHatch As Hatch = dsSketchMgr.InsertHatchByBoundary(boundaryPointCountArray, boundaryPoints, patternName, patternScale, patternAngle)
         If dsHatch IsNot Nothing Then
             'Change color of Hatch
             Dim dsColor As Color = dsHatch.Color
             dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Green)
             dsHatch.Color = dsColor

             'Zoom to fit
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
         Else
             MessageBox.Show("Hatch entity was not added to the current drawing.")
         End If
     End Sub

 End  Module
```
