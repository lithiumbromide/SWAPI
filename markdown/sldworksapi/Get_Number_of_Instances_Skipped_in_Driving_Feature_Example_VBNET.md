---
title: "Get Number of Instances Skipped in Driving Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm"
---

# Get Number of Instances Skipped in Driving Feature Example (VB.NET)

This example shows how to get the number of instances skipped in the driving feature of a derived pattern feature.

```
'--------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\PatternDrivenComponentPattern.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Adds instances to skip in the local linear pattern feature.
' 2. Inserts a derived pattern feature.
' 3. Gets the number of instances skipped in the driving feature for the
'    derived pattern feature.
' 4. Gets whether visual properties are propagated in the derived pattern
'    feature.
' 5. Examine the FeatureManager design tree, graphics area, and
'    Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
	Dim swAssemblyDoc as AssemblyDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swLocalLinearPatternData As LocalLinearPatternFeatureData
        Dim swDerivedPatternFeatureData As DerivedPatternFeatureData
        Dim list(1) As Integer
        Dim instancesSkipData As Object
        Dim instancesSkipData_Derived(1) As Integer
        Dim instancesToSkipCount As Integer
        Dim status As Boolean
        Dim i As Integer

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        'Add instances to skip to local linear pattern feature, LocalLPattern1
        status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swLocalLinearPatternData = swFeature.GetDefinition
        status = swLocalLinearPatternData.AccessSelections(swModel, Nothing)
        list(0) = 11
        list(1) = 14
        instancesSkipData = list
        swLocalLinearPatternData.SkippedItemArray = instancesSkipData
        status = swFeature.ModifyDefinition(swLocalLinearPatternData, swModel, Nothing)

        'Insert derived pattern feature, LocalCompPattern1
        status = swModelDocExt.SelectByID2("Part2^patterndrivencomponentpattern-1@patterndrivencomponentpattern", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, True, 6, Nothing, 0)
	swAssemblyDoc = swModel
        status = swAssemblyDoc.InsertDerivedPattern()

        'Get number of instances skipped in the driving feature, LocalLPattern1,
        'for the derived pattern feature, LocalCompPattern1
        status = swModelDocExt.SelectByID2("LocalCompPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swDerivedPatternFeatureData = swFeature.GetDefinition
        status = swDerivedPatternFeatureData.AccessSelections(swModel, Nothing)
        instancesSkipData_Derived = swDerivedPatternFeatureData.DrivingFeatureSkippedItemArray
        instancesToSkipCount = UBound(instancesSkipData_Derived)
        Debug.Print("Number of instances skipped in the driving feature of the derived pattern feature: " & instancesToSkipCount + 1)
        For i = 0 To instancesToSkipCount
            Debug.Print("  Instance skipped: " & instancesSkipData_Derived(i))
        Next i

        'Get whether visual properties are propagated in the derived pattern feature
        Debug.Print("Visual properties propagated in the derived pattern feature? " & swDerivedPatternFeatureData.PropagateVisualProperty)

        swDerivedPatternFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
