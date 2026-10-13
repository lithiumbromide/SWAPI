---
title: "Make Smart Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Smart_Component_Example_VB.htm"
---

# Make Smart Component Example (VBA)

This example shows how to create a Smart Component.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open an assembly containing three components.
' 2. Change names of the selected components in
'    the macro to match the names of the components
'    in your assembly.
'
' Postconditions:
' 1. Creates a Smart Component.
' 2. Expand the first selected component and
'    expand and examine the Smart Feature folder.
'-------------------------------------------------------
Option Explicit
```

```vb
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssembly As SldWorks.AssemblyDoc
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim pCompSmart As Object
 Dim pComp1 As Object
 Dim pComp2 As Object
 Dim pCompArr(1) As Object
 Dim relcomp As Variant
 Dim relfeat As Variant
 Dim boundval As Variant
 Dim boolstatus As Boolean
 Dim retval As Boolean

 Sub main()

     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssembly = swModel
     Set swSelMgr = swModel.SelectionManager
     Set swModelDocExt = swModel.Extension

    ' Select the component that you want to make smart
     boolstatus = swModelDocExt.SelectByID2("C-1@ABC_assembly", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

    ' Select the components that you want to associate with the Smart Component
     boolstatus = swModelDocExt.SelectByID2("B-1@ABC_assembly", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = swModelDocExt.SelectByID2("A-2@ABC_assembly", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

     Set pCompSmart = swSelMgr.GetSelectedObject6(1, 0)
     Set pComp1 = swSelMgr.GetSelectedObject6(2, 0)
     Set pComp2 = swSelMgr.GetSelectedObject6(3, 0)

     Set pCompArr(0) = pComp1
     Set pCompArr(1) = pComp2

     relcomp = pCompArr

     swModel.ClearSelection2 True

     ' Create the Smart Component
     retval = swAssembly.CreateSmartComponent(pCompSmart, (relcomp), (relfeat), False, Nothing, boundval)

 End Sub
```
