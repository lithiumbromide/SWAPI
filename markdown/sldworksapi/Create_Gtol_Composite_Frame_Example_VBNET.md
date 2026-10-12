---
title: "Create GTol Composite Frame Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Gtol_Composite_Frame_Example_VBNET.htm"
---

# Create GTol Composite Frame Example (VB.NET)

This example shows how to create a composite frame for a geometric tolerance symbol.

```vb
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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim selMgr As SelectionMgr
     Dim Part As ModelDoc2
     Dim gtol As Gtol

     Sub main()

         Part = swApp.ActiveDoc
         selMgr = Part.SelectionManager
         gtol = selMgr.GetSelectedObject6(1, -1)

         gtol.SetCompositeFrame2(True, 1)
         Debug.Print("Frame 1 is part of a GTol composite frame? " & gtol.GetCompositeFrame2(1))

     End Sub

     Public swApp As SldWorks

 End  Class
```
