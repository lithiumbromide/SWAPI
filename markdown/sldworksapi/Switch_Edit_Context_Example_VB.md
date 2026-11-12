---
title: "Switch Edit Context Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Edit_Context_Example_VB.htm"
---

# Switch Edit Context Example (VBA)

This example shows how to switch back and forth between assembly and part when editing. It also shows how to fix and float an assembly component.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\assem2.sldasm
 ' 2. Press F5 after each macro pause.
 '
 ' Postconditions: None
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.AssemblyDoc
 Dim boolstatus As Boolean
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Part.FixComponent
     ' Part1^Assem2-1@assem2 is now fixed
     Stop

    Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Part.UnfixComponent
     ' Part1^Assem2-1@assem2 is now floating
     Stop

    Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditPart2 True, True, 1
     ' Part1^Assem2-1@assem2 is being edited in the context of the assembly
     Stop

    Part.ClearSelection2 True
     boolstatus = Part.Extension.SelectByID2("assem2.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Part.EditAssembly
     ' The assembly is being edited

End Sub
```
