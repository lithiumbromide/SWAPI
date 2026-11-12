---
title: "Insert SimpleNote Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_SimpleNote_Example_VBA.htm"
---

# Insert SimpleNote Example (VBA)

This example shows how to insert and change a SimpleNote in a drawing document.

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
' 1. A message box pops up when a SimpleNote is
'    inserted in the drawing.
' 2. The selection filter is set to select SimpleNotes only and
'    is activated.
' 3. The SimpleNote is selected and its text changed. Examine
'    the drawing to verify.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsSimpleNote As DraftSight.SimpleNote
    Dim startX, startY, startZ As Double
    Dim noteValue As String
    Dim angle, height As Double
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
       'SimpleNote parameters (angle value should be passed in radians)
        startX = 0#
        startY = 0#
        startZ = 0#
        noteValue = "First sample text"
        angle = 3.14159265358979 / 4 '45 degrees in radians
        height = 1#
```

```
        'Add a SimpleNote
        Set dsSimpleNote = dsSketchManager.InsertSimpleNote(startX, startY, startZ, height, angle, noteValue)
```

```
        If Not dsSimpleNote Is Nothing Then
            MsgBox "A SimpleNote was added to drawing."
        End If
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight."
```

```
    End If
```

```
    'Change SimpleNote text
    ChangeSimpleNotesText dsDoc, dsSketchManager
```

```
End Sub
```

```
    Sub ChangeSimpleNotesText(ByVal dsDoc As DraftSight.Document, ByVal dsSketchManager As DraftSight.SketchManager)
```

```
        'Get Selection Manager
        Dim dsSelectionMgr As DraftSight.SelectionManager
        Set dsSelectionMgr = dsDoc.GetSelectionManager()
```

```
        'Get selection filter
        Dim dsSelectionFilter As DraftSight.SelectionFilter
        Set dsSelectionFilter = dsSelectionMgr.GetSelectionFilter()
```

```
        'Clear selection filter
        dsSelectionFilter.Clear
```

```
        'Add filter to get only SimpleNotes
        dsSelectionFilter.AddEntityType (dsObjectType_e.dsSimpleNoteType)
```

```
        'Activate selection filter
        dsSelectionFilter.Active = True
```

```
        'Get all Layer names
        Dim layerNames As Variant
        layerNames = GetLayers(dsDoc)
```

```
        Dim entityTypes As Variant
        Dim entityObjects As Variant
        Dim entityItem As Variant
```

```
        'Get SimpleNote entities
        dsSketchManager.GetEntities dsSelectionFilter, layerNames, entityTypes, entityObjects
```

```
        Const newNoteValue As String = "New sample text"
```

```
        If Not IsArray(entityObjects) Then
            Debug.Print ("   Document does not have any SimpleNotes.")
            Debug.Print (" ")
        Else
            Debug.Print ("   Document has SimpleNotes.")
            'Iterate through SimpleNotes
            For Each entityItem In entityObjects
                'Cast to SimpleNote
                Dim dsSimpleNote As DraftSight.SimpleNote
                Set dsSimpleNote = entityItem
                'Get SimpleNote
                Dim simpleNoteText As String
                simpleNoteText = dsSimpleNote.Contents
                'Set new SimpleNote text
                dsSimpleNote.Contents = newNoteValue
```

```
            Next
            Debug.Print (" ")
        End If
```

```
    End Sub
```

```
    Public Function GetLayers(ByVal dsDoc As Document) As String()
        'Get Layer Manager
        Dim dsLayerManager As DraftSight.LayerManager
        Set dsLayerManager = dsDoc.GetLayerManager
        Dim dsLayers() As Object
```

```
	'Get Layers
        dsLayers = dsLayerManager.GetLayers()
        Dim dslayerNames() As String
        Dim nbrLayers As Long
        nbrLayers = UBound(dsLayers)
        ReDim dslayerNames(nbrLayers)
```

```
        Dim index As Long
        For index = 0 To nbrLayers
            Dim dsLayer As DraftSight.Layer
            Set dsLayer = dsLayers(index)
            dslayerNames(index) = dsLayer.Name
        Next
```

```
        GetLayers = dslayerNames
```

```
    End Function
```
