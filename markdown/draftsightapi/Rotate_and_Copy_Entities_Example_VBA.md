---
title: "Rotate and Copy Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate_and_Copy_Entities_Example_VBA.htm"
---

# Rotate and Copy Entities Example (VBA)

This example shows how to rotate and copy selected entities.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a new document.
' 5. Construct these three entities: Circle, Spline, and Ellipse.
' 6. Run the macro.
'
' Postconditions:
' 1. When the prompt appears in the DraftSight command window,
'    select the Circle and Ellipse entities and press
'    the Enter key. The selected entities are rotated.
' 2. Execution stops so that you can examine the drawing to
'    verify that the selected entities were rotated. Click the
'    Continue button in the IDE to continue.
' 3. The selected entities are copied.
'----------------------------------------------------------------
Option Explicit
```

```
Dim dsApp As DraftSight.Application
```

```
Sub main()
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Get Selection Manager
        Dim dsSelectionMgr As DraftSight.SelectionManager
        Set dsSelectionMgr = dsDoc.GetSelectionManager
```

```
        'Get selection filter
        Dim dsSelectionFilter As DraftSight.SelectionFilter
        Set dsSelectionFilter = dsSelectionMgr.GetSelectionFilter
```

```
        'Clear selection filter
        dsSelectionFilter.Clear
```

```
        'Add Circle and Ellipse entity types to the selection filter
        Dim entityType As Variant
        Dim entityArray As Variant
        entityArray = Array(dsObjectType_e.dsCircleType, dsObjectType_e.dsEllipseArcType)
```

```
        For Each entityType In entityArray
            dsSelectionFilter.AddEntityType (entityType)
        Next
```

```
        'Activate selection filter
        dsSelectionFilter.Active = True
```

```
        'Get command message object
        Dim dsCommandMessage As CommandMessage
        Set dsCommandMessage = dsApp.GetCommandMessage
```

```
        'Clear previous selection
        dsSelectionMgr.ClearSelections (dsSelectionSetType_Previous)
```

```
        'Prompt user to select the Circle and the Ellipse
        Dim singleSelection As Boolean
        singleSelection = False
        Dim prompt As String
        prompt = "Select the Circle and Ellipse entities"
        Dim errorMessage As String
        errorMessage = "Unknown entity"
```

```
        Dim statusSelect As Boolean
        statusSelect = dsCommandMessage.PromptForSelection(singleSelection, prompt, errorMessage)
```

```
        If statusSelect Then
```

```
            'Get number of selected entities
            Dim count As Long
            count = dsSelectionMgr.GetSelectedObjectCount(dsSelectionSetType_e.dsSelectionSetType_Previous)
            If count <> 2 Then
                Debug.Print ("You did not select the two entities. Rerun the macro and try again.")
                End
            End If
```

```
             Dim dsEntityType As dsObjectType_e
            Dim dsEntities() As Object
            Dim dsEntityTypes() As dsObjectType_e
            ReDim dsEntities(count - 1)
            ReDim dsEntityTypes(count - 1)
```

```
            'Get selected entities
            Dim index As Long
            index = 0
            For index = 0 To (count - 1)
                Dim selectedEntity As Object
                Set selectedEntity = dsSelectionMgr.GetSelectedObject(dsSelectionSetType_Previous, index, dsEntityType)
                dsEntityTypes(index) = dsEntityType
                Set dsEntities(index) = selectedEntity
            Next
```

```
            'Rotation parameters
            Dim pivotPointX As Double
            pivotPointX = 0#
            Dim pivotPointY As Double
            pivotPointY = 0#
            Dim rotateAngle As Double
            rotateAngle = 3.14159265358979 / 4 ' In radians
```

```
            'Rotate entities
            dsSketchMgr.RotateEntities pivotPointX, pivotPointY, rotateAngle, dsEntityTypes, dsEntities
```

```
            'Stop execution
            'Examine the document
            Stop
```

```
            'Click the Continue button in the IDE
```

```
            'Copy parameters
            Dim displacementX As Double
            displacementX = 2#
            Dim displacementY As Double
            displacementY = 2#
            Dim displacementZ As Double
            displacementZ = 0#

            Dim dsEntityCopies As Variant
```

```
            'Copy entities

            dsEntityCopies = dsSketchMgr.CopyEntities2( displacementX, displacementY, displacementZ, dsEntityTypes, dsEntities)
```

```
        End If
```

```
End Sub
```
