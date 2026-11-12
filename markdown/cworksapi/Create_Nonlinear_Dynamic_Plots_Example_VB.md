---
title: "Create Nonlinear Dynamic Plots Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Dynamic_Plots_Example_VB.htm"
---

# Create Nonlinear Dynamic Plots Example (VBA)

This example shows how to a create a plot of a specific solution step of a nonlinear dynamic study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 ' 4. Create a nonlinear dynamic study.
 '
 ' Postconditions:
 ' 1. Activates Nonlinear1 study.
 ' 2. Meshes and analyzes the study.
 ' 3. Creates displacement, stress, and strain plots of solution step 72.
 ' 4. Gets the minimum and maximum values for the result plots.
 ' 5. Click OK to close any error dialog boxes.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------

Option Explicit
Sub main()

    Dim SwApp As SldWorks.SldWorks

    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CWMesh As CosmosWorksLib.CWMesh
     Dim CWResult As CosmosWorksLib.CWResults
     Dim CWCFf As CosmosWorksLib.CWPlot

    Dim errCode As Long
     Dim el As Double, tl As Double

    Dim Disp  As Variant, Stress As Variant, Strn As Variant

    Const URESMax As Double = 11.26      'nm
     Const URESMin As Double = 0#         'nm
     Const VONMax  As Double = 0.00319    'MPa
     Const VONMin  As Double = 0.00000895 'MPa

    Const MaxStrn  As Double = 0.0000000395
     Const MinStrn As Double = 0.000000000033

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "No CWAddinCallBack object"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"

    'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    'Get the Nonlinear1 study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No study manager object"
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(1)
     If Study Is Nothing Then ErrorMsg SwApp, "No study object"
    'Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
     CWMesh.Quality = 0
     Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    'Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed"

    'Get results
     Set CWResult = Study.results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object"

    'Create resultant displacement plot
     Set CWCFf = CWResult.CreatePlot(swsResultDisplacementOrAmplitude, swsStaticDisplacement_URES, swsUnitSI, False, errCode)
     If CWCFf Is Nothing Then ErrorMsg SwApp, "Failure to create plot"

    'Display plot of step 72
     errCode = CWCFf.SetPlotStepNumber(72)
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated for the given step"

    errCode = CWCFf.ActivatePlot()
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated"

    'Get min/max resultant displacements from plot
     Disp = CWCFf.GetMinMaxResultValues(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No displacement results"

    If (Disp(1) < 0.95 * URESMin) Or (Disp(1) > 1.05 * URESMin) Then
     ErrorMsg SwApp, "URES minimum % error = " & (((Disp(1) - URESMin) / URESMin) * 100)
     End If

    If (Disp(3) < 0.95 * URESMax) Or (Disp(3) > 1.05 * URESMax) Then
     ErrorMsg SwApp, "URES maximum % error = " & (((Disp(3) - URESMax) / URESMax) * 100)
     End If

    'Create stress plot
     Set CWCFf = CWResult.CreatePlot(swsResultStress, swsStaticNodalStress_VON, swsUnitSI, False, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failure to create plot"

    'Display plot of step 72
     errCode = CWCFf.SetPlotStepNumber(72)
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated for the given step"

    errCode = CWCFf.ActivatePlot()
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated"

    'Get min/max von Mises stresses from plot
     Stress = CWCFf.GetMinMaxResultValues(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No stress results"
    If (Stress(1) < 0.95 * VONMin) Or (Stress(1) > 1.05 * VONMin) Then
     ErrorMsg SwApp, " Minimum von Mises stress % error = " & (((Stress(1) - VONMin) / VONMin) * 100)
     End If

    If (Stress(3) < 0.95 * VONMax) Or (Stress(3) > 1.05 * VONMax) Then
     ErrorMsg SwApp, "Maximum von Mises stress % error = " & (((Stress(3) - VONMax) / VONMax) * 100)
     End If

    'Create equivalent elemental strain plot
     Set CWCFf = CWResult.CreatePlot(swsResultStrain, swsStaticElementalStrain_ESTRN, swsUnitSI, True, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failure to create plot"

    'Display plot of step 72
     errCode = CWCFf.SetPlotStepNumber(72)
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated for the given step"

    errCode = CWCFf.ActivatePlot()
     If errCode <> 0 Then ErrorMsg SwApp, "Plot is not activated"

    'Get min/max strains from plot
     Strn = CWCFf.GetMinMaxResultValues(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No strain results"

    If (Strn(1) < 0.95 * MinStrn) Or (Strn(1) > 1.05 * MinStrn) Then
     ErrorMsg SwApp, "Minimum strain % error = " & (((Strn(1) - MinStrn) / MinStrn) * 100)
     End If

    If (Strn(3) < 0.95 * MaxStrn) Or (Strn(3) > 1.05 * MaxStrn) Then
     ErrorMsg SwApp, "Maximum strain % error = " & (((Strn(3) - MaxStrn) / MaxStrn) * 100)
     End If

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
