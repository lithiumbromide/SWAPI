---
title: "Disable Cell Drop-down Lists in Design Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm"
---

# Disable Cell Drop-down Lists in Design Table Example (VBA)

This example shows how to disable drop-down lists for cells in a design table.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a part that has a design table.
' 2. In the Microsoft Visual Basic for Applications IDE, click
'    Tools > References > Microsoft Excel release Object Library > OK.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets and edits the design table.
' 2. Disables drop-down lists for cells in the design table.
' 3. Updates and closes the design table.
' 4. Examine the Immediate window.
'
' NOTE: You can also expand Tables on the ConfigurationManager
' tab, right-click Design Table, and click Edit Feature to
' verify that Enable cell drop-down lists (may be slower)
' is not selected.
'------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDesignTable As SldWorks.DesignTable
    Dim status As Boolean
    Dim myWorksheet As Excel.worksheet
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Get and edit design table
    Set swDesignTable = swModel.GetDesignTable
    Set myWorksheet = swDesignTable.EditTable2(False)
```

```
    'Allow changes to characteristics of design table
    swDesignTable.EditFeature
```

```
    'Disable cell drop-down lists
    status = swDesignTable.EnableCellDropdownLists
    Debug.Print "Current ""Enable cell drop-down lists (may be slower)"" setting: " & status
    swDesignTable.EnableCellDropdownLists = False
    status = swDesignTable.EnableCellDropdownLists
    Debug.Print "Modified ""Enable cell drop-down lists (may be slower)"" setting: " & status
```

```
    status = swDesignTable.UpdateFeature
    Debug.Print "Design table feature updated? " & status
```

```
    'Update and close design table
    swDesignTable.UpdateTable swDesignTableUpdateOptions_e.swUpdateDesignTableAll, True
```

```
End Sub
```
