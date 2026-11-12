---
title: "Get and Set Hatch Pattern Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Hatch_Pattern_Data_Example_VBNET.htm"
---

# Get and Set Hatch Pattern Data Example (VB.NET)

This example shows how to get and set Hatch pattern data.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1.  Create a VB.NET Windows console project.
 ' 2.  Copy and paste this example into the VB.NET IDE.
 ' 3.  Add a reference to:
 '     install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4.  Add references to System and System.Windows.Forms.
 ' 5.  Make sure that C:\ProgramData\Dassault Systemes\DraftSight\Examples
 '     exists.
 ' 6.  Copy all .dxf and .dwg files in this folder to a backup folder.
 ' 7.  Set all .dxf and .dwg files in
 '     C:\ProgramData\Dassault Systemes\DraftSight\Examples
 '     to read/write.
 ' 8.  Start DraftSight.
 ' 9.  Open the Immediate window.
 ' 10. Start debugging the project.
 '
 ' Postconditions:
 ' 1. Each .dxf or .dwg file in
 '    C:\ProgramData\Dassault Systemes\DraftSight\Examples is
 '    filtered for Hatch patterns.
 ' 2. Hatch patterns are changed in the .dxf and .dwg files
 '    that have them. Examine the Immediate window.
 ' 3. Copy all .dxf and .dwg files from the backup folder to
 '     C:\ProgramData\Dassault Systemes\DraftSight\Examples.
 '----------------------------------------------------------------

 Imports System.Collections.Generic
 Imports System.Text
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.IO
 Imports DraftSight.Interop.dsAutomation
 Imports System.Diagnostics

 Module Module1

     Sub Main()

         'Connect to DraftSight application
         Dim dsApp = GetObject(, "DraftSight.Application")
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Check if the specified folder with drawings exists
         Dim folderName As String = "C:\ProgramData\Dassault Systemes\DraftSight\Examples"

         If False = Directory.Exists(folderName) Then
             Console.WriteLine("""" & folderName & """ does not exist.")
             Return
         End If

         'Get drawing files in the folder
         Dim drawings As List(Of String) = GetDrawings(folderName)
         If 0 = drawings.Count Then
             MessageBox.Show("There are no DWG/DXF files in """ & folderName & """ directory.")
             Return
         End If

         'Iterate through all drawings
         For Each docName As String In drawings
             'Open document
             Dim dsDoc As Document = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default,  dsEncoding_e.dsEncoding_Default)
             If dsDoc IsNot Nothing Then

                 ' Print name of document
                 Debug.Print("Name of document: " & dsDoc.GetPathName())

                 'Change Hatch pattern for all Hatch entities in the drawing
                 ChangeHatchPattern(dsDoc)

                 'Save document
                 dsDoc.Save()

                 'Close document
                 dsApp.CloseDocument(docName, True)
             Else
                 MessageBox.Show("""" & docName & """ document could not be opened.")
                 Return
             End If
         Next
     End Sub

     Sub ChangeHatchPattern(ByVal dsDoc As Document)
         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get Sketch Manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Get Selection Manager
         Dim dsSelectionMgr As SelectionManager = dsDoc.GetSelectionManager()

         'Get selection filter
         Dim dsSelectionFilter As SelectionFilter = dsSelectionMgr.GetSelectionFilter()

         'Clear selection filter
         dsSelectionFilter.Clear()

         'Add Hatch entity to the selection filter
         dsSelectionFilter.AddEntityType(dsObjectType_e.dsHatchType)

         'Activate selection filter
         dsSelectionFilter.Active = True

         'Get all Layer names
         Dim layerNames As String() = GetLayers(dsDoc)

         Dim entityTypes As Object
         Dim entityObjects As Object

         'Get Hatch entities
         dsSketchMgr.GetEntities(dsSelectionFilter, layerNames, entityTypes, entityObjects)

         Dim dsEntities As Object() = DirectCast(entityObjects, Object())
         If entityObjects Is Nothing Then
             Debug.Print("   Document does not have Hatch patterns.")
             Debug.Print(" ")
         Else
             Debug.Print("   Document has Hatch patterns.")

             'Iterate through Hatch entities
             For Each entityItem As Object In dsEntities
                 'Cast to Hatch entity
                 Dim dsHatch As Hatch = TryCast(entityItem, Hatch)

                 'Get Hatch pattern
                 Dim patternName As String = ""
                 Dim angle As Double = 0.0
                 Dim scale As Double = 0.0
                 Dim patternType As dsHatchPatternType_e = dsHatchPatternType_e.dsHatchPatternType_Predefined
                 Dim spacing As Double = 1.0
                 Dim dsHatchPattern As HatchPattern = dsHatch.GetHatchPattern()

                 dsHatchPattern.GetHatchOrSolidData(patternName, angle, scale, patternType, spacing)
                 Debug.Print("   Pattern name, angle, scale, pattern types, spacing: " & patternName & ", " & angle & ", " & scale & ", " & patternType & ", " & spacing)

                 'Update Hatch pattern
                 patternName =  "HOUND"
                 angle = 0.0
                 scale = 1.0
                 patternType = dsHatchPatternType_e.dsHatchPatternType_Predefined
                 spacing = 1.0
                 dsHatchPattern.SetHatchOrSolidData(patternName, angle, scale, patternType, spacing)
             Next
             Debug.Print(" ")
         End If
     End Sub

     Function GetLayers(ByVal dsDoc As Document) As String()
         'Get Layer Manager and Layer names
         Dim dsLayerManager As LayerManager = dsDoc.GetLayerManager()

         Dim dsLayers As Object() = DirectCast(dsLayerManager.GetLayers(), Object())

         Dim layerNames As String() = New  String(dsLayers.Length - 1) {}

         For index As Integer = 0 To dsLayers.Length - 1
             Dim dsLayer As Layer = TryCast(dsLayers(index), Layer)
             layerNames(index) = dsLayer.Name
         Next

         Return layerNames
     End Function

     Function GetDrawings(ByVal folderName As String) As List(Of String)
         Dim drawings As New List(Of String)()
         'Get DWG files
         Dim files As String() = Directory.GetFiles(folderName, "*.dwg")
         If files IsNot Nothing Then
             drawings.AddRange(files)
         End If

         'Get DXF files
         files = Directory.GetFiles(folderName, "*.dxf")
         If files IsNot Nothing Then
             drawings.AddRange(files)
         End If

         Return drawings
     End Function
 End Module
```
