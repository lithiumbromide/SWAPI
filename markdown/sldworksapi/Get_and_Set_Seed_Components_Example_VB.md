---
title: "Get and Set Seed Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Seed_Components_Example_VB.htm"
---

# Get and Set Seed Components Example (VBA)

This example shows how to access the seed components of patterns in an assembly. It also shows that seed components can be replaced either by IComponent2 objects or IFeature objects representing those components.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly exists.
' 2. Open the Immediate Window.
'
' Postconditions:
' 1. Gets the names of the seed components.
' 2. Replaces the seed components either by an IComponent2 object
'    or an IFeature object representing the component.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    ' Attach to SOLIDWORKS Design
    Dim swApp As SldWorks.SldWorks
    Set swApp = Application.SldWorks
```

```
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"
```

```
    ' Open the model
    Dim swModel As ModelDoc2
    Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Verify that the model is active
    If swModel Is Nothing Then
        Debug.Print "No active model document"
        Exit Sub
    End If
```

```
    Debug.Print "Model: " & swModel.GetTitle
```

```
    ' Get all of the features in the model
    Dim swFeatMgr As FeatureManager
    Set swFeatMgr = swModel.FeatureManager
```

```
    Dim vFeatures As Variant
    vFeatures = swFeatMgr.GetFeatures(True)
```

```
    ' Iterate over all features
    Dim iFeat As Integer
    For iFeat = LBound(vFeatures) To UBound(vFeatures)
        Dim swFeature As Feature
        Set swFeature = vFeatures(iFeat)
```

```
        ' Is the current feature a patterned feature?
        Select Case UCase(swFeature.GetTypeName2)
        Case "LOCALLPATTERN"
            ' ILocalLinearPatternFeatureData
            Debug.Print "    Linear Pattern: " & swFeature.Name
            ProcessGenericPatternDefinition swFeature, swModel
```

```
        Case "LOCALCIRPATTERN"
            ' ILocalCircularPatternFeatureData
            Debug.Print "    Circular Pattern: " & swFeature.Name
            ProcessGenericPatternDefinition swFeature, swModel
```

```
        Case "DERIVEDLPATTERN"
            ' IDerivedPatternFeatureData
            Debug.Print "    Derived Linear Pattern: " & swFeature.Name
            ProcessGenericPatternDefinition swFeature, swModel
```

```
        Case "DERIVEDCIRPATTERN"
            ' IDerivedPatternFeatureData
            Debug.Print "    Derived Circular Pattern: " & swFeature.Name
            ProcessGenericPatternDefinition swFeature, swModel
```

```
        End Select
    Next
```

```
End Sub
```

```
Private Sub ProcessGenericPatternDefinition(swFeature As Feature, swModel As ModelDoc2)
```

```
    Dim patternDef As Object
    Set patternDef = swFeature.GetDefinition
```

```
    ' Verify the type of feature data object
    If TypeOf patternDef Is DerivedPatternFeatureData Or _
       TypeOf patternDef Is LocalCircularPatternFeatureData Or _
       TypeOf patternDef Is LocalLinearPatternFeatureData Then
```

```
        If patternDef.AccessSelections(swModel, Nothing) Then
            ' Get the seed components for this pattern
            Dim vSeedComps As Variant
            vSeedComps = patternDef.SeedComponentArray
```

```
            ProcessSeedComponentArray vSeedComps
```

```
            ' Replace the seed array
            patternDef.SeedComponentArray = vSeedComps
```

```
            ' Update the feature definition
            swFeature.ModifyDefinition patternDef, swModel, Nothing
        End If
    End If
End Sub
```

```
Private Sub ProcessSeedComponentArray(ByRef vSeedComps As Variant)
    ' Replace the current seeds with themselves as either features or components
    Dim replacementSeeds() As Object
    ReDim replacementSeeds(LBound(vSeedComps) To UBound(vSeedComps))
```

```
    ' Iterate over each seed component
    Dim iSeed As Integer
    For iSeed = LBound(vSeedComps) To UBound(vSeedComps)
        Dim swCompFeat As Feature
        Set swCompFeat = vSeedComps(iSeed)
```

```
        Debug.Print "        Seed " & iSeed & ": " & swCompFeat.Name
```

```
        ' Access the seed component represented by the feature
        Dim swComp As Component2
        Set swComp = swCompFeat.GetSpecificFeature2
```

```
        ' Arbitrarily decide whether to replace this seed component
        ' with a component or a feature
        If iSeed Mod 2 = 0 Then
            Set replacementSeeds(iSeed) = swComp
        Else
            Set replacementSeeds(iSeed) = swCompFeat
        End If
```

```
    Next
```

```
    ' Replace the seed array
    vSeedComps = replacementSeeds
End Sub
```
