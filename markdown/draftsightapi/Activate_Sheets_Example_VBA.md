---
title: "Activate Sheets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Activate_Sheets_Example_VBA.htm"
---

# Activate Sheets Example (VBA)

This example shows how to activate each Sheet in a drawing.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document with multiple Sheets.
' 5. Run the macro.
'
'Postconditions:
' 1. Pops up a message box when a Sheet is activated.
' 2. Click OK to close each message box.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()

    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document

    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")

    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand

    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
        'Activate each Sheet, one by one
        SwitchSheets dsDoc
    Else
        MsgBox "There are no open documents in DraftSight."
    End If
End Sub
```

```
Sub SwitchSheets(dsDoc As DraftSight.Document)
    Dim dsSheet As DraftSight.Sheet
    Dim dsVarSheets As Variant
    Dim index As Integer
    Dim sheetName As String
    'Get all Sheets
    dsVarSheets = dsDoc.GetSheets2
    If IsArray(dsVarSheets) Then
        For index = LBound(dsVarSheets) To UBound(dsVarSheets)
            Set dsSheet = dsVarSheets(index)
            'Get Sheet name
            sheetName = dsSheet.Name
            'Activate Sheet
            dsSheet.Activate
            'Verify if the Sheet was activated
            If dsSheet.IsActive Then
                MsgBox sheetName & " was activated."
            End If
        Next
    End If
```

```
End Sub
```
