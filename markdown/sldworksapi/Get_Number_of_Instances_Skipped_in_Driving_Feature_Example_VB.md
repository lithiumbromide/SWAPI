---
title: "Get Number of Instances Skipped in Driving Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm"
---

# Get Number of Instances Skipped in Driving Feature Example (VBA)

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
Option Explicit
```

```
    Dim SwApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssemblyDoc as SldWorks.AssemblyDoc
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelectionMgr As SldWorks.SelectionMgr
    Dim swFeature As SldWorks.Feature
    Dim swLocalLinearPatternData As SldWorks.LocalLinearPatternFeatureData
    Dim swDerivedPatternFeatureData As SldWorks.DerivedPatternFeatureData
    Dim list(1) As Long
    Dim instancesSkipData As Variant
    Dim instancesSkipData_Derived As Variant
    Dim instancesToSkipCount As Long
    Dim status As Boolean
    Dim i As Long
```

```
Sub main()
```

```
    Set SwApp = Application.SldWorks
    Set swModel = SwApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Add instances to skip to local linear pattern feature, LocalLPattern1
    status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swLocalLinearPatternData = swFeature.GetDefinition
    status = swLocalLinearPatternData.AccessSelections(swModel, Nothing)
    list(0) = 11
    list(1) = 14
    instancesSkipData = list
    swLocalLinearPatternData.SkippedItemArray = instancesSkipData
    status = swFeature.ModifyDefinition(swLocalLinearPatternData, swModel, Nothing)
```

```
    'Insert derived pattern feature, LocalCompPattern1
    status = swModelDocExt.SelectByID2("Part2^patterndrivencomponentpattern-1@patterndrivencomponentpattern", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("LocalLPattern1", "COMPPATTERN", 0, 0, 0, True, 6, Nothing, 0)
    Set swAssemblyDoc = swModel
    status = swAssemblyDoc.InsertDerivedPattern()
```

```
    'Get number of instances skipped in the driving feature, LocalLPattern1,
    'for the derived pattern feature, LocalCompPattern1
    status = swModelDocExt.SelectByID2("LocalCompPattern1", "COMPPATTERN", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swDerivedPatternFeatureData = swFeature.GetDefinition
    status = swDerivedPatternFeatureData.AccessSelections(swModel, Nothing)
    instancesSkipData_Derived = swDerivedPatternFeatureData.DrivingFeatureSkippedItemArray
    instancesToSkipCount = UBound(instancesSkipData_Derived)
    Debug.Print "Number of instances skipped in the driving feature of the derived pattern feature: " & instancesToSkipCount + 1
    For i = 0 To instancesToSkipCount
        Debug.Print "  Instance skipped: " & instancesSkipData_Derived(i)
    Next i
    swDerivedPatternFeatureData.ReleaseSelectionAccess
```

```
    'Get whether visual properties are propagated in the derived pattern feature
    Debug.Print "Visual properties propagated in the derived pattern feature? " & swDerivedPatternFeatureData.PropagateVisualProperty
```

```
End Sub
```
