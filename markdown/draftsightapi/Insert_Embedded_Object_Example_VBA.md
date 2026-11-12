---
title: "Insert Embedded Object Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Embedded_Object_Example_VBA.htm"
---

# Insert Embedded Object Example (VBA)

This example shows how to embed a file object in a DraftSight drawing.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Modify the document name referenced in the code.
 ' 5. Start DraftSight and open a drawing document.
 ' 6. Start debugging the project.
 '
 ' Postconditions:
 ' 1. The file object is embedded in the drawing.
 ' 2. Inspect the Immediate window for its position and parameters.
 '----------------------------------------------------------------
 Dim dsApp As DraftSight.Application
 Option Explicit
 Sub Main()
     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")
     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand
    'Get active document
     Dim dsDoc As DraftSight.Document
     Set dsDoc = dsApp.GetActiveDocument()
     If dsDoc Is Nothing Then
         MsgBox ("There are no open documents in DraftSight.")
         Return
     End If
    'Get model space
     Dim dsModel As DraftSight.Model
     Set dsModel = dsDoc.GetModel()
    'Get sketch manager
     Dim dsSketchMgr As DraftSight.SketchManager
     Set dsSketchMgr = dsModel.GetSketchManager()
    'Embedded object parameters
     Dim filePath As String
     filePath = "full_path\SampleDoc.docx"
     Dim link As Boolean
     link = True
     Dim displayAsIcon As Boolean
     displayAsIcon = False
    'Insert embedded object
     Dim dsEmbeddedObject As DraftSight.EmbeddedObject
     Set dsEmbeddedObject = dsSketchMgr.InsertEmbeddedObjectFromFile(filePath, link, displayAsIcon)
     If Not (dsEmbeddedObject Is Nothing) Then
         Call PrintParameters(dsEmbeddedObject)
     Else
         MsgBox ("Embedded object entity was not added to the current drawing.")
     End If
 End Sub
Sub PrintParameters(dsEmbeddedObject As EmbeddedObject)
     Debug.Print ("Embedded object parameters...")
    'Print common entity parameters
     Debug.Print ("Handle = " & dsEmbeddedObject.Handle)
     Debug.Print ("Color = " & dsEmbeddedObject.Color.GetNamedColor())
     Debug.Print ("Erased = " & dsEmbeddedObject.Erased)
     Debug.Print ("Layer = " & dsEmbeddedObject.Layer)
     Debug.Print ("LineScale = " & dsEmbeddedObject.LineScale)
     Debug.Print ("LineStyle = " & dsEmbeddedObject.LineStyle)
     Debug.Print ("LineWeight = " & dsEmbeddedObject.LineWeight)
     Debug.Print ("Visible = " & dsEmbeddedObject.Visible)
    Dim x1 As Double, y1 As Double, z1 As Double
     Dim x2 As Double, y2 As Double, z2 As Double
     dsEmbeddedObject.GetBoundingBox x1, y1, z1, x2, y2, z2
     Debug.Print ("BoundingBox: " & x1 & ", " & y1 & ", " & z1 & " and " & ", " & x2 & ", " & y2 & ", " & z2)
    'Print embedded object parameters
     Debug.Print ("Height = " & dsEmbeddedObject.Height)
     Debug.Print ("Width = " & dsEmbeddedObject.Width)
     Debug.Print ("PrintQuality = " & dsEmbeddedObject.PrintQuality)
     Debug.Print ("LinkPath = " & dsEmbeddedObject.GetLinkPath())
     Debug.Print ("SourceApplication = " & dsEmbeddedObject.GetSourceApplication())
     Debug.Print ("Type:  " & dsEmbeddedObject.[GetType]())
    'Get position of embedded object
     Dim x As Double, y As Double, z As Double
     dsEmbeddedObject.GetPosition x, y, z
     Debug.Print ("Position: " & x & ", " & y & ", " & z)
 End Sub
```
