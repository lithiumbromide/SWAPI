---
title: "Insert Block Instance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Block_Instance_Example_VBNET.htm"
---

# Insert Block Instance Example (VB.NET)

This example shows how to insert a Block instance in a drawing document.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a new document.
' 5. If C:\Block.dwg exists, then skip this step.
'    - or -
'    If C:\Block.dwg does not exist, then construct
'    some geometry in the drawing, save the drawing
'    as C:\Block.dwg, and open a new drawing document.
' 6. Start debugging the project.
'
' Postconditions: A message box pops up when a Block instance is
' inserted in the drawing document.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsBlockInstance As BlockInstance
        Dim pathName As String
        Dim insertX, insertY, insertZ, scaleX, scaleY, scaleZ, rotation As Double
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
            'Block instance parameters (rotation value should be in radians)
            pathName = "C:\Block.dwg"
            insertX = 0.0#
            insertY = 0.0#
            insertZ = 0.0#
            scaleX = 1.0#
            scaleY = 1.0#
            scaleZ = 1.0#
            rotation = 0.0#
```

```
            'Add a Block instance
            dsBlockInstance = dsSketchManager.InsertBlock2(pathName, insertX, insertY, insertZ, scaleX, scaleY, scaleZ, rotation)
```

```
            If dsBlockInstance Is Nothing Then
                MsgBox(pathName & " file was not found.")
            Else
                MsgBox("A Block instance from '" & pathName & "' file was added to the drawing.")
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
```

```
    End Sub
```

```
End Module
```
