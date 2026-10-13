---
title: "Create Fatigue Study for Dynamic Harmonic Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_for_Dynamic_Harmonic_Study_Example_VB.htm"
---

# Create Fatigue Study for Dynamic Harmonic Study Example (VBA)

This example shows how to create a fatigue study for a linear dynamic harmonic study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\Dynamics\ac_unit.sldasm.
 ' 4. Activate Sample_Harmonic.
 ' 5. Expand Parts in the Simulation design tree and apply Ductile Iron (SN)
 '    to all parts (right-click a part, click Apply/Edit Material,
 '    select SOLIDWORKS Materials > Iron > Ductile Iron (SN), and click Apply).
 ' 6. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates study, HarmonicFatigue.
 ' 2. Adds a fatigue event for step 15 of Sample_Harmonic.
 ' 3. Analyzes HarmonicFatigue.
 ' 4. Displays a message box with the damage percent error.
 ' 5. Click OK in the message box.
 ' 6. Prints the minimum and maximum fatigue to the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Option Explicit

Sub main()
    Dim SwApp               As SldWorks.SldWorks
     Dim COSMOSWORKS         As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack     As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc              As CosmosWorksLib.CWModelDoc
     Dim StudyMngr           As CosmosWorksLib.CWStudyManager
     Dim Study               As CosmosWorksLib.CWStudy
     Dim CWFeatObj           As CosmosWorksLib.CWResults
     Dim FatigueOptions      As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent        As CosmosWorksLib.CWFatigueEvent
     Dim errCode             As Long
     Dim Damage              As Variant
    Const Tol           As Double = 0.05   '5% damage tolerance
     Const DamageMax     As Double = 63.68  '63.68% maximum damage

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWAddinCallBack Is Nothing Then ErrorMsg SwApp, "CWAddinCallBack object not found"
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"

    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"

    ' Add default fatigue study results plot
     errCode = ActDoc.AddDefaultFatigueStudyPlot(swsFatigueStudy_DamagePlot)

    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get CWStudyManager object"

    ' Create harmonic fatigue study
     Debug.Print "Creating HarmonicFatigue study..."

    Set Study = StudyMngr.CreateNewStudy3("HarmonicFatigue", swsAnalysisStudyTypeFatigue, 2, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to create new study"

    errCode = Study.SetFatigueResultOptions(1, Nothing)

    Set FatigueOptions = Study.FatigueStudyOptions
     If FatigueOptions Is Nothing Then ErrorMsg SwApp, "Failed to get CWFatigueStudyOptions object"

    Set FatigueEvent = FatigueOptions.AddFatigueEventForHarmonic("Sample_Harmonic", 0, 15, 100000, 150000, errCode)
     FatigueEvent.SuppressUnSuppress 'suppress event
     FatigueEvent.SuppressUnSuppress 'unsuppress event

    errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    Set CWFeatObj = Study.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"
    ' Get minimum and maximum fatigue values
     Damage = CWFeatObj.GetMinMaxFatigue(1, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get minimum and maximum fatigue. Error code as defined in swsResultsError_e: " & errCode

    ' Report damage percent error if result maximum fatigue value is not within tolerance
     If (Damage(3) < (1 - Tol) * DamageMax) Or (Damage(3) > (1 + Tol) * DamageMax) Then
         ErrorMsg SwApp, "Damage % error = " & (((Damage(3) - DamageMax) / DamageMax) * 100)
     End If

    Debug.Print "  Minimum fatigue is " & Damage(1) & " at node " & Damage(0) & "."
     Debug.Print "  Maximum fatigue is " & Damage(3) & " at node " & Damage(2) & "."

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
