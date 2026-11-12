---
title: "Get Factor of Safety Values for Composites Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Factor_of_Safety_Values_for_Composites_Example_VB.htm"
---

# Get Factor of Safety Values for Composites Example (VBA)

This example shows how to get Factor of Safety results for specified entities having either composite or non-composite shells.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1.  Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2.  Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '     click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3.  Open public_documents\samples\tutorial\api\tjoint.sldprt.
 ' 4.  Click the Ready - 8 plies tab.
 ' 5.  Expand tjoint in the FeatureManager design tree.
 ' 6.  Right-click SurfaceBody1 and click Edit Definition.
 ' 7.  Select Thin and click the green arrow.
 ' 8.  Right-click SurfaceBody2 and click Edit Definition.
 ' 9.  Select Thin and click the green arrow.
 ' 10. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Analyzes two studies:
 '    a. 8 plies with non-composite materials applied to surface bodies.
 '    b. 16 plies with composite materials applied to surface bodies.
 ' 2. Inspect the Immediate window for the minimum and maximum factors of safety.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Option Explicit
Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim CWResult As CosmosWorksLib.CWResults
 Dim CWMesh As CosmosWorksLib.CWMesh
 Dim SelMgr As SelectionMgr
 Dim bIsCompositeOption As Boolean
 Dim varArray1(0) As Variant
 Dim Obj1 As Object
 Dim NonCompositeCriterion As Long
 Dim CompositeFailureCriterion As Long
 Dim ShellFace As Long
 Dim PlyNum As Long
 Dim ShellFaceOption As Long
 Dim MinFOSVal As Long
 Dim swFactorOfSafetyDist As Long
 Dim FosVal As Variant
 Dim boolstatus As Boolean
 Dim errCode As Long
 Dim el As Double, tl As Double
Sub main()
    Set SwApp = Application.SldWorks
     Set Part = SwApp.ActiveDoc
    Set SelMgr = Part.SelectionManager
     boolstatus = Part.Extension.SketchBoxSelect("0.000000", "0.000000", "0.000000", "0.000000", "0.000000", "0.000000")
     boolstatus = Part.Extension.SelectByID2("Surface-Trim1", "SURFACEBODY", -5.33802776919856E-02, 3.81973755003173E-03, 0.025111145036476, True, 0, Nothing, 0)

    Set Obj1 = SelMgr.GetSelectedObject6(1, -1)
     Set varArray1(0) = Obj1

    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     Set StudyMngr = ActDoc.StudyManager()

    bIsCompositeOption = True
     NonCompositeCriterion = swsFOSNonCompositeCriterion_VonMisesHencky
     CompositeFailureCriterion = swsFOSCompositeCriterion_Tsai_Hill
     PlyNum = 0 ' Across all plies
     ShellFace = swsFOS_ShellFaceOption_TopFace
     ShellFaceOption = swsFOS_NormalShellFaceOption_Top
     MinFOSVal = 1
     swFactorOfSafetyDist = swsFOS_DistributionOpt_AreaBelowFOS

    ' Get study 1 (non-composite shells)
     Debug.Print "Analyzing Study 1 with 8 plies..."
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(1)

    ' Create mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object", False
     CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed", True
    ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed", True
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object", False

    ' For non-composite shells
     FosVal = CWResult.GetMinMaxFactorOfSafety2(True, Nothing, swsFOSNonCompositeCriterion_Automatic, swsFOS_ShellFaceOption_TopFace, 0, errCode)
     Debug.Print "  Non-composite shell:"
     Debug.Print "    Minimum FOS: " & FosVal(0)
     Debug.Print "    Maximum FOS: " & FosVal(1)

    ' For non-composite shells and detail settings
     FosVal = CWResult.GetMinMaxFactorOfSafetyWithDetailSettings2(True, (varArray1), swsFOSNonCompositeCriterion_VonMisesHencky, True, 1000, swsStrengthUnitPSI, swsFactorOfSafetyStressLimitOption_YieldStrength, 0, swsFactorOfSafetyStressLimitOption_UltimateStrength, 0, 1, 1, False, ShellFaceOption, 0, errCode)
     Debug.Print "  Non-composite shell and detail settings:"
     Debug.Print "    Minimum FOS: " & FosVal(0)
     Debug.Print "    Maximum FOS: " & FosVal(1)

    ' Get study 2 (composite shells)
     Debug.Print ""
     Debug.Print "Analyzing Study 2 with 16 plies..."
     StudyMngr.ActiveStudy = 2
     Set Study = StudyMngr.GetStudy(2)

    ' Create mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object", False
     CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed", True

    ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed", True
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object", False

    FosVal = CWResult.GetFactorOfSafetyForComposites(bIsCompositeOption, (varArray1), NonCompositeCriterion, CompositeFailureCriterion, PlyNum, ShellFace, ShellFaceOption, swFactorOfSafetyDist, MinFOSVal, errCode)
     Debug.Print "  Composite shell:"
     Debug.Print "    Minimum FOS: " & FosVal(0)
     Debug.Print "    Maximum FOS: " & FosVal(1)

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String, EndTest As Boolean)
    SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
End Sub
```
