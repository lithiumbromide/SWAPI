---
title: "Insert Structural Weldments Using Custom Weldment Profile Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VB.htm"
---

# Insert Structural Weldments Using Custom Weldment Profile Example (VBA)

This example shows how to insert a structural weldment feature using a custom weldment profile configuration and structural member groups.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified library feature exists.
' 2. Verify that a valid pathname exists in Parts in Tools > Options >
'    System Options > Default Templates.
' 3. Create C:\Test\Pipes.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified library feature, adds the nxn configuration,
'    saves the library feature as nxn.sldlfp, and closes the new library
'    feature, which is called a custom weldment profile when used to create
'    structural weldment features.
' 2. Creates a new part document that contains a sketch of two
'    rectangles.
' 3. Creates a weldment and two structural member features using the
'    sketch and the nxn configuration of the custom weldment profile created in
'    step 1.
' 4. Rotates Pipes nxn(1).
' 5. Examine the FeatureManager design tree, graphics area, and
'    the Immediate window.
'---------------------------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchMgr As SldWorks.SketchManager
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swConfigMgr As SldWorks.ConfigurationManager
Dim swConfig As SldWorks.Configuration
Dim swFeature As SldWorks.Feature
Dim swStructuralMemberGroup1 As SldWorks.StructuralMemberGroup
Dim swStructuralMemberGroup2 As SldWorks.StructuralMemberGroup
Dim swWeldFeat As SldWorks.Feature
Dim swStructuralMemberFeatData As SldWorks.StructuralMemberFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim libFeature As String
Dim newLibFeature As String
Dim macroFolder As String
Dim template As String
Dim sketchLines As Variant
Dim segs1(1) As Object
Dim groups1 As Variant
Dim groupArray1(0) As Object
Dim segs2(1) As Object
Dim groups2 As Variant
Dim groupArray2(0) As Object
Dim group As SldWorks.StructuralMemberGroup
Dim groups As Variant
Dim segs As Variant
Dim weldmentProfile As String
Dim weldmentConfigurationName As String
```

```
Option Explicit
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open existing library feature, add nxn configuration,
    'and save library feature as nxn.sldlfp
    libFeature = "C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp"
    Set swModel = swApp.OpenDoc6(libFeature, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("0.5 sch 40.SLDPRT", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.AddConfiguration("nxn", "", "", swConfigurationOptions2_e.swConfigOption_DontActivate, "", "")
    newLibFeature = "C:\Test\Pipes\nxn.sldlfp"
    status = swModelDocExt.SaveAs(newLibFeature, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
    Set swModel = Nothing
    swApp.CloseDoc newLibFeature
```

```
    'Open new part document and
    'create weldment and structural members
    macroFolder = swApp.GetCurrentMacroPathFolder()
    swApp.SetCurrentWorkingDirectory macroFolder
    template = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
    Set swModel = swApp.NewDocument(template, 0, 0, 0)
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
```

```
    swModel.ClearSelection2 True
```

```
    Set swSketchMgr = swModel.SketchManager
    sketchLines = swSketchMgr.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0)
```

```
    swModel.ClearSelection2 True
```

```
    sketchLines = swSketchMgr.CreateCornerRectangle(0.06513561531715, 0.03369083550887, 0, 0.1807053904567, -0.08106219210316, 0)
    swSketchMgr.InsertSketch True
```

```
    swModel.ViewZoomtofit2
```

```
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.InsertWeldmentFeature()
```

```
    Set swStructuralMemberGroup1 = swFeatMgr.CreateStructuralMemberGroup
```

```
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)
```

```
    Set segs1(0) = swSelMgr.GetSelectedObject6(1, 0)
    Set segs1(1) = swSelMgr.GetSelectedObject6(2, 0)

    swStructuralMemberGroup1.segments = segs1
    swStructuralMemberGroup1.Angle = 0.785714285714286 'radians
    swStructuralMemberGroup1.ApplyCornerTreatment = True
    swStructuralMemberGroup1.CornerTreatmentType = swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter
    swStructuralMemberGroup1.MirrorProfile = True
    swStructuralMemberGroup1.MirrorProfileAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical
```

```
    Set groupArray1(0) = swStructuralMemberGroup1
    groups1 = groupArray1
```

```
    weldmentProfile = "C:\Test\Pipes\nxn.SLDLFP"
    weldmentConfigurationName = "nxn"
    Set swFeature = swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups1), weldmentConfigurationName)
