---
title: "Hide or Show First Column in Hole Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Column_in_Hole_Table_Example_VBNET.htm"
---

# Hide or Show First Column in Hole Table Example (VB.NET)

This example shows how to hide the first column in a hole table.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\simplehole.slddrw.
' 2. Select the hole table feature in the FeatureManager
'    design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Hides the first column.
' 2. Examine the hole table and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

     Public Sub main()
         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swHoleTableAnnotation As HoleTableAnnotation
         Dim swTableAnnotation As TableAnnotation
         Dim swAnnotation As Annotation
         Dim swHoleTable As HoleTable

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager

         If (swSelMgr.GetSelectedObjectCount = 0 Or Not (swSelMgr.GetSelectedObjectType(1) = swSelectType_e.swSelHOLETABLEFEATS)) Then
             MsgBox("Please select a hole table feature in the FeatureManager design tree.")
             Exit Sub
         End If

         swHoleTable = swSelMgr.GetSelectedObject6(1, -1)
         swHoleTableAnnotation = swHoleTable.GetTableAnnotations(0)
         swTableAnnotation = swHoleTableAnnotation
         swAnnotation = swTableAnnotation.GetAnnotation

         ' If first column hidden, then show it
         If (swTableAnnotation.ColumnHidden(0)) Then
             Debug.Print(" First column hidden before API call: " & swTableAnnotation.ColumnHidden(0))
             swTableAnnotation.ColumnHidden(0) = False
             Debug.Print(" First column hidden after API call:  " & swTableAnnotation.ColumnHidden(0))
         Else
             ' If first column shown, then hide it
             Debug.Print(" First column hidden before API call: " & swTableAnnotation.ColumnHidden(0))
             swTableAnnotation.ColumnHidden(0) = True
             Debug.Print(" First column hidden after API call:  " & swTableAnnotation.ColumnHidden(0))
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

End Class
```
