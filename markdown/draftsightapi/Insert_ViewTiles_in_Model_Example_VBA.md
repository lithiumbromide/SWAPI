---
title: "Insert ViewTiles in Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_ViewTiles_in_Model_Example_VBA.htm"
---

# Insert ViewTiles in Model Example (VBA)

This example shows how to:

- insert ViewTiles in a model document.
- turn off and on the display of the coordinate system icon in each ViewTile.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Ensure that the file specified to open exists.
' 6. Press F5 and click Step Into to step into the code.
' 7. Press F8 repeatedly to step through the code. Observe
'    the changes in the model document and ViewTiles.
'
' Postconditions:
' 1. Opens the specified file.
' 2. Inserts four ViewTiles.
' 3. Iterates through the four ViewTiles. For each ViewTile:
'    a. Turns off displaying the coordinate system at the
'       the origin.
'    b. Specifies to display the coordinate system at the origin.
'    c. Turns on displaying the coordinate system at the
'       origin.
' 4. Close the model document without saving any changes.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    'Connect to DraftSight
    Dim dsApp As DraftSight.Application
    Set dsApp = GetObject(, "DraftSight.Application")

    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand

    'Open document
    Dim dsDoc As DraftSight.Document
    Dim docName As String
    docName = "C:\ProgramData\Dassault Systemes\DraftSight\Examples\A-54643.DWG"
    Set dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)
    If dsDoc Is Nothing Then
        MsgBox "There are no open documents in DraftSight."
        Return
    End If
    'Get active document
    dsApp.GetActiveDocument
```

```
    'Get model
    Dim dsModel As DraftSight.Model
    Set dsModel = dsDoc.GetModel
```

```
    'Insert ViewTiles
    Dim viewTiles As Variant
    Dim index As Long
    Dim dsViewTile As DraftSight.ViewTile
    viewTiles = dsModel.InsertViewTiles(dsViewTilesMode_e.dsViewTilesMode_4_Left, dsViewTilesApplyTo_e.dsViewTilesApplyTo_ActiveViewTile)
    If IsArray(viewTiles) Then
        For index = LBound(viewTiles) To UBound(viewTiles)
            Set dsViewTile = viewTiles(index)
            'Turn off displaying coordinate system icon at origin
            dsViewTile.CSIconIsOn = False
            If Not (dsViewTile.CSIconIsOn) Then
                'Display coordinate system at origin
                dsViewTile.CSIconAtOrigin = True
                'Turn on displaying coordinate system icon at origin
                dsViewTile.CSIconIsOn = True
            End If
```

```
        Next
    End If
```

```
End Sub
```
