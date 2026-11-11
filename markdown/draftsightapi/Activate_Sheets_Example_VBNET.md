---
title: "Activate Sheets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Activate_Sheets_Example_VBNET.htm"
---

# Activate Sheets Example (VB.NET)

This example shows how to activate each Sheet in a drawing.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document with multiple Sheets.
' 5. Start debugging the project.
'
'Postconditions:
' 1. Pops up a message box when a Sheet is activated.
' 2. Click OK to close each message box.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Module Module1
    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Abort any command currently running in
        'DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
            'Activate each Sheet, one by one
            SwitchSheets(dsDoc)
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
    End Sub

    Sub SwitchSheets(ByVal dsDoc As Document)
        Dim dsSheet As Sheet
        Dim dsVarSheets As Object
        Dim index As Integer
        Dim sheetName As String
        'Get all Sheets
        dsVarSheets = dsDoc.GetSheets2
        If IsArray(dsVarSheets) Then
            For index = LBound(dsVarSheets) To UBound(dsVarSheets)
                dsSheet = dsVarSheets(index)
                'Get Sheet name
                sheetName = dsSheet.Name
                'Activate Sheet
                dsSheet.Activate()
                'Verify if the Sheet was activated
                If dsSheet.IsActive Then
                    MsgBox(sheetName & " was activated.")
                End If
            Next
        End If
    End Sub

End Module
```
