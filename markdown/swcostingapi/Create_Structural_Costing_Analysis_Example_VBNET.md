---
title: "Create Structural Costing Analysis Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_Structural_Costing_Analysis_Example_VBNET.htm"
---

# Create Structural Costing Analysis Example (VB.NET)

This example shows how to create a structural Costing analysis of a weldment part.

```
'------------------------------------------------
' Preconditions:
' 1. Specified part template exists.
' 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Creates a weldment part.
' 2. Gets the CostingManager.
' 3. Gets the Costing part.
' 4. Sets the Costing manufacturing method
'    to structural and gets the Costing body.
' 5. Gets the common Costing analysis and the
'    structural Costing analysis.
' 6. Gets the material classes from the Costing template
'    and sets the material class.
' 7. Gets the material names from the Costing template
'    and sets the material for the material class.
' 8. Sets and gets structural Costing analysis
'    parameters.
' 9. Gets the total manufacturing cost.
'10. Examine the Immediate window to see the
'    results of steps 6 through 9.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.sldcostingapi
Imports System.Runtime.InteropServices
Imports System.Diagnostics
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swFeatMgr As FeatureManager
        Dim swSelMgr As SelectionMgr
        Dim swcCostMgr As CostManager
        Dim swcCostPart As CostPart
        Dim swcCostBody As CostBody
        Dim swcCostAnalysis As CostAnalysis
        Dim swcStructuralAnalysis As CostAnalysisStructural
        Dim swFeat As Object
        Dim sketchLines As Object
        Dim groupArray(0) As StructuralMemberGroup
        Dim group1 As StructuralMemberGroup
        Dim segment1(0) As SketchLine
        Dim segmentArray1(0) As SketchLine
        Dim status As Boolean
        Dim totalCost As Double
        Dim templateName As String
        Dim materialClassCount As Integer
        Dim materialClasses As Object
        Dim materialCount As Integer
        Dim materials As Object
        Dim i As Integer
        Dim costMethod As Integer

        'Open new part
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

        'Sketch a rectangle
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        swSketchMgr = swModel.SketchManager
        sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0712674458144988, -0.0441036883594848, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Create a weldment feature
        swFeatMgr = swModel.FeatureManager
        swFeat = swFeatMgr.InsertWeldmentFeature()

        'Create a structural member
        status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, -0.00830721773633059, 0, True, 0, Nothing, 0)
        group1 = swFeatMgr.CreateStructuralMemberGroup()
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, 0.334864850338306, 0.393154025912395, True, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        segment1(0) = swSelMgr.GetSelectedObject6(1, 0)
        group1.Segments = (segment1)
        group1.ApplyCornerTreatment = True
        group1.CornerTreatmentType = 1
        group1.GapWithinGroup = 0
        group1.GapForOtherGroups = 0
        group1.Angle = 0
        groupArray(0) = group1
        swFeat = swFeatMgr.InsertStructuralWeldment4("c:\program files\solidworks corp\solidworks\lang\english\weldment profiles\ansi inch\rectangular tube\3 x 2 x 0.25.sldlfp", 1, True, (groupArray))
        swModel.ClearSelection2(True)

        'Get CostingManager
        swcCostMgr = swModelDocExt.GetCostingManager
        If swcCostMgr Is Nothing Then
            Debug.Print("CostingManager is nothing.")
            Exit Sub
        End If

        'Get Costing part
        swcCostPart = swcCostMgr.CostingModel
        If swcCostPart Is Nothing Then
            Debug.Print("Costing part is nothing.")
            Exit Sub
        End If

        'Set the Costing manufacturing method
        'to structural and get the Costing body
        swcCostBody = swcCostPart.SetCostingMethod("", swcMethodType_e.swcMethodType_Structural)
        If swcCostBody Is Nothing Then
            Debug.Print("Costing body is nothing.")
            Exit Sub
        End If

        'Get the common Costing analysis
        swcCostAnalysis = swcCostBody.GetCostAnalysis
        If swcCostAnalysis Is Nothing Then
            Debug.Print("Failed to activate Costing analysis.")
            Exit Sub
        End If

        'Get the structural Costing analysis
        swcStructuralAnalysis = swcCostAnalysis.GetSpecificAnalysis
        If swcStructuralAnalysis Is Nothing Then
            Debug.Print("Structural Costing analysis is nothing.")
            Exit Sub
        End If

        'Get the material classes from the Costing template
        materialClassCount = swcStructuralAnalysis.GetMaterialClassesCount
        If materialClassCount = 0 Then
            Debug.Print("No material classes for this structural Costing analysis.")
            Exit Sub
        End If
        Debug.Print("Structural Costing Analysis")
        materialClasses = swcStructuralAnalysis.GetMaterialClasses
        Debug.Print("  Valid material classes for this structural Costing Analysis: ")
        For i = 0 To materialClassCount - 1
            Debug.Print("    " & materialClasses(i))
        Next i

        'Set the material class
        swcStructuralAnalysis.CurrentMaterialClass = materialClasses(0)
        Debug.Print("  Name of the material class for this structural Costing analysis: " & materialClasses(0))

        'Get the material names from the Costing template
        templateName = swcCostAnalysis.CostingTemplateName
        Debug.Print("  Costing template path and file name: " & templateName)
        materialCount = swcStructuralAnalysis.GetMaterialCount(materialClasses(0))
        If materialCount = 0 Then
            Debug.Print("No materials for this structural Costing Analysis.")
            Exit Sub
        End If
        Debug.Print("  Number of materials: " & materialCount)
        materials = swcStructuralAnalysis.GetMaterials(materialClasses(0))
        Debug.Print("  Valid materials for this structural Costing Analysis: ")
        For i = 0 To materialCount - 1
            Debug.Print("    " & materials(i))
        Next i
        swcStructuralAnalysis.CurrentMaterial = materials(0)
        Debug.Print("  Name of material for " & materialClasses(0) & " for this structural Costing analysis: " & materials(0))

        'Set and get structural Costing analysis parameters
        'Get current profile
        Debug.Print("  Current profile:")
        Debug.Print("    Standard: " & swcStructuralAnalysis.CurrentProfileStandard)
        Debug.Print("    Type:     " & swcStructuralAnalysis.CurrentProfileType)
        Debug.Print("    Size:     " & swcStructuralAnalysis.CurrentProfileSize)

        'Get current cost method
        costMethod = swcStructuralAnalysis.CurrentCostMethodType
        Select Case costMethod
            Case 0
                Debug.Print("  Current cost method: Unknown")
                Debug.Print("  Exiting. Check the template.")
                Exit Sub
            Case 1
                Debug.Print("  Current cost method: Per length")
            Case 2
                Debug.Print("  Current cost method: Per unit length")
        End Select

        'Reset the shop rate to the default
        swcStructuralAnalysis.ShopRateApplied = True
        swcStructuralAnalysis.ShopRate = 27.55
        Debug.Print("  Shop rate applied: " & swcStructuralAnalysis.ShopRateApplied)
        Debug.Print("  Shop rate: $" & swcStructuralAnalysis.ShopRate)

        totalCost = swcCostAnalysis.GetTotalCostToManufacture
        Debug.Print("Total structural cost to manufacture: $" & totalCost)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
