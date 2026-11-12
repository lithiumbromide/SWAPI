---
title: "Get Features of Multibody Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm"
---

# Get Features of Multibody Sheet Metal Part Example (VBA)

This example shows how to sort the cut-list folder of a multibody sheet metal part.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
' 1. Open  C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\weldment_box3.sldprt.
' 2. Inspect the cut list folder.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number and names of the features in the cut list bodies.
' 2. Sets the cut list sorting options.
' 3. Sorts the cut list.
' 4. Inspect the sorted cut list folder in the Immediate window.
 '--------------------------------------------------------------------------
 Option Explicit
Sub main()

   Dim swApp As SldWorks.SldWorks
   Dim swModel As SldWorks.ModelDoc2
   Dim swFeat As SldWorks.Feature
   Dim swBodyFolder As SldWorks.BodyFolder
   Dim selMgr As SldWorks.SelectionMgr
    Dim swBody As Body2
   Dim Bodies As Variant
   Dim Features As Variant
    Dim CutListSortOptions As SldWorks.CutListSortOptions
   Dim i As Long
   Dim j As Long
   Dim boolstatus As Boolean
   Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
   Set selMgr = swModel.SelectionManager
    boolstatus = swModel.Extension.SelectByID2("Solid Bodies", "BDYFOLDER", 0, 0, 0, False, 0, Nothing, 0)
   Set swFeat = selMgr.GetSelectedObject6(1, -1)
    Set swBodyFolder = swFeat.GetSpecificFeature2
    swBodyFolder.SetAutomaticCutList True
   swBodyFolder.SetAutomaticUpdate False
    Bodies = swBodyFolder.GetBodies
   Debug.Print " Number of bodies: " & swBodyFolder.GetBodyCount
   Debug.Print " Cut list type: " & swBodyFolder.GetCutListType
   Debug.Print " Generate cut list automatically? " & swBodyFolder.GetAutomaticCutList
   Debug.Print " Automatically update cut list? " & swBodyFolder.GetAutomaticUpdate
   For i = 0 To (swBodyFolder.GetBodyCount - 1)
      Set swBody = Bodies(i)
      Features = swBody.GetFeatures
      Debug.Print " Number of features in body #" & i + 1 & ": " & swBody.GetFeatureCount
      For j = 0 To (swBody.GetFeatureCount - 1)
          Debug.Print " Name of feature: " & Features(j).GetTypeName2
      Next j
   Next i

   ' Sort the cut list
   Set CutListSortOptions = swBodyFolder.GetCutListSortOptions
   CutListSortOptions.CollectIdenticalBodies = True
   boolstatus = swBodyFolder.SortCutList(CutListSortOptions, False)

End Sub
```
