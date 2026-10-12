---
title: "Insert Structural Weldments Using Custom Weldment Profile Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VBNET.htm"
---

# Insert Structural Weldments Using Custom Weldment Profile Example (VB.NET)

This example shows how to insert a structural weldment feature using a custom weldment profile configuration and structural member groups.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified library feature and part document template
'    exist.
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatMgr As FeatureManager
        Dim swSelMgr As SelectionMgr
        Dim swSketchMgr As SketchManager
        Dim swFeatureMgr As FeatureManager
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim swFeature As Feature
        Dim swStructuralMemberGroup1 As StructuralMemberGroup
        Dim swStructuralMemberGroup2 As StructuralMemberGroup
        Dim swWeldFeat As Feature
        Dim swStructuralMemberFeatData As StructuralMemberFeatureData
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim libFeature As String
        Dim newLibFeature As String
        Dim macroFolder As String
        Dim template As String
        Dim sketchLines As Object
        Dim segs1(1) As SketchSegment
        Dim groupArray1(0) As Object
        Dim groups1(0) As DispatchWrapper
        Dim segs2(1) As SketchSegment
        Dim groups2(0) As DispatchWrapper
        Dim groupArray2(0) As Object
        Dim group As StructuralMemberGroup
        Dim groups(1) As Object
        Dim segs(1) As Object
        Dim weldmentProfile As String
        Dim weldmentConfigurationName As String

        'Open existing library feature, add nxn configuration,
        'and save library feature as nxn.sldlfp
        libFeature = "C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp"
        swModel = swApp.OpenDoc6(libFeature, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("0.5 sch 40.SLDPRT", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.AddConfiguration("nxn", "", "", swConfigurationOptions2_e.swConfigOption_DontActivate, "", "")
        newLibFeature = "C:\Test\Pipes\nxn.sldlfp"
        status = swModelDocExt.SaveAs(newLibFeature, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
        swModel = Nothing
        swApp.CloseDoc(newLibFeature)

        'Open new part document and
        'create weldment and structural members
        macroFolder = swApp.GetCurrentMacroPathFolder()
        swApp.SetCurrentWorkingDirectory(macroFolder)
        template = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
        swModel = swApp.NewDocument(template, 0, 0, 0)
        swFeatMgr = swModel.FeatureManager
        swSelMgr = swModel.SelectionManager
        swModel.ClearSelection2(True)
        swSketchMgr = swModel.SketchManager
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0)
        swModel.ClearSelection2(True)
        sketchLines = swSketchMgr.CreateCornerRectangle(0.06513561531715, 0.03369083550887, 0, 0.1807053904567, -0.08106219210316, 0)
        swSketchMgr.InsertSketch(True)
        swModel.ViewZoomtofit2()
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertWeldmentFeature()
        swStructuralMemberGroup1 = swFeatMgr.CreateStructuralMemberGroup
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)
        segs1(0) = swSelMgr.GetSelectedObject6(1, 0)
        segs1(1) = swSelMgr.GetSelectedObject6(2, 0)
        swStructuralMemberGroup1.Segments = segs1
        swStructuralMemberGroup1.Angle = 0.785714285714286 'radians
        swStructuralMemberGroup1.ApplyCornerTreatment = True
        swStructuralMemberGroup1.CornerTreatmentType = swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter
        swStructuralMemberGroup1.MirrorProfile = True
        swStructuralMemberGroup1.MirrorProfileAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical

        groupArray1(0) = swStructuralMemberGroup1
        groups1(0) = New DispatchWrapper(groupArray1(0))

        weldmentProfile = "C:\Test\Pipes\nxn.SLDLFP"
        weldmentConfigurationName = "nxn"
        swFeature = swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups1), weldmentConfigurationName)
        swModel.ClearSelection2(True)

        swStructuralMemberGroup2 = swFeatMgr.CreateStructuralMemberGroup
        status = swModelDocExt.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, True, 0, Nothing, 0)
        segs2(0) = swSelMgr.GetSelectedObject6(1, 0)
        segs2(1) = swSelMgr.GetSelectedObject6(2, 0)

        swStructuralMemberGroup2.Segments = segs2
        swStructuralMemberGroup2.AlignAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical

        groupArray2(0) = swStructuralMemberGroup2
        groups2(0) = New DispatchWrapper(groupArray2(0))

        swFeature = swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups2), weldmentConfigurationName)
        swModel.ClearSelection2(True)

        'Get feature data for each structural member group
        status = swModelDocExt.SelectByID2("Pipes nxn(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
        swStructuralMemberFeatData = swWeldFeat.GetDefinition
        swStructuralMemberFeatData.AccessSelections(swModel, Nothing)
        Debug.Print("")
        Debug.Print("Groups count: " & swStructuralMemberFeatData.GetGroupsCount)
        Debug.Print("  Feature name: " & swWeldFeat.Name)
        Debug.Print("    Custom weldment profile configuration name: " & swStructuralMemberFeatData.ConfigurationName)
        Debug.Print("    Transfer material? " & swStructuralMemberFeatData.TransferMaterial)
        Debug.Print("    Library material profile: " & swStructuralMemberFeatData.LibraryProfileMaterial)

        groups = swStructuralMemberFeatData.groups
        Dim i As Long, j As Long
        Debug.Print("    Group:")
        For i = LBound(groups) To UBound(groups)
            group = groups(i)
            Debug.Print("      Segment count: " & group.GetSegmentsCount)
            Debug.Print("      Rotational angle: " & group.Angle)
            Debug.Print("      Apply corner treatment: " & group.ApplyCornerTreatment)
            Debug.Print("      Corner treatment type: " & group.CornerTreatmentType)
            Debug.Print("      Mirror profile: " & group.MirrorProfile)
            Debug.Print("      Mirror profile axis: " & group.MirrorProfileAxis)
            Debug.Print("      Gap within: " & group.GapWithinGroup)
            segs = group.segments
            For j = LBound(segs) To UBound(segs)
                segs(j).Select(False)
            Next j
        Next i
        swStructuralMemberFeatData.ReleaseSelectionAccess()

        status = swModelDocExt.SelectByID2("Pipes nxn(2)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
        swStructuralMemberFeatData = swWeldFeat.GetDefinition
        swStructuralMemberFeatData.AccessSelections(swModel, Nothing)
        Debug.Print("")
        Debug.Print("Groups count: " & swStructuralMemberFeatData.GetGroupsCount)
        Debug.Print("  Feature name: " & swWeldFeat.Name)
        Debug.Print("    Custom weldment profile configuration name: " & swStructuralMemberFeatData.ConfigurationName)
        Debug.Print("    Transfer material? " & swStructuralMemberFeatData.TransferMaterial)
        Debug.Print("    Library material profile: " & swStructuralMemberFeatData.LibraryProfileMaterial)

        groups = swStructuralMemberFeatData.groups
        Debug.Print("    Group:")
        For i = LBound(groups) To UBound(groups)
            group = groups(i)
            Debug.Print("      Segment count: " & group.GetSegmentsCount)
            Debug.Print("      Rotational angle: " & group.Angle)
            Debug.Print("      Apply corner treatment: " & group.ApplyCornerTreatment)
            Debug.Print("      Corner treatment type: " & group.CornerTreatmentType)
            Debug.Print("      Mirror profile: " & group.MirrorProfile)
            Debug.Print("      Mirror profile axis: " & group.MirrorProfileAxis)
            Debug.Print("      Gap within: " & group.GapWithinGroup)
            segs = group.segments
            For j = LBound(segs) To UBound(segs)
                segs(j).Select(False)
            Next j
        Next i
        swStructuralMemberFeatData.ReleaseSelectionAccess()
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
