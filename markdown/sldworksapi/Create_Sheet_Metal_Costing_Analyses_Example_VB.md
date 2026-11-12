---
title: "Create Sheet Metal Costing Analysis Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sheet_Metal_Costing_Analyses_Example_VB.htm"
---

# Create Sheet Metal Costing Analysis Example (VBA)

This example shows how to create a sheet metal Costing analysis.

```
'-----------------------------------------------
' Preconditions:
' 1. Open:
'    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\sheet_metal_part.sldprt
' 2. Verify that the Costing templates exist by clicking Tools > Options >
'    System Options > File Locations and selecting Costing templates in
'    Show folders for in SOLIDWORKS Design. Click Cancel to close the dialog.
' 3. Add a reference to SldCosting API 20nn Type Library.
' 4. Open the Immediate window.
' 5. Run the macro.
'
' Postconditions:
' 1. If prompted to save a temporary template with the costing data,
'    click Yes, browse to the folder where to save the temporary
'    template, type the name of the temporary template in File name,
'    and click Save.
' 2. Creates a sheet metal analysis, which might
'    take one or more minutes to complete.
' 3. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swCosting As SldCostingAPI.CostManager
Dim swCostingPart As SldCostingAPI.CostPart
Dim swCostingBody As SldCostingAPI.CostBody
Dim swCostingModel As Object
Dim swCostingAnalysis As SldCostingAPI.CostAnalysis
Dim swCostingSheetMetal As SldCostingAPI.CostAnalysisSheetMetal
Dim sheetmetalCostingTemplatePathName As String
Dim sheetmetalCostingReportTemplateFolderName As String
Dim nbrSheetmetalCostingTemplate As Long
Dim nbrcommonCostingTemplate As Long
Dim commonCostingTemplates As Variant
Dim sheetmetalCostingTemplates As Variant
Dim nbrCostingBodies As Long
Dim costingBodies As Variant
Dim costingBodyName As String
Dim i As Long
Dim isSheetMetalBody As Boolean
Dim swCostingFeat As SldCostingAPI.CostFeature
Dim swCostingNextFeat As SldCostingAPI.CostFeature
Dim swCostingSubFeat As SldCostingAPI.CostFeature
Dim swCostingNextSubFeat As SldCostingAPI.CostFeature
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
```

```
' Get Costing templates names
Debug.Print ("Costing template folders:")
sheetmetalCostingTemplatePathName = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileLocationsCostingTemplates)
Debug.Print "    Name of Costing template folder: " & sheetmetalCostingTemplatePathName
sheetmetalCostingReportTemplateFolderName = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileLocationsCostingReportTemplateFolder)
Debug.Print "    Name of Costing report template folder: " & sheetmetalCostingReportTemplateFolderName
Debug.Print ""
```

```
' Get CostingManager
Set swCosting = swModelDocExt.GetCostingManager
swCosting.WaitForUIUpdate
```

```
' Get the number of templates
nbrSheetmetalCostingTemplate = swCosting.GetTemplateCount(swcCostingType_e.swcCostingType_SheetMetal)
nbrcommonCostingTemplate = swCosting.GetTemplateCount(swcCostingType_e.swcCostingType_Common)
```

```
' Get names of templates
sheetmetalCostingTemplates = swCosting.GetTemplatePathnames(swcCostingType_e.swcCostingType_SheetMetal)
commonCostingTemplates = swCosting.GetTemplatePathnames(swcCostingType_e.swcCostingType_Common)
```

```
ReDim Preserve sheetmetalCostingTemplates(nbrSheetmetalCostingTemplate)
ReDim Preserve commonCostingTemplates(nbrcommonCostingTemplate)
```

```
Debug.Print ("Costing templates:")
```

```
' Print names of templates to Immediate window
For i = 0 To (UBound(sheetmetalCostingTemplates) - 1)
    Debug.Print "    Name of sheet metal Costing template: " & sheetmetalCostingTemplates(i)
Next i
```

```
Debug.Print ""
```

```
For i = 0 To (UBound(commonCostingTemplates) - 1)
    Debug.Print "    Name of common Costing template: " & commonCostingTemplates(i)
Next i
```

```
Debug.Print ""
```

```
' Get Costing part
Set swCostingModel = swCosting.CostingModel
Set swCostingPart = swCostingModel
```

```
' Create common Costing analysis
Set swCostingAnalysis = swCostingPart.CreateCostAnalysis("c:\program files\solidworks corp\solidworks\lang\english\costing templates\multibodytemplate_default(englishstandard).sldctc")
```

```
' Get common Costing analysis data
Debug.Print ("Common Costing analysis data:")
Debug.Print ("    Template name:  " & swCostingAnalysis.costingTemplateName)
Debug.Print ("    Currency code: " & swCostingAnalysis.CurrencyCode)
Debug.Print ("    Currency name: " & swCostingAnalysis.CurrencyName)
Debug.Print ("    Currency separator: " & swCostingAnalysis.CurrencySeparator)
Debug.Print ("    Total manufacturing cost: " & swCostingAnalysis.GetManufacturingCost)
Debug.Print ("    Material costs: " & swCostingAnalysis.GetMaterialCost)
Debug.Print ("    Setup cost: " & swCostingAnalysis.GetSetupCost)
Debug.Print ("    Total cost to charge: " & swCostingAnalysis.GetTotalCostToCharge)
Debug.Print ("    Total cost to manufacture: " & swCostingAnalysis.GetTotalCostToManufacture)
Debug.Print ("    Lot size: " & swCostingAnalysis.LotSize)
Debug.Print ("    Total quantity: " & swCostingAnalysis.TotalQuantity)
Debug.Print ""
```

