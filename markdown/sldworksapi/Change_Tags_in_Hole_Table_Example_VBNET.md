---
title: "Change Tags in Hole Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Tags_in_Hole_Table_Example_VBNET.htm"
---

# Change Tags in Hole Table Example (VB.NET)

This example shows how to change the tags in a hole table.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a drawing document that contains
'    a hole table named Hole Table1 that has
'    has four columns (TAG, X LOC, Y LOC, and SIZE)
'    and at least five rows.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Disables updating hole table tags.
' 2. Changes tag in column 1, row 2 to Test1.
' 3. Changes tag in column 1, row 5 to Test2.
' 4. Enables updating of hole table and model view
'    and shows new tags.
' 5. Examine the Immediate window and hole table.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public
 Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swHoleTable As HoleTable
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        boolstatus = swModel.Extension.SelectByID2("Hole
 Table1", "HOLETABLE", 0, 0, 0, False, 0, Nothing, 0)
        swHoleTable = swSelMgr.GetSelectedObject6(1,
 -1)

        swHoleTable.EnableUpdate = False 'Disable updating
 hole table tags

        Debug.Print("Original name of tag in column1, row 2:   "
 & swHoleTable.HoleTag(1))
        swHoleTable.HoleTag(1) = "Test1"
        Debug.Print("New name of tag in column1, row 2:        "
 & swHoleTable.HoleTag(1))
        Debug.Print("")
        Debug.Print("Original name of tag in column1, row 5:   "
 & swHoleTable.HoleTag(4))
        swHoleTable.HoleTag(4) = "Test1"  '
 Fails because same name is used in row 2
        swHoleTable.HoleTag(4) = "Test2"
        Debug.Print("New name of tag in column1, row 2:        "
 & swHoleTable.HoleTag(4))

        swHoleTable.EnableUpdate = True 'Enable updating
 hole table tags
    End
 Sub
```

```vb
     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
