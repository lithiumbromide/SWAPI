---
title: "Create Nonlinear Dynamic Plots Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Dynamic_Plots_Example_VBNET.htm"
---

# Create Nonlinear Dynamic Plots Example (VB.NET)

This example shows how to a create a plot of a specific solution step of a nonlinear dynamic study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
  '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

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

         Dim errCode As Integer
         Dim el As Double, tl As Double

         Dim Disp As Object, Stress As Object, Strn As Object

         Const URESMax As Double = 11.26     'nm
         Const URESMin As Double = 0.0#      'nm
         Const VONMax As Double = 0.00319    'MPa
         Const VONMin As Double = 0.00000895 'MPa

         Const MaxStrn As Double = 0.0000000395
         Const MinStrn As Double = 0.000000000033

         CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If CWAddinCallBack Is Nothing Then ErrorMsg(swApp, "No CWAddinCallBack object")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object")

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         'Get the Nonlinear1 study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager object")
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(1)
         If Study Is Nothing Then ErrorMsg(swApp, "No study object")

         'Mesh
         CWMesh = Study.Mesh
         If CWMesh Is Nothing Then ErrorMsg(swApp, "No mesh object")
         CWMesh.Quality = 0
         Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

         'Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed")

         'Get results
         CWResult = Study.results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No result object")

         'Create resultant displacement plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultDisplacementOrAmplitude, swsStaticResultDisplacementComponentTypes_e.swsStaticDisplacement_URES, swsUnit_e.swsUnitSI, False, errCode)
         If CWCFf Is Nothing Then ErrorMsg(swApp, "Failure to create plot")

         'Display plot of step 72
         errCode = CWCFf.SetPlotStepNumber(72)
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated for the given step")

         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated")

         'Get min/max resultant displacements from plot
         Disp = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No displacement results")

         If (Disp(1) < 0.95 * URESMin) Or (Disp(1) > 1.05 * URESMin) Then
             ErrorMsg(swApp, "URES minimum % error = " & (((Disp(1) - URESMin) / URESMin) * 100))
         End If

         If (Disp(3) < 0.95 * URESMax) Or (Disp(3) > 1.05 * URESMax) Then
             ErrorMsg(swApp, "URES maximum % error = " & (((Disp(3) - URESMax) / URESMax) * 100))
         End If

         'Create stress plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultStress, swsStaticResultNodalStressComponentTypes_e.swsStaticNodalStress_VON, swsUnit_e.swsUnitSI, False, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failure to create plot")

         'Display plot of step 72
         errCode = CWCFf.SetPlotStepNumber(72)
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated for the given step")

         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated")

         'Get min/max von Mises stresses from plot
         Stress = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No stress results")

         If (Stress(1) < 0.95 * VONMin) Or (Stress(1) > 1.05 * VONMin) Then
             ErrorMsg(swApp, " Minimum von Mises stress % error = " & (((Stress(1) - VONMin) / VONMin) * 100))
         End If

         If (Stress(3) < 0.95 * VONMax) Or (Stress(3) > 1.05 * VONMax) Then
             ErrorMsg(swApp, "Maximum von Mises stress % error = " & (((Stress(3) - VONMax) / VONMax) * 100))
         End If

         'Create equivalent elemental strain plot
         CWCFf = CWResult.CreatePlot(swsPlotResultTypes_e.swsResultStrain, swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ESTRN, swsUnit_e.swsUnitSI, True, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failure to create plot")

         'Display plot of step 72
         errCode = CWCFf.SetPlotStepNumber(72)
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated for the given step")

         errCode = CWCFf.ActivatePlot()
         If errCode <> 0 Then ErrorMsg(swApp, "Plot is not activated")

         'Get min/max strains from plot
         Strn = CWCFf.GetMinMaxResultValues(errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No strain results")

         If (Strn(1) < 0.95 * MinStrn) Or (Strn(1) > 1.05 * MinStrn) Then
             ErrorMsg(swApp, "Minimum strain % error = " & (((Strn(1) - MinStrn) / MinStrn) * 100))
         End If

         If (Strn(3) < 0.95 * MaxStrn) Or (Strn(3) > 1.05 * MaxStrn) Then
             ErrorMsg(swApp, "Maximum strain % error = " & (((Strn(3) - MaxStrn) / MaxStrn) * 100))
         End If

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End Class
```
