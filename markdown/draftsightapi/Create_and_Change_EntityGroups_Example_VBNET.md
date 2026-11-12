---
title: "Create and Change EntityGroups Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_EntityGroups_Example_VBNET.htm"
---

# Create and Change EntityGroups Example (VB.NET)

This example shows how to create and change EntityGroups.

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
' 1. Inserts entities, two lines and two circles, in the drawing.
' 2. Creates two EntityGroups:
'    * SampleGroup1 contains two lines, line1 and line2.
'    * SampleGroup2 contains two circles, circle1 and circle2.
' 3. Changes the color of the lines from white to red.
' 4. Removes an entity, circle1, from SampleGroup2.
' 5. Adds an entity, circle2, to SampleGroup1.
' 6. Reorders SampleGroup1.
' 7. Explodes SampleGroup2, which removes the definition
'    from the drawing; however, circle1 remains as an entity
'    in the drawing.
' 8. Renames SampleGroup1 and changes its description.
'
' NOTE: Execution of the macro stops several times. Follow the
' instructions in the macro each time execution stops.
'----------------------------------------------------------------
Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms
Imports System.Diagnostics

Module Module1

    Public dsApp As DraftSight.Interop.dsAutomation.Application
    Public dsDoc As Document

    Sub Main()
        'Connect to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        ' Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        If dsApp Is Nothing Then
            Return
        End If

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Insert entities
        Dim dsSketchMgr As SketchManager = dsApp.GetActiveDocument().GetModel().GetSketchManager()
        Dim line1 As Line = dsSketchMgr.InsertLine(0, 0, 0, 10, 10, 0)
        Dim line2 As Line = dsSketchMgr.InsertLine(5, 0, 0, 15, 10, 0)
        Dim circle1 As Circle = dsSketchMgr.InsertCircle(5, 5, 0, 10)
        Dim circle2 As Circle = dsSketchMgr.InsertCircle(10, 5, 0, 10)

        Dim EntitiesArray1 As DispatchWrapper() = New DispatchWrapper(1) {}
        EntitiesArray1(0) = New DispatchWrapper(line1)
        EntitiesArray1(1) = New DispatchWrapper(line2)

        Dim EntitiesArray2 As DispatchWrapper() = New DispatchWrapper(1) {}
        EntitiesArray2(0) = New DispatchWrapper(circle1)
        EntitiesArray2(1) = New DispatchWrapper(circle2)

        CreateGroups(EntitiesArray1, EntitiesArray2)

        System.Diagnostics.Debugger.Break()
        'Type GROUP at the command-window prompt
        'to verify that two EntityGroups, SampleGroup1
        'and SampleGroup2, were created
        'Press OK to close the dialog
        'Press F5 in the IDE to continue

        'Get SampleGroup2 and remove circle2
        Dim dsGroup2 As Group = dsDoc.GetGroup("SampleGroup2")
        If dsGroup2.HasEntity(circle2) Then
            Dim index As Integer = dsGroup2.GetIndex(circle2)
            dsGroup2.RemoveEntityAt(index)
        End If

        'Get SampleGroup1 and add circle1 at last position
        Dim dsGroup1 As Group = dsDoc.GetGroup("SampleGroup1")
        Dim EntitiesArray As DispatchWrapper() = New DispatchWrapper(0) {}
        EntitiesArray(0) = New DispatchWrapper(circle1)
        Dim count As Integer = dsGroup1.GetEntitiesCount()
        dsGroup1.InsertEntitiesAt(count, EntitiesArray)

        Dim newCount As Integer = dsGroup1.GetEntitiesCount()
        If newCount <> count + 1 Then
            MessageBox.Show("Circle1 was not inserted.")
        End If

        'Move circle1 to second position (index 1)
        Dim circleIndex As Integer = dsGroup1.GetIndex(circle1)
        If circleIndex <> count Then
            MessageBox.Show("Circle1 inserted at wrong position.")
        End If

        dsGroup1.Reorder(circleIndex, 1, 1)
        circleIndex = dsGroup1.GetIndex(circle1)
        If circleIndex <> 1 Then
            MessageBox.Show("Circle1 inserted at wrong position.")
        End If

        'Explode SampleGroup2
        dsGroup2.Explode()

        System.Diagnostics.Debugger.Break()
        'Type GROUP at the command-window prompt
        'to verify that only SampleGroup1 exists
        'Press OK to close the dialog
        'Press F5 in the IDE to continue

        Dim dsGroups As Object = Nothing
        dsGroups = dsDoc.GetGroups()

        Dim groupObjects As Object() = DirectCast(dsGroups, Object())
        If groupObjects.Length <> 1 Then
            MessageBox.Show("Group2 was not exploded.")
        End If

        'Rename SampleGroup1 and change description
        dsGroup1.Rename("SampleGroup")
        dsGroup1.Description = "My sample group."

        System.Diagnostics.Debugger.Break()
        'Type GROUP at the command-window prompt
        'to verify that SampleGroup1 was renamed
        'to SampleGroup and its description
        'changed to "My sample group"
        'Press OK to close the dialog
        'Press F5 in the IDE to continue
    End Sub

    Private Sub CreateGroups(ByVal EntitiesArray1 As DispatchWrapper(), ByVal EntitiesArray2 As DispatchWrapper())
        'Create group
        Dim dsGroup1 As Group = dsDoc.CreateGroup("SampleGroup1", False, "This is my first sample group.", EntitiesArray1)

        Dim dsEntities As Object = Nothing
        Dim dsEntityTypes As Object = Nothing

        dsEntities = dsGroup1.GetEntities(dsEntityTypes)

        Dim entityObjects As Object() = DirectCast(dsEntities, Object())
        Dim dsEntityTypesArray As Integer() = DirectCast(dsEntityTypes, Integer())

        If entityObjects Is Nothing AndAlso dsEntityTypesArray Is Nothing Then
            Return
        End If

        'Change color of lines from white to red
        Dim dsEntityHelper As EntityHelper = dsApp.GetEntityHelper()
        Dim dsColor As Color = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Red)

        For Each dsEntity As Object In entityObjects
            If dsEntity IsNot Nothing Then
                dsEntityHelper.SetColor(dsEntity, dsColor)
            End If
        Next

        Dim dsGroup2 As Group = dsDoc.CreateGroup("SampleGroup2", False, "This is my second sample group.", EntitiesArray2)
    End Sub

End Module
```
