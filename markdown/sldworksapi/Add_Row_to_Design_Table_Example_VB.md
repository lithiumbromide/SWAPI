---
title: "Add Row to Design Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Row_to_Design_Table_Example_VB.htm"
---

# Add Row to Design Table Example (VBA)

This example shows how to add a row to a design table. This example also adds a configuration to the part document.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a design table.
' 2. Select the design table on the ConfigurationManager
'    tab (expand Tables and select Design Table).
'
' Postconditions: Adds a row and a configuration
' named 190 to the part document.
'-------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDesignTable As SldWorks.DesignTable
    Dim cells(1) As String
    Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDesignTable = swModel.GetDesignTable

    ' Name of configuration for newly created row
    cells(0) = "190"
```

```
    ' Data for Column B of newly created row
    cells(1) = "S"
```

```
    swDesignTable.EditTable
    boolstatus = swDesignTable.AddRow((cells))
    boolstatus = swDesignTable.UpdateTable(SwConst.swDesignTableUpdateOptions_e.swUpdateDesignTableAll, True)
```

```
End Sub
```
