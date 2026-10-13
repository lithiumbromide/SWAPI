---
title: "Create Plots for a Static Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Plots_for_Static_Study_Example_VBNET.htm"
---

# Create Plots for a Static Study Example (VB.NET)

This example shows how to create plots of displacement, stress, and strain results in a static study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 '  2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '     (in the IDE, click Project > Add Reference > .NET >
 '     SolidWorks.Interop.cosworks > OK).
 '  3. Ensure that c:\temp exists.
 '  4. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 '  5. Open the Immediate window.
 '
 ' Postconditions:
  '  1. Deletes all default static study plots from the model document.
 '  2. Activates the Ready static study.
 '  3. Meshes and runs the study.
 '  4. Creates Displacement1 plot.
 '  5. Changes the units of the displacement plot.
 '  6. Creates and activates Stress2 plot.
 '  7. Probes and annotates Stress2 and saves the probed result plot to
 '     c:\temp\tutor1-Ready-Image-1.png.
 '  8. Creates Strain1 plot.
 '  9. Applies a view orientation to each plot.
  ' 10. Gets the minimum and maximum values for the result plots.
 ' 11. Click OK to close each message box.
 ' 12. Detect stress hot spots and singularities.
 ' 13. Creates the Stress Hot Spot1 plot and gets hot spot nodes and elements.
 ' 14. Inspect c:\temp\tutor1-Ready-Image-1.png.
  ' 15. Inspect the Immediate window.
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

     Sub main()

         Dim COSMOSWORKS As CosmosWorks
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CWMesh As CWMesh
         Dim CWResult As CWResults
         Dim CWCFf As CWPlot
         Dim CWProbeResultsManager As CWResultsProbeManager
         Dim errCode As Long
         Dim el As Double, tl As Double
         Dim Disp As Object, Stress As Object, Strn As Object
         Dim SelNodeElemVariant(1) As Integer
         Dim SelNodeElemWarnings As Object = Nothing

         Const URESMax As Double = 1004928   'nm
         Const URESMin As Double = 0.0#        'nm
         Const VONMax As Double = 284       'MPa
         Const VONMin As Double = 0.797     'MPa
         Const MaxStrn As Double = 0.00352
         Const MinStrn As Double = 0.00000294

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object", True)
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object", True)

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document", True)

         'Delete all default static study plots from this model
         ActDoc.DeleteAllDefaultStaticStudyPlots()

         'Get Ready study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager object", True)
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No study object", True)

         'Set static study options
         Dim StudyOptions As CWStaticStudyOptions
         StudyOptions = Study.StaticStudyOptions
         StudyOptions.AdaptiveMethodType = 2
         StudyOptions.PAdaptiveConvergenceCriteria = 0
         StudyOptions.PAdaptiveErrorLimit = 1.0#
         StudyOptions.PAdaptiveMaxIterations = 4
         StudyOptions.PAdaptiveMaxPOrder = 5
         StudyOptions.PAdaptiveStartingPOrder = 2
         StudyOptions.PAdaptiveStrainEnergyErrorLimit = 2.0#
         StudyOptions.IncludeRemarkInReport = 1
         StudyOptions.RemarkComment = "Remark comment"
         StudyOptions.NoPenetration = 1
         StudyOptions.IgnoreClearanceForSurfaceContact = 1
         StudyOptions.IncompatibleBondingOption = swsIncompatibleBondingOption_e.swsIncompatibleBondingOption_Automatic
         StudyOptions.IncludeGlobalFriction = 1
         StudyOptions.FrictionCoefficient = 0.5

         'Mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No mesh object", False)
         CWMesh.Quality = 1
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed", True)

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed", True)

         'Get results
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No result object", False)

         Debug.Print("Time taken in seconds for input phase: " & Study.GetTimeTakenForInputPhase)
         Debug.Print("Time taken in seconds to solve this study: " & Study.GetTotalSolutionTime)

         'Create displacement plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, swsDisplacementComponent_e.swsDisplacementComponentURES, swsLinearUnit_e.swsLinearUnitCentimeters, False, errCode)
         If CWCFf Is Nothing Then ErrorMsg(swApp, "Failed to create plot", False)

         'Change the units from cm to in
         errCode = CWCFf.SetComponentUnitAndValueByElem(swsDisplacementComponent_e.swsDisplacementComponentURES, swsLinearUnit_e.swsLinearUnitInches, False)

         'Apply top view orientation
         errCode = CWCFf.ApplyNameViewOrientation2(swsNameViewOrientation_e.swsNameViewOrientation_Top)

         'Activate plot
         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated", True)

         'Get min/max resultant displacements from plot
         Disp = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No displacement result values", True)

         If (Disp(1) < 0.95 * URESMin) Or (Disp(1) > 1.05 * URESMin) Then
             ErrorMsg(swApp, "URES minimum % error = " & (((Disp(1) - URESMin) / URESMin) * 100), False)
         End If

         If (Disp(3) < 0.95 * URESMax) Or (Disp(3) > 1.05 * URESMax) Then
             ErrorMsg(swApp, "URES maximum % error = " & (((Disp(3) - URESMax) / URESMax) * 100), False)
         End If

         'Create stress plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultStress, swsStaticResultNodalStressComponentTypes_e.swsStaticNodalStress_VON, swsStrengthUnit_e.swsStrengthUnitPascal, False, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to create plot", True)

         'Apply bottom view orientation
         errCode = CWCFf.ApplyNameViewOrientation2(swsNameViewOrientation_e.swsNameViewOrientation_Bottom)

         'Activate plot
         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated", True)

         'Get min/max von Mises stresses from plot
         Stress = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No stress results", True)

         If (Stress(1) < 0.95 * VONMin) Or (Stress(1) > 1.05 * VONMin) Then
             ErrorMsg(swApp, " Minimum von Mises stress % error = " & (((Stress(1) - VONMin) / VONMin) * 100), False)
         End If

         If (Stress(3) < 0.95 * VONMax) Or (Stress(3) > 1.05 * VONMax) Then
             ErrorMsg(swApp, "Maximum von Mises stress % error = " & (((Stress(3) - VONMax) / VONMax) * 100), False)
         End If

         ' Probe stress plot at two locations
         CWProbeResultsManager = CWCFf.GetResultsProbeManager(errCode)

         errCode = CWProbeResultsManager.BeginProbing()

         CWProbeResultsManager.ClearSelectionAndAnnotations()
         CWProbeResultsManager.ProbingOption = swsProbePostResultOption_e.swsProbePostResultOption_AtNodeElemNumber
         SelNodeElemVariant(0) = 1033
         SelNodeElemVariant(1) = 924

        errCode = CWProbeResultsManager.ShowAnnotationOnSelNodeElems((SelNodeElemVariant), SelNodeElemWarnings)
         If errCode = 14 Then ErrorMsg(swApp, "Not all specified nodes or elements are annotated", True)

         errCode = CWProbeResultsManager.CaptureProbedResultPlotAsPNGImage("c:\temp\", "tutor1-Ready-Image-1")

         errCode = CWProbeResultsManager.EndProbing()

         'Create strain plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultStrain, swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ESTRN, swsStrengthUnit_e.swsStrengthUnitPascal, True, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to create plot", True)

         'Apply left view orientation
         errCode = CWCFf.ApplyNameViewOrientation2(swsNameViewOrientation_e.swsNameViewOrientation_Left)

         'Activate plot
         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated", True)

         'Get min/max strains from plot
         Strn = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No strain results", True)

         If (Strn(1) < 0.95 * MinStrn) Or (Strn(1) > 1.05 * MinStrn) Then
             ErrorMsg(swApp, "Minimum strain % error = " & (((Strn(1) - MinStrn) / MinStrn) * 100), False)
         End If

         If (Strn(3) < 0.95 * MaxStrn) Or (Strn(3) > 1.05 * MaxStrn) Then
             ErrorMsg(swApp, "Maximum strain % error = " & (((Strn(3) - MaxStrn) / MaxStrn) * 100), False)
         End If

         'Detect stress hot spots and singularities
         Dim hotSpotsFound As Boolean
         Dim singularitiesFound As Boolean
         Dim nodeArray As Object = Nothing
         Dim elemArray As Object = Nothing
         errCode = CWResult.RunStressHotSpotDiagnosticsAndDetectSingularities(25, True, 3, 0.6, 1.5, 0, hotSpotsFound, singularitiesFound)

         'Create stress hot spot plot and get detected hot spots
         If hotSpotsFound = True Then
             errCode = CWResult.GetDetectedHotSpotNodes(nodeArray)
             errCode = CWResult.GetDetectedHotSpotElements(elemArray)
             CWCFf = CWResult.CreateStressHotSpotPlot(True, True, errCode)
         End If

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
