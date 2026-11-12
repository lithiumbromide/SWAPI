---
title: "Switch Layouts Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Switch_Layouts_Example_VBA.htm"
---

# Switch Layouts Example (VBA)

This example shows how to switch layouts.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
'Postconditions: Message boxes pop up when a model or sheet
'is activated. Read the text in each message box before clicking
'OK to close it.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
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
        'Activate each layout, one by one
        SwitchLayouts dsDoc
```

```
    Else
        MsgBox "There are no open documents in DraftSight."
    End If
End Sub
```

```
Sub SwitchLayouts(dsDoc As DraftSight.Document)
    Dim dsSheet As DraftSight.Sheet
    Dim dsModel As DraftSight.Model
    Dim dsVarSheets As Variant
    Dim index As Integer
    Dim sheetName As String
```

```
    'Get all sheets
    dsVarSheets = dsDoc.GetSheets
```

```
    If IsArray(dsVarSheets) Then
```

```
        For index = LBound(dsVarSheets) To UBound(dsVarSheets)
```

```
            Set dsSheet = dsVarSheets(index)
```

```
            'Get sheet name
            sheetName = dsSheet.Name
```

```
            'Change sheet name, if it is not a model
            If sheetName <> "Model" Then
```

```
                'Activate sheet
                dsSheet.Activate
```

```
                'Verify if the sheet was activated
                If dsSheet.IsActive Then
                    MsgBox "The sheet " & sheetName & " was activated."
                End If
```

```
            Else
```

```
                'Activate model sheet
                Set dsModel = dsDoc.GetModel
```

```
                If Not dsModel Is Nothing Then
```

```
                    'Activate model sheet
                    dsModel.Activate
```

```
                    'Verify if the sheet was activated
                    If dsModel.IsActive Then
                        MsgBox "The model sheet was activated."
                    End If
```

```
                End If
```

```
            End If
```

```
        Next
```

```
    End If
```

```
End Sub
```
