---
title: "Create and Attach HyperLink Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Attach_Hyperlink_Example_VBNET.htm"
---

# Create and Attach HyperLink Example (VB.NET)

This example shows how to create and attach a HyperLink to a Circle.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this example into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a drawing document.
 ' 6. Click Start Debugging.
 '
 ' Postconditions:
 ' 1. A Circle is constructed in the drawing document.
 ' 2. A HyperLink is created and attached to the Circle.
 ' 3. In DraftSight, put the cursor on the Circle to see the
 '    the hyperlink and Ctrl+click to open DraftSight's website.
 '----------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1

     Sub Main()

         Dim dsDoc As Document
         Dim dsModel As Model
         Dim dsSketchManager As SketchManager
         Dim dsCircle As Circle
         Dim centerX, centerY, centerZ, radius As Double

         'Connect to DraftSight
         Dim dsApp = GetObject(, "DraftSight.Application")
         dsApp.AbortRunningCommand() '  abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         dsDoc = dsApp.GetActiveDocument()
         If Not dsDoc Is  Nothing  Then

             'Get model space
             dsModel = dsDoc.GetModel()

             'Get Sketch Manager
             dsSketchManager = dsModel.GetSketchManager()

             'Circle parameters
             centerX = 1.0#
             centerY = 2.0#
             centerZ = 0.0#
             radius = 5.0#

             'Construct a Circle
             dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)

             'Create and attach HyperLink to Circle
             Dim startCornerX As Double
             startCornerX = 0.0#
             Dim startCornerY As Double
             startCornerY = 0.0#
             Dim startCornerZ As Double
             startCornerZ = 0.0#
             Dim oppositeCornerX As Double
             startCornerX = 0.0#
             Dim oppositeCornerY As Double
             startCornerY = 0.0#
             Dim oppositeCornerZ As Double
             startCornerZ = 0.0#
             Dim hyperLinkAddress As String
             hyperLinkAddress =  "http://www.3ds.com/products/draftsight/free-cad-software/"
             Dim description As String
             description =  "DraftSight's website"
             Dim ds3DPolyLine As PolyLine3D
             Dim dsHyperLink As HyperLink

             dsHyperLink = dsSketchManager.AttachLinkToArea(startCornerX, startCornerY, startCornerZ, oppositeCornerX, oppositeCornerY, oppositeCornerZ, hyperLinkAddress, description, ds3DPolyLine)
             dsCircle.SetHyperLink(dsHyperLink)

         Else

             MsgBox("There are no open documents in DraftSight.")

         End If
     End Sub

 End Module
```
