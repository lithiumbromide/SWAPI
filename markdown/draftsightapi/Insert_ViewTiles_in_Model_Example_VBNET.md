---
title: "Insert ViewTiles in Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_ViewTiles_in_Model_Example_VBNET.htm"
---

# Insert ViewTiles in Model Example (VB.NET)

This example shows how to:

- insert ViewTiles in a model document.
- turn off and on the display of the coordinate system icon in each ViewTile.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET console project in Microsoft
'    Visual Studio 2012.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight.
' 5. Ensure that the file specified to open exits.
' 7. Press F11 to step into the code.
' 8. Press F10 repeatedly to step through the code. Observe
'    the changes in the model document and ViewTiles while
'    stepping through the code.
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
Imports DraftSight.Interop.dsAutomation
Imports System
Imports System.Runtime.InteropServices

Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document = Nothing
        Dim dsModel As Model = Nothing

        'Connect to DraftSight
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        'Abort any command currently running
        'in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Open document
        Dim docName As String = "C:\ProgramData\Dassault Systemes\DraftSight\Examples\A-54643.DWG"
        dsDoc = dsApp.OpenDocument2(docName, dsDocumentOpenOption_e.dsDocumentOpen_Default, dsEncoding_e.dsEncoding_Default)

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If (dsDoc IsNot Nothing) Then
            'Get model space
            dsModel = dsDoc.GetModel()
        Else
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If

        'Insert ViewTiles
        Dim viewTiles(3) As Object
        Dim index As Long
        Dim dsViewTile As ViewTile
        viewTiles = dsModel.InsertViewTiles(dsViewTilesMode_e.dsViewTilesMode_4_Left, dsViewTilesApplyTo_e.dsViewTilesApplyTo_ActiveViewTile)
        If IsArray(viewTiles) Then
            For index = LBound(viewTiles) To UBound(viewTiles)
                dsViewTile = viewTiles(index)
                'Turn off displaying coordinate system icon at origin
                dsViewTile.CSIconIsOn = False
                If Not (dsViewTile.CSIconIsOn) Then
                    'Display coordinate system at origin
                    dsViewTile.CSIconAtOrigin = True
                    'Turn on displaying coordinate system icon at origin
                    dsViewTile.CSIconIsOn = True
                End If
            Next
        End If

    End Sub

End Module
```
