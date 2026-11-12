---
title: "Switch Edit Context Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Switch_Edit_Context_Example_VBNET.htm"
---

# Switch Edit Context Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim assem As AssemblyDoc
     Dim Part As ModelDoc2
     Dim boolstatus As Boolean

     Sub main()

         assem = swApp.ActiveDoc
         Part = assem

         boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         assem.FixComponent()
         ' Part1^Assem2-1@assem2 is now fixed
         Stop

         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         assem.UnfixComponent()
         ' Part1^Assem2-1@assem2 is now floating
         Stop

         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Part1^Assem2-1@assem2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         assem.EditPart2(True, True, 1)
         ' Part1^Assem2-1@assem2 is being edited in the context of the assembly
         Stop

         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("assem2.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         assem.EditAssembly()
         ' The assembly is being edited

     End Sub

     Public swApp As SldWorks

 End  Class
```
