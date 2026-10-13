---
title: "Get Components in Each BOM Table Row Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm"
---

# Get Components in Each BOM Table Row Example (VB.NET)

This example shows how to get the components in each row of a BOM table annotation.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
' 2. Make a drawing from the assembly.
' 3. Select Insert > Tables > Bill of Materials.
' 4. Ensure that Parts only in BOM Type is selected.
' 5. Ensure that Display configurations of the same part as separate items
'    in Part Configuration Grouping is selected.
' 6. Click OK.
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub ProcessTableAnn(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swTableAnn As TableAnnotation, ByVal ConfigName As String)

        Dim nNumRow As Long
        Dim J As Long
        Dim I As Long
        Dim ItemNumber As String = Nothing
        Dim PartNumber As String = Nothing
        Dim RowLocked As Boolean
        Dim RowHeight As Double

        Debug.Print("   Table Title: " & swTableAnn.Title)

        nNumRow = swTableAnn.RowCount

        Dim swBOMTableAnn As BomTableAnnotation
        swBOMTableAnn = swTableAnn

        For J = 0 To nNumRow - 1
            RowLocked = swTableAnn.GetLockRowHeight(J)
            RowHeight = swTableAnn.GetRowHeight(J)
            Debug.Print("   Row Number " & J & " (height = " & RowHeight & "; height locked = " & RowLocked & ")")
            Debug.Print("     Component Count: " & swBOMTableAnn.GetComponentsCount2(J, ConfigName, ItemNumber, PartNumber))
            Debug.Print("       Item Number: " & ItemNumber)
            Debug.Print("       Part Number: " & PartNumber)

            Dim vPtArr As Object
            Dim swComp As Object
            Dim pt As Object

            vPtArr = swBOMTableAnn.GetComponents2(J, ConfigName)

            If (Not vPtArr Is Nothing) Then
                For I = 0 To UBound(vPtArr)
                    pt = vPtArr(I)
                    swComp = pt
                    If Not swComp Is Nothing Then
                        Debug.Print("           Component Name: " & swComp.Name2)
                        Debug.Print("           Configuration Name: " & swComp.ReferencedConfiguration)
                        Debug.Print("           Component Path: " & swComp.GetPathName)
                    Else
                        Debug.Print("  Could not get component.")
                    End If
                Next
            End If
        Next J
    End Sub

    Sub ProcessBomFeature(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swBomFeat As BomFeature)

        Dim swFeat As Feature
        Dim vTableArr As Object
        Dim vTable As Object
        Dim vConfigArray As Object
        Dim vConfig As Object
        Dim ConfigName As String
        Dim swTable As TableAnnotation

        swFeat = swBomFeat.GetFeature
        vTableArr = swBomFeat.GetTableAnnotations

        For Each vTable In vTableArr
            swTable = vTable
            vConfigArray = swBomFeat.GetConfigurations(True, True)
            For Each vConfig In vConfigArray
                ConfigName = vConfig
                Debug.Print(" Component for Configuration: " & ConfigName)
                ProcessTableAnn(swApp, swModel, swTable, ConfigName)
            Next vConfig
        Next vTable

    End Sub

    Sub main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim swFeat As Feature
        Dim swBomFeat As BomFeature

        swModel = swApp.ActiveDoc
        swDraw = swModel
        swFeat = swModel.FirstFeature

        Do While Not swFeat Is Nothing
            If "BomFeat" = swFeat.GetTypeName Then
                Debug.Print("Feature Name: " & swFeat.Name)

                swBomFeat = swFeat.GetSpecificFeature2

                ProcessBomFeature(swApp, swModel, swBomFeat)
            End If
            swFeat = swFeat.GetNextFeature
        Loop
    End Sub

    Public swApp As SldWorks

End Class
```
