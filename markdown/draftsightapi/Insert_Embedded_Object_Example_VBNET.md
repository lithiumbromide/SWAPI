---
title: "Insert Embedded Object Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Embedded_Object_Example_VBNET.htm"
---

# Insert Embedded Object Example (VB.NET)

This example shows how to embed a file object in a DraftSight drawing.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this example into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Place the document to embed in the project assembly folder.
 ' 6. Right-click the project and select Add > Existing Item.
 ' 7. Select the document to embed and click Add.
 ' 8. Right-click the file in Solution Explorer and select Properties.
 ' 9. For the Copy to Output property, select Copy Always.
 '10. Modify the document name referenced in the code.
 '11. Start DraftSight and open a drawing document.
 '12. Start debugging the project.
 '
 ' Postconditions:
 ' 1. The file object is embedded in the drawing.
 ' 2. Inspect the Immediate window for its position and parameters.
 '----------------------------------------------------------------
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Windows.Forms
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics
 Imports System.IO
 Imports System.Reflection

 Module Module1

     Sub Main()
         'Connect to DraftSight application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get sketch manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Embedded object parameters
         Dim filePath As String = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "SampleDoc.docx")
         Dim link As Boolean = True
         Dim displayAsIcon As Boolean = False

         'Insert embedded object
         Dim dsEmbeddedObject As EmbeddedObject = dsSketchMgr.InsertEmbeddedObjectFromFile(filePath, link, displayAsIcon)
         If dsEmbeddedObject IsNot Nothing Then
             PrintParameters(dsEmbeddedObject)
         Else
             MessageBox.Show("Embedded object entity was not added to the current drawing.")
         End If
     End Sub

     Sub PrintParameters(ByVal dsEmbeddedObject As EmbeddedObject)
         Debug.Print(Environment.NewLine   "Embedded object parameters...")

         'Print common entity parameters
         Debug.Print("Handle = " & Convert.ToString(dsEmbeddedObject.Handle))
         Debug.Print("Color = " & dsEmbeddedObject.Color.GetNamedColor())
         Debug.Print("Erased = " & Convert.ToString(dsEmbeddedObject.Erased))
         Debug.Print("Layer = " & Convert.ToString(dsEmbeddedObject.Layer))
         Debug.Print("LineScale = " & Convert.ToString(dsEmbeddedObject.LineScale))
         Debug.Print("LineStyle = " & Convert.ToString(dsEmbeddedObject.LineStyle))
         Debug.Print("LineWeight = " & Convert.ToString(dsEmbeddedObject.LineWeight))
         Debug.Print("Visible = " & Convert.ToString(dsEmbeddedObject.Visible))

         Dim x1 As Double, y1 As  Double, z1  As  Double
         Dim x2 As Double, y2 As  Double, z2  As  Double
         dsEmbeddedObject.GetBoundingBox(x1, y1, z1, x2, y2, z2)
         Debug.Print(String.Format("BoundingBox: ({0},{1},{2}) and ({3},{4},{5})", x1, y1, z1, x2, y2, _
          z2))

         'Print embedded object parameters
         Debug.Print("Height = " & Convert.ToString(dsEmbeddedObject.Height))
         Debug.Print("Width = " & Convert.ToString(dsEmbeddedObject.Width))
         Debug.Print("PrintQuality = " & Convert.ToString(dsEmbeddedObject.PrintQuality))
         Debug.Print("LinkPath = " & dsEmbeddedObject.GetLinkPath())
         Debug.Print("SourceApplication = " & dsEmbeddedObject.GetSourceApplication())
         Debug.Print("Type = " & dsEmbeddedObject.[GetType]())

         'Get position of embedded object
         Dim x As  Double, y  As  Double, z  As  Double
         dsEmbeddedObject.GetPosition(x, y, z)
         Debug.Print(String.Format("Position = ({0},{1},{2})", x, y, z))
     End Sub

     Function ConnectToDraftSight() As DraftSight.Interop.dsAutomation.Application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application =  Nothing

         Try
             'Connect to DraftSight
             dsApp =  DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
         Catch ex As Exception
             MessageBox.Show("Failed to connect to DraftSight. Cause: " & ex.Message)
             dsApp = Nothing
         End Try

         Return dsApp
     End Function
 End Module
```
