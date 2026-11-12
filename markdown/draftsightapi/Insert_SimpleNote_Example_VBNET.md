---
title: "Insert SimpleNote Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_SimpleNote_Example_VBNET.htm"
---

# Insert SimpleNote Example (VB.NET)

This example shows how to insert and change a SimpleNote in a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
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
Imports DraftSight.Interop.dsAutomation
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsSimpleNote As SimpleNote
        Dim startX, startY, startZ As Double
        Dim noteValue As String
        Dim angle, height As Double
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get model space
            dsModel = dsDoc.GetModel()
```

```
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()
```

```
            'SimpleNote parameters (angle value should be passed in radians)
            startX = 0.0#
            startY = 0.0#
            startZ = 0.0#
            noteValue = "Sample text"
            angle = 3.14159265358979 / 4 '45 degrees in radians
            height = 1.0#
```

```
            'Add a SimpleNote
            dsSimpleNote = dsSketchManager.InsertSimpleNote(startX, startY, startZ, height, angle, noteValue)
```

```
            If Not dsSimpleNote Is Nothing Then
                MsgBox("A SimpleNote was added to drawing.")
            End If
```

```
        Else
```

```
            MsgBox("There are no open documents in DraftSight.")
```

```
        End If

	'Change SimpleNote text
        ChangeSimpleNotesText(dsDoc, dsSketchManager)
```

```
    End Sub
```

```
    Sub ChangeSimpleNotesText(ByVal dsDoc As Document, ByVal dsSketchManager As SketchManager)
        'Get Selection Manager
        Dim dsSelectionMgr As SelectionManager = dsDoc.GetSelectionManager()
```

```
        'Get selection filter
        Dim dsSelectioFilter As SelectionFilter = dsSelectionMgr.GetSelectionFilter()
```

```
        'Clear selection filter
        dsSelectioFilter.Clear()
```

```
        'Add filter to get only SimpleNotes
        dsSelectioFilter.AddEntityType(dsObjectType_e.dsSimpleNoteType)
```

```
        'Activate selection filter
        dsSelectioFilter.Active = True
```

```
        'Get all Layers in drawing
        Dim layerNames As String() = GetLayerNames(dsDoc)
```

```
        'Get SimpleNote entities
        Dim entityObjects As Object
        Dim entityTypes As Object
        dsSketchManager.GetEntities(dsSelectioFilter, layerNames, entityTypes, entityObjects)
        If entityObjects IsNot Nothing AndAlso entityTypes IsNot Nothing Then
            Dim dsEntityArray As Object() = DirectCast(entityObjects, Object())
```

```
            Const newNoteValue As String = "New sample text"
```

```
            'Iterate through all SimpleNote entities
            For index As Integer = 0 To dsEntityArray.Length - 1
                'Cast the selected object to SimpleNote
                Dim dsSimpleNote As SimpleNote = TryCast(dsEntityArray(index), SimpleNote)
```

```
                'Get SimpleNote text
                Dim noteValue As String = dsSimpleNote.Contents
```

```
                'Set new text for SimpleNote
                dsSimpleNote.Contents = newNoteValue
            Next
        End If
    End Sub
```

```
    Function GetLayerNames(ByVal dsDoc As Document) As String()
        Dim layerNames As String() = Nothing
```

```
        Dim dsLayerManager As LayerManager = dsDoc.GetLayerManager()
```

```
        Dim dsLayers As Object() = DirectCast(dsLayerManager.GetLayers(), Object())
        If dsLayers IsNot Nothing Then
            layerNames = New String(dsLayers.Length - 1) {}
```

```
            For index As Integer = 0 To dsLayers.Length - 1
                Dim dsLayer As Layer = TryCast(dsLayers(index), Layer)
                layerNames(index) = dsLayer.Name
            Next
        End If
```

```
        Return layerNames
    End Function
```

```
End Module
```

```
End Module
```
