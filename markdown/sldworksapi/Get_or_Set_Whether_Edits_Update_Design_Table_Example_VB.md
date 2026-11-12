---
title: "Get or Set Whether Edits Update Design Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_or_Set_Whether_Edits_Update_Design_Table_Example_VB.htm"
---

# Get or Set Whether Edits Update Design Table Example (VBA)

This example shows how to get or set whether edits to a design table update the design table.

```
'-----------------------------------
' Preconditions:
' 1. Open a part document that contains a design table.
' 2. Verify that the part document contains a design
'    table by expanding Tables in the ConfigurationManager.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the design table is updatable before
'    running the macro.
' 2. Sets the design table to not updatable if it is
'    updatable or vice versa.
' 3. Examine the Immediate window.
'-----------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDesignTable As SldWorks.DesignTable
Dim boolstatus As Boolean
Dim laststate As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Set swDesignTable = swModel.GetDesignTable()
```

```
    ' Allow changes to the characteristics of the
    ' design table
    swDesignTable.EditFeature
```

```
    ' Get whether design table is updatable
    laststate = swDesignTable.Updatable
    Debug.Print "Design table updatable: " & CStr(laststate)
```

```
    ' If design table is updatable, then set it
    ' to not updatable or vice versa
    swDesignTable.Updatable = Not laststate
```

```
    ' Update this characteristic of the design table
    boolstatus = swDesignTable.UpdateFeature()
```

```
    ' Get whether design table is updatable
    laststate = swDesignTable.Updatable
    Debug.Print "Design table updatable: " & CStr(laststate)
```

```
End Sub
```
