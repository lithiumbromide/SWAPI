---
title: "Delete Instances and Dimensions in Variable Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm"
---

# Delete Instances and Dimensions in Variable Pattern Feature Example (VBA)

This example shows how to:

- delete instances in a variable pattern feature.
- add and delete dimensions in the pattern table in a variable pattern table.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part and selects the variable pattern feature.
' 2. Accesses the variable pattern feature.
' 3. Deletes the last and fourth instance from the pattern table
'    and pattern.
' 4. Gets the number and names of the controlling dimensions.
' 5. Selects and adds two dimensions to the pattern table and
'    deletes the second dimension from the pattern table.
' 6. Rolls forward the modified variable pattern feature.
' 7. Examine the graphics area and Immediate window.
'
' NOTE: Because the part used is elsewhere, do not save changes.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swDimensionDrivenTablePatternFeat As SldWorks.DimPatternFeatureData
Dim swDisplayDimension as SldWorks.DisplayDimension
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim dimNbr As Long
Dim i As Long
Dim controllingDimNames() As String
Dim controllingDimName As String

Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part and select the variable pattern feature
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\bottle.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swDimensionDrivenTablePatternFeat = swFeature.GetDefinition
```

```
    'Roll back and access the variable pattern feature
    status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, Nothing)
```

```
    'Delete the last instance of the variable pattern in the pattern table and pattern
    status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(-1)
    Debug.Print "Last instance of variable pattern deleted from pattern table? " & status
```

```
    'Delete another instance of the variable pattern in the pattern table and pattern
    status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(3)
    Debug.Print "Fourth instance of variable pattern deleted from pattern table? " & status
```

```
    'Get the number and names of the controlling dimensions
    dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount
    Debug.Print ("Number of controlling dimensions: " & dimNbr)
    Debug.Print ("  Controlling dimension names: ")
    ReDim Preserve controllingDimNames(dimNbr)
    For i = 0 To dimNbr - 1
        controllingDimNames(i) = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i)
        controllingDimName = controllingDimNames(i)
        Debug.Print ("     " & controllingDimName)
    Next i
```

```
    'Select two display dimensions and add them to the pattern table
    status = swModelDocExt.SelectByID2("D1@Sketch2@bottle.SLDPRT", "DIMENSION", 1.76517231321772E-02, 1.49650532369545E-02, -2.43235746513165E-02, False, 0, Nothing, 0)
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    status = swDimensionDrivenTablePatternFeat.AddDimension
    If status Then
        Debug.Print "Added " & swDisplayDimension.GetNameForSelection & " to pattern table"
    End If
```

```
    swModel.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("D2@Sketch2@bottle.SLDPRT", "DIMENSION", 0.019517663324148, 2.97942417761803E-02, -2.37034236540374E-02, False, 0, Nothing, 0)
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    status = swDimensionDrivenTablePatternFeat.AddDimension
    If status Then
        Debug.Print "Added " & swDisplayDimension.GetNameForSelection & " to pattern table"
    End If
```

```
    'Delete the just-added display dimension from the pattern table
    status = swDimensionDrivenTablePatternFeat.DeleteDimension(swDisplayDimension.GetNameForSelection)
    If status Then
        Debug.Print "  Deleted " & swDisplayDimension.GetNameForSelection & " from pattern table"
    End If
```

```
    swDimensionDrivenTablePatternFeat.PropagateVisualProperties = True
```

```
    'Roll forward the variable pattern feature
    swFeature.ModifyDefinition swDimensionDrivenTablePatternFeat, swModel, Nothing
```

```
End Sub
```
