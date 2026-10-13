---
title: "Export BOM's Second Column to BOM Table Area Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm"
---

# Export BOM's Second Column to BOM Table Area Example (VB.NET)

This example shows how to export a BOM's second column to a BOM Table Area of a SOLIDWORKS MBD 3D PDF.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified assembly,
'    * specified SOLIDWORKS MBD 3D PDF theme, and
'    * c:\temp exist.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Inserts an indented BOM table in the assembly.
' 2. Gets the title of the second column in the BOM table
'    to export that column to the SOLIDWORKS MBD 3D PDF.
' 3. Gets the name of the BOM to map to the SOLIDWORKS
'    MBD 3D PDF.
' 4. Gets the SOLIDWORKS MBD 3D PDF data object.
'    a. Sets to display the SOLIDWORKS MBD 3D PDF after
'       publishing it.
'    b. Sets the path for the SOLIDWORKS MBD 3D PDF.
'    c. Sets the SOLIDWORKS MBD 3D PDF theme.
'    d. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
'    e. Maps the BOM and exports its second column to a BOM
'       Table Area in the SOLIDWORKS MBD 3D PDF.
'    f. Publishes and displays the SOLIDWORKS MBD 3D PDF.
' 5. Examine c:\temp\MBDAssembly1.PDF and the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swBOMAnnotation As BomTableAnnotation
        Dim swTableAnnotation As TableAnnotation
        Dim swBOMFeature As BomFeature
        Dim swMBDPdfData As MBD3DPdfData
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim bomType As Integer
        Dim tableTemplate As String
        Dim columnNames(0) As String
        Dim columns() As Object
        Dim BOMTableName As String
        Dim standardViews As Object
        Dim viewIDs(2) As Integer
        Dim nbrBOMTableAreas As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        ' Insert indented BOM table in assembly
        bomType = swBomType_e.swBomType_Indented
        tableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
        swBOMAnnotation = swModelDocExt.InsertBomTable3(tableTemplate, 0, 1, bomType, "Default", False, swNumberingType_e.swNumberingType_Detailed, True)

        ' Get title of second column in BOM table to export to SOLIDWORKS MBD 3D PDF
        swTableAnnotation = swBOMAnnotation
        columnNames(0) = swTableAnnotation.GetColumnTitle(1)
        Debug.Print("Title of second column to export to SOLIDWORKS MBD 3D PDF: " & columnNames(0))
        columns = columnNames

        ' Get name of BOM to map to SOLIDWORKS MBD 3D PDF
        swBOMFeature = swBOMAnnotation.BomFeature
        BOMTableName = swBOMFeature.Name
        Debug.Print("Name of BOM to map to SOLIDWORKS MBD 3D PDF: " & BOMTableName)

        ' Get MBD3PdfData object
        swMBDPdfData = swModelDocExt.GetMBD3DPdfData

        ' Set to display SOLIDWORKS MBD 3D PDF
        swMBDPdfData.ViewPdfAfterSaving = True

        ' Set path for SOLIDWORKS MBD 3D PDF
        swMBDPdfData.FilePath = "c:\temp\MBDAssembly1.PDF"

        ' Set SOLIDWORKS MBD 3D PDF theme
        swMBDPdfData.ThemeName = "c:\program files\solidworks corp\solidworks\data\themes\simple assembly (a4, landscape)\theme.xml"

        ' Set standard views for SOLIDWORKS MBD 3D PDF
        viewIDs(0) = swStandardViews_e.swFrontView
        viewIDs(1) = swStandardViews_e.swTopView
        viewIDs(2) = swStandardViews_e.swDimetricView
        standardViews = viewIDs
        swMBDPdfData.SetStandardViews(standardViews)

        ' Map BOM and export its second column to a BOM Table Area
        nbrBOMTableAreas = swMBDPdfData.GetBomAreaCount
        If nbrBOMTableAreas > 0 Then
            swMBDPdfData.SetBomTable(0, BOMTableName, columns)
        End If

        ' Publish SOLIDWORKS MBD 3D PDF
        swModelDocExt.PublishTo3DPDF(swMBDPdfData)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
