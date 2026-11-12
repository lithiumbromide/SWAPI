---
title: "Get Factor of Safety Values for Composites Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Factor_of_Safety_Values_for_Composites_Example_VBNET.htm"
---

# Get Factor of Safety Values for Composites Example (VB.NET)

This example shows how to get Factor of Safety results for specified entities having either composite or non-composite shells.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1.  Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2.  Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '     (in the IDE, click Project > Add Reference > .NET >
 '     SolidWorks.Interop.cosworks > OK).
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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim COSMOSWORKS As COSMOSWORKS
     Dim CWAddinCallBack As CWAddinCallBack
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim CWResult As CWResults
     Dim CWMesh As CWMesh
     Dim SelMgr As SelectionMgr
     Dim bIsCompositeOption As Boolean
     Dim varArray1(0) As Object
     Dim Obj1 As Object
     Dim NonCompositeCriterion As Integer
     Dim CompositeFailureCriterion As Integer
     Dim ShellFace As Integer
     Dim PlyNum As Integer
     Dim ShellFaceOption As Integer
     Dim MinFOSVal As Integer
     Dim swFactorOfSafetyDist As Integer
     Dim FosVal As Object
     Dim boolstatus As Boolean
     Dim longstatus As Integer
     Dim errCode As Integer
     Dim el As Double, tl As Double

     Sub main()

         Part = SwApp.ActiveDoc

         SelMgr = Part.SelectionManager
         boolstatus = Part.Extension.SketchBoxSelect("0.000000", "0.000000", "0.000000", "0.000000", "0.000000", "0.000000")
         boolstatus = Part.Extension.SelectByID2("Surface-Trim1", "SURFACEBODY", -0.0533802776919856, 0.00381973755003173, 0.025111145036476, True, 0, Nothing, 0)

         Obj1 = SelMgr.GetSelectedObject6(1, -1)
         varArray1(0) = Obj1

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         ActDoc = COSMOSWORKS.ActiveDoc()
         StudyMngr = ActDoc.StudyManager()

         bIsCompositeOption = 1
         NonCompositeCriterion = swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_VonMisesHencky
         CompositeFailureCriterion = swsFOS_CompositeCriterion_e.swsFOSCompositeCriterion_Tsai_Hill
         PlyNum = 0 ' Across all plies
         ShellFace = swsFOS_ShellFaceOption_e.swsFOS_ShellFaceOption_TopFace
         ShellFaceOption = swsFOS_NormalShellFaceOption_e.swsFOS_NormalShellFaceOption_Top
         MinFOSVal = 1
         swFactorOfSafetyDist = swsFOS_DistributionOpt_e.swsFOS_DistributionOpt_AreaBelowFOS

         ' Analyze study 1 (non-composite shells) and process results
         Debug.Print("Analyzing Study 1 with 8 plies...")
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(1)

         ' Create mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(SwApp, "No mesh object.", False)
         CWMesh.Quality = 1
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(SwApp, "Mesh failed.", True)

         ' Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed.", True)
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(SwApp, "No result object.", False)

         ' For non-composite shells
         FosVal = CWResult.GetMinMaxFactorOfSafety2(True, Nothing, swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_Automatic, swsFOS_ShellFaceOption_e.swsFOS_ShellFaceOption_TopFace, 0, errCode)
         Debug.Print("  Non-composite shell:")
         Debug.Print("    Minimum FOS: " & FosVal(0))
         Debug.Print("    Maximum FOS: " & FosVal(1))

         ' For non-composite shells and detail settings
         FosVal = CWResult.GetMinMaxFactorOfSafetyWithDetailSettings2(True, (varArray1), swsFOS_NonCompositeCriterion_e.swsFOSNonCompositeCriterion_VonMisesHencky, True, 1000, swsStrengthUnit_e.swsStrengthUnitPSI, swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_YieldStrength, 0, swsFactorOfSafetyStressLimitOption_e.swsFactorOfSafetyStressLimitOption_UltimateStrength, 0, 1, 1, False, ShellFaceOption, 0, errCode)
         Debug.Print("  Non-composite shell and detail settings:")
         Debug.Print("    Minimum FOS: " & FosVal(0))
         Debug.Print("    Maximum FOS: " & FosVal(1))

         ' Analyze study 2 (composite shells) and process results
         Debug.Print("")
         Debug.Print("Analyzing Study 2 with 16 plies...")
         StudyMngr.ActiveStudy = 2
         Study = StudyMngr.GetStudy(2)

         ' Create mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(SwApp, "No mesh object.", False)
         CWMesh.Quality = 1
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(SwApp, "Mesh failed.", True)

         ' Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed.", True)
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(SwApp, "No result object.", False)

         FosVal = CWResult.GetFactorOfSafetyForComposites(True, (varArray1), NonCompositeCriterion, CompositeFailureCriterion, PlyNum, ShellFace, ShellFaceOption, swFactorOfSafetyDist, MinFOSVal, errCode)
         Debug.Print("  Composite shell:")
         Debug.Print("    Minimum FOS: " & FosVal(0))
         Debug.Print("    Maximum FOS: " & FosVal(1))

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)

         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")

     End Sub

     Public swApp As SldWorks

 End Class
```
