---
title: "Get Components in Each BOM Table Row Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Each_BOM_Table_Row_VB.htm"
---

# Get Components in Each BOM Table Row Example (VBA)

This example shows how to get the components in each row of a BOM table annotation.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
 ' 2. Make a drawing from the assembly.
 ' 3. Select Insert > Tables > Bill of Materials.
 ' 4. Ensure that Parts only in BOM type is selected.
 ' 5. Ensure that Display configurations of the same part as separate items
 '    in Part configuration Grouping is selected.
 ' 6. Click  OK.
 ' 7. Click anywhere in the drawing to insert the BOM table.
 '
 ' Postconditions:
 ' 1. Gets the Bill of Materials1 feature.
 ' 2. Gets the Default configuration.
 ' 3. Processes the BOM table for the Default configuration.
 ' 4. Examine the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes to it.
 '-----------------------------------------------------------------------------
 Option Explicit
```

```
Sub ProcessTableAnn(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTableAnn As SldWorks.TableAnnotation, ConfigName As String)
```

```
    Dim nNumRow As Long
    Dim nNumColumn As Long
    Dim J As Long
    Dim I As Long
    Dim ItemNumber As String
    Dim PartNumber As String
    Dim RowLocked As Boolean
    Dim RowHeight As Double

    Debug.Print "   Table Title: " & swTableAnn.Title
```

```
    nNumRow = swTableAnn.RowCount
```

```
    Dim swBOMTableAnn As BomTableAnnotation
    Set swBOMTableAnn = swTableAnn
```

```
    For J = 0 To nNumRow - 1
        RowLocked = swTableAnn.GetLockRowHeight(J)
        RowHeight = swTableAnn.GetRowHeight(J)
        Debug.Print "   Row Number " & J & " (height = " & RowHeight & "; height locked = " & RowLocked & ")"
        Debug.Print "     Component Count: " & swBOMTableAnn.GetComponentsCount2(J, ConfigName, ItemNumber, PartNumber)
        Debug.Print "       Item Number: " & ItemNumber
        Debug.Print "       Part Number: " & PartNumber
```

```
        Dim vPtArr As Variant
        Dim swComp As Object
        Dim pt As Object
        Dim compPath As String
```

```
        vPtArr = swBOMTableAnn.GetComponents2(J, ConfigName)
```

```
        If (Not IsEmpty(vPtArr)) Then
            For I = 0 To UBound(vPtArr)
                Set pt = vPtArr(I)
                Set swComp = pt
                If Not swComp Is Nothing Then
                    Debug.Print "           Component Name: " & swComp.Name2
                    Debug.Print "           Configuration Name: " & swComp.ReferencedConfiguration
                    Debug.Print "           Component Path: " & swComp.GetPathName
                Else
                    Debug.Print "  Could not get component."
                End If
            Next
        End If
    Next J
End Sub
```

```
Sub ProcessBomFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swBomFeat As SldWorks.BomFeature)
```

```
    Dim swFeat As SldWorks.Feature
    Dim vTableArr As Variant
    Dim vTable As Variant
    Dim vConfigArray As Variant
    Dim vConfig As Variant
    Dim ConfigName As String
    Dim swTable As SldWorks.TableAnnotation
```

```
    Set swFeat = swBomFeat.GetFeature
    vTableArr = swBomFeat.GetTableAnnotations
```

```
    For Each vTable In vTableArr
        Set swTable = vTable
        vConfigArray = swBomFeat.GetConfigurations(True, True)
        For Each vConfig In vConfigArray
             ConfigName = vConfig
             Debug.Print " Component for configuration: " & ConfigName
             ProcessTableAnn swApp, swModel, swTable, ConfigName
        Next vConfig
    Next vTable
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swFeat As SldWorks.Feature
    Dim swBomFeat As SldWorks.BomFeature
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swFeat = swModel.FirstFeature
```

```
    Do While Not swFeat Is Nothing
        If "BomFeat" = swFeat.GetTypeName Then
            Debug.Print "Feature Name: " & swFeat.Name
            Set swBomFeat = swFeat.GetSpecificFeature2
            ProcessBomFeature swApp, swModel, swBomFeat
        End If
        Set swFeat = swFeat.GetNextFeature
    Loop

End Sub
```
