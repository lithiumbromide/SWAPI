---
title: "Reorder Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reorder_Features_Example_VBNET.htm"
---

# Reorder Features Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim modelDoc2 As ModelDoc2
     Dim featureMgr As FeatureManager
     Dim modelDocExt As ModelDocExtension
     Dim retVal As Boolean
     Sub Main()

         modelDoc2 = swApp.ActiveDoc
         modelDocExt = modelDoc2.Extension

         retVal = modelDocExt.ReorderFeature2("Fillet5", "", swMoveLocation_e.swMoveToEnd)
         Debug.Print("Fillet5 moved to the end of the FeatureManager design tree? " & retVal)

     End Sub

     Public swApp As SldWorks

 End  Class
```
