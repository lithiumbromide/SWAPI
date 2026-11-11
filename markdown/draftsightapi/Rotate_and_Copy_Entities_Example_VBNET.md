---
title: "Rotate and Copy Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate_and_Copy_Entities_Example_VBNET.htm"
---

# Rotate and Copy Entities Example (VB.NET)

This example shows how to rotate and copy selected entities.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this example into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
 ' 4. Add references to System and System.Windows.Forms.
 ' 5. Start DraftSight and open a new document.
 ' 6. Construct multiple entities (e.g., circle, rectangle, 2D PolyLine, etc.).
 ' 7. Start debugging the project.
 '
 ' Postconditions:
 ' 1. When the prompt appears in the DraftSight command window,
 '    select the entities to rotate and press the Enter key. The
 '    selected entities are rotated.
 ' 2. Execution stops so that you can examine the drawing to
 '    verify that the selected entities were rotated. Click the
 '    Continue button in the IDE to continue.
 ' 3. The selected entities are copied.
 '----------------------------------------------------------------

 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Runtime.InteropServices
 Imports System.Windows.Forms
 Imports System.Diagnostics

 Module Module1

     Sub Main()

         'Connect to DraftSight application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application
         dsApp = GetObject(, "DraftSight.Application")

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

         'Get Sketch Manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Get selection manager
         Dim dsSelectionMgr As SelectionManager = dsDoc.GetSelectionManager()

         'Get selection filter
         Dim dsSelectionFilter As SelectionFilter = dsSelectionMgr.GetSelectionFilter()

         'Clear selection filter
         dsSelectionFilter.Clear()

         'Add all entities to the selection filter
         For Each entityType As dsObjectType_e In [Enum].GetValues(GetType(dsObjectType_e))
             dsSelectionFilter.AddEntityType(entityType)
         Next

         'Activate selection filter
         dsSelectionFilter.Active = True

         'Get command message object
         Dim dsCommandMessage As CommandMessage = dsApp.GetCommandMessage()

         'Clear previous selection
         dsSelectionMgr.ClearSelections(dsSelectionSetType_e.dsSelectionSetType_Previous)

         'Run prompt to select entities
         Dim singleSelection As Boolean = False
         Dim prompt As String = "Select entities"
         Dim errorMessage As String = "Unknown entity"
         If dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage) Then
             'Get number of selected objects
             Dim count As Integer = dsSelectionMgr.GetSelectedObjectCount(dsSelectionSetType_e.dsSelectionSetType_Previous)

             Dim dsEntities As DispatchWrapper() = New DispatchWrapper(count - 1) {}
             Dim dsEntityTypes As Integer() = New Integer(count - 1) {}

             'Get selected entities
             For index As Integer = 0 To count - 1
                 Dim entityType As dsObjectType_e
                 Dim selectedEntity As Object = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, entityType)
                 dsEntities(index) = New DispatchWrapper(selectedEntity)

                 dsEntityTypes(index) = CInt(entityType)
             Next

             'Rotation parameters
             Dim pivotPointX As Double = 0.0
             Dim pivotPointY As Double = 0.0
             Dim rotateAngle As Double = Math.PI / 4 'In radians

             'Rotate entities
             dsSketchMgr.RotateEntities(pivotPointX, pivotPointY, rotateAngle, dsEntityTypes, dsEntities)

             'Stop execution
             'Examine the document
             System.Diagnostics.Debugger.Break()

             'Click the Continue button in the IDE

             'Copy parameters
             Dim displacementX As Double = 2.0
             Dim displacementY As Double = 2.0
             Dim displacementZ As Double = 0.0
            Dim dsEntityCopies As   Object()

             'Copy entities
             dsEntityCopies = dsSketchMgr.CopyEntities2(displacementX, displacementY, displacementZ, dsEntityTypes, dsEntities)

         End If

     End Sub

 End  Module
```
