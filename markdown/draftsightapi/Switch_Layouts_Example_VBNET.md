---
title: "Switch Layouts Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Switch_Layouts_Example_VBNET.htm"
---

# Switch Layouts Example (VB.NET)

This example shows how to switch layouts.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
'Postconditions: Message boxes pop up when a model or sheet
'is activated. Read the text in each message box before clicking
'OK to close it.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
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
            'Activate each layout, one by one
            SwitchLayouts(dsDoc)
```

```
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
    End Sub
    Sub SwitchLayouts(ByVal dsDoc As Document)
        Dim dsSheet As Sheet
        Dim dsModel As Model
        Dim dsVarSheets As Object
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
                dsSheet = dsVarSheets(index)
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
                    dsSheet.Activate()
```

```
                    'Verify if the sheet was activated
                    If dsSheet.IsActive Then
                        MsgBox("The sheet " & sheetName & " was activated.")
                    End If
```

```
                Else
```

```
                    'Activate model sheet
                    dsModel = dsDoc.GetModel
```

```
                    If Not dsModel Is Nothing Then
```

```
                        'Activate model sheet
                        dsModel.Activate()
```

```
                        'Verify if the sheet was activated
                        If dsModel.IsActive Then
                            MsgBox("The model sheet was activated.")
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

```
End Module
```