```
' Get Costing bodies
nbrCostingBodies = swCostingPart.GetBodyCount
If (nbrCostingBodies > 0) Then
    Debug.Print "Costing bodies:"
    Debug.Print ("    Number of Costing bodies: " & nbrCostingBodies)
    costingBodies = swCostingPart.GetBodies
        For i = 0 To (nbrCostingBodies - 1)
            Set swCostingBody = costingBodies(i)
            costingBodyName = swCostingBody.GetName
            Debug.Print ("    Name of Costing body: " & costingBodyName)
            isSheetMetalBody = False
            ' Make sure body is sheet metal
            If (swCostingBody.GetBodyType = swcBodyType_e.swcBodyType_SheetMetal) Then
                isSheetMetalBody = True
                ' Determine analysis status of Costing body
                Select Case swCostingBody.BodyStatus
                    Case swcBodyStatus_e.swcBodyStatus_NotAnalysed
                        ' Create Costing analysis
                        Set swCostingAnalysis = swCostingBody.CreateCostAnalysis("c:\program files\solidworks corp\solidworks\lang\english\costing templates\sheetmetaltemplate_default(englishstandard).sldcts")
                        Debug.Print ("    Creating sheet metal Costing analysis for: " & swCostingBody.GetName)
                    Case swcBodyStatus_e.swcBodyStatus_Analysed
                        ' Get Costing analysis
                        Set swCostingAnalysis = swCostingBody.GetCostAnalysis
                        Debug.Print ("    Getting sheet metal Costing analysis for: " & swCostingBody.GetName)
                    Case swcBodyStatus_e.swcBodyStatus_Excluded
                        ' Body excluded from Costing analysis
                        Debug.Print ("    Excluded from sheet metal Costing analysis: " & swCostingBody.GetName)
                    Case swcBodyStatus_e.swcBodyStatus_AssignedCustomCost
                        ' Body has an assigned custom Cost
                        Debug.Print ("    Custom cost assigned: " & swCostingBody.GetName)
                End Select
```

```
                Debug.Print ""
```

```
            End If
        Next i
```

```
        If Not isSheetMetalBody Then
            Debug.Print ""
            Debug.Print "No sheet metal bodies in part! Exiting macro."
            Exit Sub
        End If
End If
```

```
' Get sheet metal Costing Analysis data
Set swCostingSheetMetal = swCostingAnalysis.GetSpecificAnalysis
Debug.Print "Sheet metal Costing analysis: "
Debug.Print ("    Current material: " & swCostingSheetMetal.CurrentMaterial)
Debug.Print ("    Current material class: " & swCostingSheetMetal.CurrentMaterialClass)
Debug.Print ("    Current thickness: " & swCostingSheetMetal.CurrentThickness)
Debug.Print ("    Material cost: " & swCostingSheetMetal.MaterialCost)
Debug.Print ("    Material cost from template: " & swCostingSheetMetal.MaterialCostFromTemplate)
Debug.Print ("    Type of blank size: " & swCostingSheetMetal.BlankSizeType)
Debug.Print ("    Blank area from model: " & swCostingSheetMetal.BlankAreaFromModel)
Debug.Print ("    Blank area, include any margins, from model: " & swCostingSheetMetal.FinalAreaFromModel)
```

```
Debug.Print ("")
```

```
' Get Costing features
Debug.Print "Costing features:"
Set swCostingFeat = swCostingAnalysis.GetFirstCostFeature
While Not swCostingFeat Is Nothing
    Debug.Print ("    Feature: " & swCostingFeat.Name)
    Debug.Print ("      Type: " & swCostingFeat.GetType)
    Debug.Print ("        Setup related: " & swCostingFeat.IsSetup)
    Debug.Print ("        Overridden: " & swCostingFeat.IsOverridden)
    Debug.Print ("        Combined cost: " & swCostingFeat.CombinedCost)
    Debug.Print ("        Combined time: " & swCostingFeat.CombinedTime)
```

```
    Set swCostingSubFeat = swCostingFeat.GetFirstSubFeature
    While Not swCostingSubFeat Is Nothing
        Debug.Print ("      Subfeature: " & swCostingSubFeat.Name)
        Debug.Print ("        Type: " & swCostingSubFeat.GetType)
        Debug.Print ("          Setup related: " & swCostingSubFeat.IsSetup)
        Debug.Print ("          Overridden: " & swCostingSubFeat.IsOverridden)
        Debug.Print ("          Combined cost: " & swCostingSubFeat.CombinedCost)
        Debug.Print ("          Combined time: " & swCostingSubFeat.CombinedTime)
        Set swCostingNextSubFeat = swCostingSubFeat.GetNextFeature
        Set swCostingSubFeat = Nothing
        Set swCostingSubFeat = swCostingNextSubFeat
        Set swCostingNextSubFeat = Nothing
    Wend
    Set swCostingNextFeat = swCostingFeat.GetNextFeature
    Set swCostingFeat = Nothing
    Set swCostingFeat = swCostingNextFeat
    Set swCostingNextFeat = Nothing
Wend
```

```
End Sub
```
