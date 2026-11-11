---
title: "Insert External Reference Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_External_Reference_Example_VBA.htm"
---

# Insert External Reference Example (VBA)

This example shows how to insert an external reference to a drawing document.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a new drawing document.
' 5. If C:\Block.dwg exists, then skip this step.
'    - or -
'    If C:\Block.dwg does not exist, then construct
'    some geometry in the drawing, save the drawing
'    as C:\Block.dwg, and open a new drawing document.
' 6. Run the macro.
'
' Postconditions: A message box pops up when an external reference
' is inserted in the drawing document.
'----------------------------------------------------------------
Option Explicit
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsExtReference As DraftSight.BlockInstance
    Dim dsReference as DraftSight.ExternalReference
    Dim pathName As String
    Dim insertX, insertY, insertZ, scaleValue, rotation As Double
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
        'External reference parameters (rotation value should be in radians)
        pathName = "C:\Block.dwg"
        insertX = 0#
        insertY = 0#
        insertZ = 0#
        scaleValue = 1#
        rotation = 0#
```

```
        'Add an external reference
        Set dsExtReference = dsSketchManager.InsertExternalReference(pathName, insertX, insertY, insertZ, scaleValue, rotation)
```

```
        If dsExtReference Is Nothing Then
            MsgBox pathName & " file was not found."
        Else
            MsgBox "A external reference was added to drawing."
            Dim references As Variant
            Dim reference As Object
            references = dsDoc.GetExternalReferences
            Set reference = references(0)
            Set dsReference = reference
            If Not dsReference Is Nothing Then
                MsgBox ("Name of external reference " & dsReference.Name & ".")
            End If

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
End Sub
```
