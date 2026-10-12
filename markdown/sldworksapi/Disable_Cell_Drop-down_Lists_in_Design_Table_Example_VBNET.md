---
title: "Disable Cell Drop-down Lists in Design Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm"
---

# Disable Cell Drop-down Lists in Design Table Example (VB.NET)

This example shows how to disable drop-down lists for cells in a design table.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a part that has a design table.
' 2. In the SolidWorks Visual Studio for Applications Tools
'    IDE, click Project > Add Reference > .NET >
'    Microsoft.Office.Interop.Excel > OK.
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDesignTable As DesignTable
        Dim status As Boolean
        Dim myWorksheet As Microsoft.Office.Interop.Excel.Worksheet

        swModel = swApp.ActiveDoc

        'Get and edit design table
        swDesignTable = swModel.GetDesignTable
        myWorksheet = swDesignTable.EditTable2(False)
```

```
        'Allow changes to characteristics of design table
        swDesignTable.EditFeature

        'Disable cell drop-down lists
        status = swDesignTable.EnableCellDropdownLists
        Debug.Print("Current ""Enable cell drop-down lists (may be slower)"" setting: " & status)
        swDesignTable.EnableCellDropdownLists = False
        status = swDesignTable.EnableCellDropdownLists
        Debug.Print("Modified ""Enable cell drop-down lists (may be slower)"" setting: " & status)

        status = swDesignTable.UpdateFeature
        Debug.Print("Design table feature updated? " & status)

        'Update and close design table
        swDesignTable.UpdateTable(swDesignTableUpdateOptions_e.swUpdateDesignTableAll, True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
