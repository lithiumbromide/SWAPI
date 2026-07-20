---
title: "Reorder Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reorder_Features_Example_VB.htm"
---

# Reorder Features Example (VBA)

This example shows how to move a feature to another location in the
FeatureManager design tree of a part.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\clamp2.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Fillet5 moves to the end of the FeatureManager design tree.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the assembly document is used by elsewhere,
 ' do not save any changes when closing the document.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim modelDoc2 As SldWorks.modelDoc2
 Dim modelDocExt As SldWorks.ModelDocExtension
 Dim retVal As Boolean

 Sub Main()

    Set swApp = Application.SldWorks
     Set modelDoc2 = swApp.ActiveDoc
     Set modelDocExt = modelDoc2.Extension
    retVal = modelDocExt.ReorderFeature2("Fillet5", "", swMoveToEnd)
     Debug.Print "Fillet5 moved to the end of the FeatureManager design tree? " & retVal
End Sub
```
