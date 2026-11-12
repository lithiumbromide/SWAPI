---
title: "Get Selection Specification Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selection_Specification_Example_VBNET.htm"
---

# Get Selection Specification Example (VB.NET)

This example shows how to get the selection specification of a selected object.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Open a model document that contains at least two features.
 ' 2. Select two features in the FeatureManager design tree.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
  ' 1. Gets the selection specifications of the first and second selections.
 ' 2. Inspect the Immediate window.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim SelMgr As SelectionMgr
     Dim selObject As Feature
     Dim selectByString As String
     Dim objectTypeStr As String
     Dim objectTypeInt As Integer
     Dim X As Double
     Dim Y As Double
     Dim Z As Double

     Sub main()

         Part = swApp.ActiveDoc
         SelMgr = Part.SelectionManager

         ' Get the selection specification of the first selected object
         selObject = SelMgr.GetSelectedObject6(1, -1)
         SelMgr.GetSelectByIdSpecification(selObject, selectByString, objectTypeStr, objectTypeInt)
         Debug.Print("Name of selected feature: " & selectByString)
         Debug.Print("Type of object: " & objectTypeStr)
         Debug.Print("Type of object as defined in swSelectType_e: " & objectTypeInt)

         Debug.Print("")

         ' Get the selection specification of the selected object in position 2 of the selection list
         SelMgr.GetSelectionSpecification(2, selectByString, objectTypeStr, objectTypeInt, X, Y, Z)
         Debug.Print("Name of selected feature: " & selectByString)
         Debug.Print("Type of object: " & objectTypeStr)
         Debug.Print("Type of object as defined in swSelectType_e: " & objectTypeInt)
         Debug.Print("X Coordinate: " & X)
         Debug.Print("Y Coordinate: " & Y)
         Debug.Print("Z Coordinate: " & Z)

     End Sub

     Public swApp As SldWorks

 End Class
```
