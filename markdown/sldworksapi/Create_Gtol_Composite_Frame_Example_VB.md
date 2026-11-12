---
title: "Create GTol Composite Frame Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Gtol_Composite_Frame_Example_VB.htm"
---

# Create GTol Composite Frame Example (VBA)

This example shows how to create a composite frame for a geometric tolerance symbol.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a document with a geometric tolerance (GTol) whose first two
'    frames have the same symbol.
' 2. Select the GTol in the graphics area.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a composite frame for the symbol in the graphics area.
' 2. Examine the graphics area and Immediate window.
'----------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim selMgr As SldWorks.SelectionMgr
 Dim Part As SldWorks.ModelDoc2
 Dim gtol As SldWorks.gtol

 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
     Set selMgr = Part.SelectionManager
     Set gtol = selMgr.GetSelectedObject6(1, -1)

    gtol.SetCompositeFrame2 True, 1
     Debug.Print "Frame 1 is part of a GTol composite frame? " & gtol.GetCompositeFrame2(1)

End Sub
```
