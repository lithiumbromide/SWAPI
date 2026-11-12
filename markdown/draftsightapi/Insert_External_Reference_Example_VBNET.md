---
title: "Insert External Reference Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_External_Reference_Example_VBNET.htm"
---

# Insert External Reference Example (VB.NET)

This example shows how to insert an external reference to a drawing document.

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
' Postconditions: A message box pops up when an external reference
' is inserted in the drawing document.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation

Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsExtReference As BlockInstance
	Dim dsReference as ExternalReference
        Dim pathName As String
        Dim insertX, insertY, insertZ, scaleValue, rotation As Double

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

        'Get active document
        dsDoc = dsApp.GetActiveDocument()

        If Not dsDoc Is Nothing Then
            'Get model space
            dsModel = dsDoc.GetModel()
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()

            'External reference parameters (rotation value should be in radians)
            pathName = "C:\Block.dwg"
            insertX = 0.0#
            insertY = 0.0#
            insertZ = 0.0#
            scaleValue = 1.0#
            rotation = 0.0#
            'Add a Block instance
            dsExtReference = dsSketchManager.InsertExternalReference(pathName, insertX, insertY, insertZ, scaleValue, rotation)

            If dsExtReference Is Nothing Then
                MsgBox(pathName & " file was not found.")
            Else
                MsgBox("An external reference was added to the drawing.")
                Dim references As Object
                Dim reference As Object
                references = dsDoc.GetExternalReferences
                reference = references(0)
                dsReference = reference
                If Not dsReference Is Nothing Then
                    MsgBox("Name of external reference " & dsReference.Name & ".")
                End If
```

```
            End If
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
    End Sub
End Module
```
