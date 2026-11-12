---
title: "Create Machining Costing Analysis Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Machining_Costing_Analyses_Example_VBNET.htm"
---

# Create Machining Costing Analysis Example (VB.NET)

This example shows how to create a machining Costing analysis.

```vb
  '-----------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\machined_part.sldprt
 ' 2. Verify that the Costing templates exist by clicking Tools > Options
 '    System Options > File Locations and selecting Costing templates in
 '    Show folders for in SOLIDWORKS Design. Click Cancel to close the dialog.
 ' 3. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
 ' 4. Open the Immediate window.
 ' 5. Run the macro.
 '
 ' Postconditions:
 ' 1. Creates machining Costing analysis, which might
 '    take one or more minutes to complete.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because the part is used elsewhere, do not
' save changes.
 '------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.sldcostingapi
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swCosting As CostManager
         Dim swCostingPart As CostPart
         Dim swCostingBody As CostBody
         Dim swCostingModel As Object
         Dim swCostingAnalysis As CostAnalysis
         Dim swCostingMachining As CostAnalysisMachining
         Dim machiningCostingTemplatePathName As String
         Dim machiningCostingReportTemplateFolderName As String
         Dim nbrMachiningCostingTemplate As Integer
         Dim nbrCommonCostingTemplate As Integer
         Dim commonCostingTemplates As Object
         Dim machiningCostingTemplates As Object
         Dim nbrCostingBodies As Integer
         Dim costingBodies As Object
         Dim costingBodyName As String
         Dim i As Integer
          Dim isBody  As  Boolean
         Dim swCostingFeat As CostFeature
         Dim swCostingNextFeat As CostFeature
         Dim swCostingSubFeat As CostFeature
         Dim swCostingNextSubFeat As CostFeature

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Get Costing templates names
         Debug.Print("Costing template folders:")
         machiningCostingTemplatePathName = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileLocationsCostingTemplates)
         Debug.Print("    Name of Costing template folder: " & machiningCostingTemplatePathName)
         machiningCostingReportTemplateFolderName = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileLocationsCostingReportTemplateFolder)
         Debug.Print("    Name of Costing report template folder: " & machiningCostingReportTemplateFolderName)
         Debug.Print("")

         ' Get CostingManager
         swCosting = swModelDocExt.GetCostingManager
         swCosting.WaitForUIUpdate()

         ' Get the number of templates
         nbrMachiningCostingTemplate = swCosting.GetTemplateCount(swcCostingType_e.swcCostingType_Machining)
         nbrCommonCostingTemplate = swCosting.GetTemplateCount(swcCostingType_e.swcCostingType_Common)

         ' Get names of templates
         machiningCostingTemplates = swCosting.GetTemplatePathnames(swcCostingType_e.swcCostingType_Machining)
         commonCostingTemplates = swCosting.GetTemplatePathnames(swcCostingType_e.swcCostingType_Common)

         ReDim Preserve machiningCostingTemplates(nbrMachiningCostingTemplate)
         ReDim Preserve commonCostingTemplates(nbrCommonCostingTemplate)

         Debug.Print("Costing templates:")

         ' Print names of templates to Immediate window
         For i = 0 To (UBound(machiningCostingTemplates) - 1)
             Debug.Print("    Name of machining Costing template: " & machiningCostingTemplates(i))
         Next i

         Debug.Print("")

         For i = 0 To (UBound(commonCostingTemplates) - 1)
             Debug.Print("    Name of common Costing template: " & commonCostingTemplates(i))
         Next i

         Debug.Print("")

         ' Get Costing part
         swCostingModel = swCosting.CostingModel
         swCostingPart = swCostingModel

         ' Create common Costing analysis
         swCostingAnalysis = swCostingPart.CreateCostAnalysis("c:\program files\solidworks corp\solidworks\lang\english\costing templates\multibodytemplate_default(englishstandard).sldctc")

         ' Get common Costing analysis data
         Debug.Print("Common Costing analysis data:")
         Debug.Print("    Template name:  " & swCostingAnalysis.costingTemplateName)
         Debug.Print("    Currency code: " & swCostingAnalysis.CurrencyCode)
         Debug.Print("    Currency name: " & swCostingAnalysis.CurrencyName)
         Debug.Print("    Currency separator: " & swCostingAnalysis.CurrencySeparator)
         Debug.Print("    Total manufacturing cost: " & swCostingAnalysis.GetManufacturingCost)
         Debug.Print("    Material costs: " & swCostingAnalysis.GetMaterialCost)
         Debug.Print("    Setup cost: " & swCostingAnalysis.GetSetupCost)
         Debug.Print("    Total cost to charge: " & swCostingAnalysis.GetTotalCostToCharge)
         Debug.Print("    Total cost to manufacture: " & swCostingAnalysis.GetTotalCostToManufacture)
         Debug.Print("    Lot size: " & swCostingAnalysis.LotSize)
         Debug.Print("    Total quantity: " & swCostingAnalysis.TotalQuantity)
         Debug.Print("")

         ' Get Costing bodies
         nbrCostingBodies = swCostingPart.GetBodyCount
         isBody =  False
         If (nbrCostingBodies > 0) Then
             Debug.Print("Costing bodies:")
             Debug.Print("    Number of Costing bodies: " & nbrCostingBodies)
             costingBodies = swCostingPart.GetBodies
             For i = 0 To (nbrCostingBodies - 1)
                 swCostingBody = costingBodies(i)
                 costingBodyName = swCostingBody.GetName
                 Debug.Print("    Name of Costing body: " & costingBodyName)
                 ' Make sure body is machining body
                 If (swCostingBody.GetBodyType = swcBodyType_e.swcBodyType_Machined) Then
                     isBody = True
                     ' Determine analysis status of Costing body
                     Select Case swCostingBody.BodyStatus
                         Case swcBodyStatus_e.swcBodyStatus_NotAnalysed
                             ' Create Costing analysis
                             swCostingAnalysis = swCostingBody.CreateCostAnalysis("c:\program files\solidworks corp\solidworks\lang\english\costing templates\machiningtemplate_default(englishstandard).sldcts")
                             Debug.Print("    Creating machining Costing analysis for: " & swCostingBody.GetName)
                         Case swcBodyStatus_e.swcBodyStatus_Analysed
                             ' Get Costing analysis
                             swCostingAnalysis = swCostingBody.GetCostAnalysis
                             Debug.Print("    Getting machining Costing analysis for: " & swCostingBody.GetName)
                         Case swcBodyStatus_e.swcBodyStatus_Excluded
                             ' Body excluded from Costing analysis
                             Debug.Print("    Excluded from machining Costing analysis: " & swCostingBody.GetName)
                         Case swcBodyStatus_e.swcBodyStatus_AssignedCustomCost
                             ' Body has an assigned custom Cost
                             Debug.Print("    Custom cost assigned: " & swCostingBody.GetName)
                     End Select

                     Debug.Print("")

                 End If
             Next i
         End If

          If  Not isBody  Then
             Debug.Print("")
             Debug.Print("No bodies in part! Exiting macro.")
              Exit  Sub
         End  If

         ' Get machining Costing Analysis data
         swCostingMachining = swCostingAnalysis.GetSpecificAnalysis
         Debug.Print("Machining Costing analysis: ")
         Debug.Print("    Current material: " & swCostingMachining.CurrentMaterial)
         Debug.Print("    Current material class: " & swCostingMachining.CurrentMaterialClass)
         Debug.Print("    Current plate thickness: " & swCostingMachining.CurrentPlateThickness)

         Debug.Print("")

         ' Get Costing features
         Debug.Print("Costing features:")
         swCostingFeat = swCostingAnalysis.GetFirstCostFeature
         While Not swCostingFeat Is Nothing
             Debug.Print("    Feature: " & swCostingFeat.Name)
             Debug.Print("      Type: " & swCostingFeat.GetType)
             Debug.Print("        Setup related: " & swCostingFeat.IsSetup)
             Debug.Print("        Overridden: " & swCostingFeat.IsOverridden)
             Debug.Print("        Combined cost: " & swCostingFeat.CombinedCost)
             Debug.Print("        Combined time: " & swCostingFeat.CombinedTime)

             swCostingSubFeat = swCostingFeat.GetFirstSubFeature
             While Not swCostingSubFeat Is Nothing
                 Debug.Print("      Subfeature: " & swCostingSubFeat.Name)
                 Debug.Print("        Type: " & swCostingSubFeat.GetType)
                 Debug.Print("          Setup related: " & swCostingSubFeat.IsSetup)
                 Debug.Print("          Overridden: " & swCostingSubFeat.IsOverridden)
                 Debug.Print("          Combined cost: " & swCostingSubFeat.CombinedCost)
                 Debug.Print("          Combined time: " & swCostingSubFeat.CombinedTime)
                 swCostingNextSubFeat = swCostingSubFeat.GetNextFeature
                 swCostingSubFeat = Nothing
                 swCostingSubFeat = swCostingNextSubFeat
                 swCostingNextSubFeat = Nothing
             End While
             swCostingNextFeat = swCostingFeat.GetNextFeature
             swCostingFeat = Nothing
             swCostingFeat = swCostingNextFeat
             swCostingNextFeat = Nothing
         End While

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
