---
title: "Create and Change EntityGroups Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_and_Change_EntityGroups_Example_VBA.htm"
---

# Create and Change EntityGroups Example (VBA)

This example shows how to create and change EntityGroups.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
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
' NOTE: There are several Stop statements in the macro. Follow
' the instructions in the macro at each Stop statement.
'----------------------------------------------------------------
Option Explicit
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsGroup1 As DraftSight.Group
    Dim dsGroup2 As DraftSight.Group
```

```
    Sub main()
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Insert entities
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsApp.GetActiveDocument().GetModel().GetSketchManager()
        Dim line1 As DraftSight.Line
        Set line1 = dsSketchMgr.InsertLine(0, 0, 0, 10, 10, 0)
        Dim line2 As DraftSight.Line
        Set line2 = dsSketchMgr.InsertLine(5, 0, 0, 15, 10, 0)
        Dim circle1 As DraftSight.Circle
        Set circle1 = dsSketchMgr.InsertCircle(5, 5, 0, 10)
        Dim circle2 As DraftSight.Circle
        Set circle2 = dsSketchMgr.InsertCircle(10, 5, 0, 10)
```

```
        Dim EntitiesArray1(1) As DraftSight.Line
        Set EntitiesArray1(0) = line1
        Set EntitiesArray1(1) = line2
```

```
        Dim EntitiesArray2(1) As DraftSight.Circle
        Set EntitiesArray2(0) = circle1
        Set EntitiesArray2(1) = circle2
```

```
        Set dsGroup1 = dsDoc.CreateGroup("SampleGroup1", False, "This is my first sample group.", EntitiesArray1)
```

```
        Dim dsEntities As Variant
        Dim dsEntityTypes As Variant
```

```
        dsEntities = dsGroup1.GetEntities(dsEntityTypes)
```

```
        Debug.Print ("Size of dsEntities: " & UBound(dsEntities))
```

```
        'Change color of lines from white to red
        Dim dsEntityHelper As DraftSight.EntityHelper
        Set dsEntityHelper = dsApp.GetEntityHelper()
        Dim dsColor As DraftSight.Color
        Set dsColor = dsApp.GetNamedColor(dsNamedColor_e.dsNamedColor_Red)
```

```
        Dim dsEntity As Object
        Dim i As Long
        For i = 0 To UBound(dsEntities)
            Set dsEntity = dsEntities(i)
            dsEntityHelper.SetColor dsEntity, dsColor
        Next
```

```
        Set dsGroup2 = dsDoc.CreateGroup("SampleGroup2", False, "This is my second sample group.", EntitiesArray2)
```

```
        Stop
        'Type GROUP at the command window
        'to verify that two EntityGroups, SampleGroup1
        'and SampleGroup2, were created
        'Press OK to close the dialog
        'Press F5 in the IDE to continue
```

```
        'Get SampleGroup2 and remove circle2
        Set dsGroup2 = dsDoc.GetGroup("SampleGroup2")
        If dsGroup2.HasEntity(circle2) Then
            Dim index As Long
            index = dsGroup2.GetIndex(circle2)
            dsGroup2.RemoveEntityAt (index)
        End If
```

```
        'Get SampleGroup1 and add circle1 at last position
        Set dsGroup1 = dsDoc.GetGroup("SampleGroup1")
        Dim EntitiesArray(0) As Object
        Set EntitiesArray(0) = circle1
        Dim count As Long
        count = dsGroup1.GetEntitiesCount()
        dsGroup1.InsertEntitiesAt count, EntitiesArray
```

```
        Dim newCount As Long
        newCount = dsGroup1.GetEntitiesCount()
        If newCount <> count + 1 Then
            MsgBox ("Circle1 was not inserted.")
        End If
```

```
        'Move circle1 to second position (index 1)
        Dim circleIndex As Long
        circleIndex = dsGroup1.GetIndex(circle1)
        If circleIndex <> count Then
            MsgBox ("Circle1 inserted at wrong position.")
        End If
```

```
        dsGroup1.Reorder circleIndex, 1, 1
        circleIndex = dsGroup1.GetIndex(circle1)
        If circleIndex <> 1 Then
            MsgBox ("Circle1 inserted at wrong position.")
        End If
```

```
        'Explode SampleGroup2
        dsGroup2.Explode
```

```
        Stop
        'Type GROUP at the command window
        'to verify that only SampleGroup1 exists
        'Press OK to close the dialog
        'Press F5 in the IDE to continue
```

```
        Dim dsGroups() As DraftSight.Group
        dsGroups = dsDoc.GetGroups()
```

```
        Dim nbrGroups As Long
        nbrGroups = UBound(dsGroups)
        If nbrGroups <> 0 Then
            MsgBox ("Group2 was not exploded.")
        End If
```

```
        'Rename SampleGroup1 and change description
        dsGroup1.Rename ("SampleGroup")
        dsGroup1.Description = "My sample group."
```

```
        Stop
        'Type GROUP at the command window
        'to verify that SampleGroup1 was renamed
        'to SampleGroup and its description
        'changed to "My sample group"
        'Press OK to close the dialog
        'Press F5 in the IDE to continue
```

```
    End Sub
```