```

```
    swModel.ClearSelection2 True
```

```
    Set swStructuralMemberGroup2 = swFeatMgr.CreateStructuralMemberGroup
```

```
    status = swModelDocExt.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, True, 0, Nothing, 0)
    Set segs2(0) = swSelMgr.GetSelectedObject6(1, 0)
    Set segs2(1) = swSelMgr.GetSelectedObject6(2, 0)
```

```
    swStructuralMemberGroup2.segments = segs2
    swStructuralMemberGroup2.AlignAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical
```

```
    Set groupArray2(0) = swStructuralMemberGroup2
    groups2 = groupArray2
```

```
    Set swFeature = swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups2), weldmentConfigurationName)
```

```
    swModel.ClearSelection2 True
```

```
    'Get feature data for each structural member group
    status = swModelDocExt.SelectByID2("Pipes nxn(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swStructuralMemberFeatData = swWeldFeat.GetDefinition
    swStructuralMemberFeatData.AccessSelections swModel, Nothing
```

```
    Debug.Print ""
    Debug.Print "Groups count: " & swStructuralMemberFeatData.GetGroupsCount
    Debug.Print "  Feature name: " & swWeldFeat.Name
    Debug.Print "    Custom weldment profile configuration name: " & swStructuralMemberFeatData.ConfigurationName
    Debug.Print "    Transfer material? " & swStructuralMemberFeatData.TransferMaterial
    Debug.Print "    Library material profile: " & swStructuralMemberFeatData.LibraryProfileMaterial
```

```
    groups = swStructuralMemberFeatData.groups
```

```
    Dim i As Long, j As Long
        Debug.Print "    Group:"
        For i = LBound(groups) To UBound(groups)
           Set group = groups(i)
            Debug.Print "      Segment count: " & group.GetSegmentsCount
            Debug.Print "      Rotational angle: " & group.Angle
            Debug.Print "      Apply corner treatment: " & group.ApplyCornerTreatment
            Debug.Print "      Corner treatment type: " & group.CornerTreatmentType
            Debug.Print "      Mirror profile: " & group.MirrorProfile
            Debug.Print "      Mirror profile axis: " & group.MirrorProfileAxis
            Debug.Print "      Gap within: " & group.GapWithinGroup
            segs = group.segments
            For j = LBound(segs) To UBound(segs)
                segs(j).Select False
            Next j
        Next i
```

```
    swStructuralMemberFeatData.ReleaseSelectionAccess
```

```
    status = swModelDocExt.SelectByID2("Pipes nxn(2)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swStructuralMemberFeatData = swWeldFeat.GetDefinition
    swStructuralMemberFeatData.AccessSelections swModel, Nothing
```

```
    Debug.Print ""
    Debug.Print "Groups count: " & swStructuralMemberFeatData.GetGroupsCount
    Debug.Print "  Feature name: " & swWeldFeat.Name
    Debug.Print "    Custom weldment profile configuration name: " & swStructuralMemberFeatData.ConfigurationName
    Debug.Print "    Transfer material? " & swStructuralMemberFeatData.TransferMaterial
    Debug.Print "    Library material profile: " & swStructuralMemberFeatData.LibraryProfileMaterial
```

```
    groups = swStructuralMemberFeatData.groups
        Debug.Print "    Group:"
        For i = LBound(groups) To UBound(groups)
           Set group = groups(i)
            Debug.Print "      Segment count: " & group.GetSegmentsCount
            Debug.Print "      Rotational angle: " & group.Angle
            Debug.Print "      Apply corner treatment: " & group.ApplyCornerTreatment
            Debug.Print "      Corner treatment type: " & group.CornerTreatmentType
            Debug.Print "      Mirror profile: " & group.MirrorProfile
            Debug.Print "      Mirror profile axis: " & group.MirrorProfileAxis
            Debug.Print "      Gap within: " & group.GapWithinGroup
            segs = group.segments
            For j = LBound(segs) To UBound(segs)
                segs(j).Select False
            Next j
        Next i
```

```
    swStructuralMemberFeatData.ReleaseSelectionAccess
    swModel.ClearSelection2 True
```

```
End Sub
```
