---
title: "Create Fatigue Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Fatigue_Study_Example_VB.htm"
---

# Create Fatigue Study Example (VBA)

This example shows how to create a fatigue study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open, rebuild, and fix as needed public_documents\samples\tutorial\api\
 '    landing_gear.sldasm.
 ' 4. Activate Ready_Static.
 ' 5. Right-click BearingLoads-1 and click Edit Definition.
 ' 6. Select load-bearing faces that are concentric with the Z-axis of the
 '    selected coordinate system and click the green check mark.
 ' 7. Mesh the study.
 ' 8. Run the study.
 ' 9. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. A default fatigue study results plot is created.
 ' 2. Two fatigue studies are created and analyzed:
 '    * Fatigue_StudyAPIConst (constant amplitude fatigue study)
 '    * Fatigue_StudyAPIVariable (variable amplitude fatigue study)
 ' 3. Inspect the Immediate window for fatigue study options, fatigue events,
 '    and fatigue study analysis results.
 ' 4. Inspect the fatigue results plots.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Option Explicit
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub

 Function SelectByPID(Part As SldWorks.ModelDoc2, PIDName As String, PIDCollection As Collection) As Object
     Dim PID()       As Byte
     Dim PIDVariant  As Variant
     Dim PIDString   As String
     Dim EntityType  As Long
     Dim i           As Integer
     Dim SelObj      As Object
     Dim errCode     As Long

    'Get the string from the collection
     PIDString = ""
     PIDString = PIDCollection.Item(PIDName)

    'Parse the string into an array
     PIDVariant = Split(PIDString, ",")
     ReDim PID(UBound(PIDVariant))

    'Change to a byte array
     For i = 0 To (UBound(PIDVariant) - 1)
         PID(i) = PIDVariant(i)
     Next i

    'Select the entity
     Set SelObj = Part.Extension.GetObjectByPersistReference3((PID), errCode)
     Set SelectByPID = SelObj
     Set SelObj = Nothing
 End Function

 Function PIDInitializer() As Collection
    Dim PIDCollection As New Collection
         Dim selection1 As String
    'Constants
     selection1 = "255,18,0,0,3,0,0,0,255,254,255,27,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,45,0,49,0,64,0,108,0,97,0,110,0,100,0,105,0,110,0,103,0,95,0,103,0,101,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,57,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,3,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,104,67,0,58,0,92,0,68,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,32,0,97,0,110,0,100,0,32,0,83,0,101,0,116,0,116,0,105,0,110,0,103,0,115,0,92,0,97,0,116,0,114,0,105,0,118,0,101,0,100,0,105,0,92,0,77,0,121,0,32,0,68,0,111,0,99,0,117,0,109,0,101,0,110,0,116,0,115,0,92,0,99,"
     selection1 = selection1 & "0,111,0,115,0,109,0,111,0,115,0,95,0,115,0,117,0,112,0,112,0,111,0,114,0,116,0,92,0,50,0,48,0,48,0,54,0,98,0,101,0,116,0,97,0,92,0,76,0,97,0,110,0,100,0,105,0,110,0,103,0,32,0,71,0,101,0,97,0,114,0,92,0,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,12,85,0,112,0,112,0,114,0,115,0,119,0,97,0,121,0,95,0,108,0,110,0,107,0,2,0,0,247,212,198,52,0,138,187,76,66,1,0,0,0,0,0,0,0,18,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,32,0,0,0,0,0,0,0,138,187,76,66,8,0,0,0,166,214,198,52,14,0,0,0,3,128,0,0,5,128,8,0,8,0,0,0,166,214,198,52,13,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,166,214,198,52,1,0,0,0,255,255,255,255,0,0,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"
    'Store constants in a collection
     PIDCollection.Add selection1, "selection1"
    Set PIDInitializer = PIDCollection
 End Function

 Sub main()

    Dim SwApp               As SldWorks.SldWorks
     Dim Part                As SldWorks.ModelDoc2
     Dim COSMOSWORKS         As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack     As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc              As CosmosWorksLib.CWModelDoc
     Dim StudyMngr           As CosmosWorksLib.CWStudyManager
     Dim Study               As CosmosWorksLib.CWStudy
     Dim Study2              As CosmosWorksLib.CWStudy
     Dim Study3              As CosmosWorksLib.CWStudy
     Dim Study4              As CosmosWorksLib.CWStudy
     Dim CWFeatObj           As CosmosWorksLib.CWResults
     Dim FatigueOptions      As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent        As CosmosWorksLib.CWFatigueEvent
     Dim FatigueOptions2     As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent2       As CosmosWorksLib.CWFatigueEvent
     Dim FatigueOptions3     As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent3       As CosmosWorksLib.CWFatigueEvent
     Dim FatigueOptions4     As CosmosWorksLib.CWFatigueStudyOptions
     Dim FatigueEvent4       As CosmosWorksLib.CWFatigueEvent
     Dim fatEv               As CosmosWorksLib.CWFatigueEvent
     Dim PointsX             As Variant
     Dim PointsY             As Variant
     Dim PointsX_2           As Variant
     Dim PointsY_2           As Variant
     Dim errCode             As Long
     Dim Disp                As Variant
     Dim VarStudyNames       As Variant
     Dim VarScales           As Variant
     Dim VarSteps            As Variant
     Dim AssocCounts         As Long
     Dim VarNewStudyNames    As Variant
     Dim VarNewScales        As Variant
     Dim VarNewSteps         As Variant
     Dim VarVertices         As Variant
     Dim bchecked            As Long
     Dim dcycles             As Double
     Dim lhCurve             As Variant
     Dim ntype               As Long
     Dim dsamplingrate       As Double
     Dim nnoofbins           As Long
     Dim npercentfilterloadcycles As Long

    Dim PIDCollection As New Collection
     Set PIDCollection = PIDInitializer()

    Set SwApp = Application.SldWorks

    Set Part = SwApp.ActiveDoc

    VarVertices = Array(SelectByPID(Part, "selection1", PIDCollection))

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

    'Create constant amplitude fatigue study
     Debug.Print "Creating constant amplitude fatigue study Fatigue_StudyAPIConst..."
     Set Study = StudyMngr.CreateNewStudy3("Fatigue_StudyAPIConst", swsAnalysisStudyTypeFatigue, 0, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to create new study"

    errCode = Study.SetFatigueResultOptions(1, Nothing)

    Set FatigueOptions = Study.FatigueStudyOptions
     If FatigueOptions Is Nothing Then ErrorMsg SwApp, "Failed to get CWFatigueStudyOptions object"

    Set FatigueEvent = FatigueOptions.AddFatigueEventForConstantAmplitude("Ready_Static", -0.002, 1, errCode)
     FatigueEvent.SuppressUnSuppress 'suppress event
     FatigueEvent.SuppressUnSuppress 'unsuppress event
    AssocCounts = FatigueEvent.GetStudyAssociationData(VarStudyNames, VarScales, VarSteps)

    FatigueEvent.FatigueEventBeginEdit
     FatigueEvent.Cycles2 = 500.0
     FatigueEvent.LoadingRatio = 8.9
     FatigueEvent.LoadingType = 2 ' Loading ratio
     VarNewScales = Array(5.6)
     VarNewStudyNames = Array("Ready_Static")
     VarNewSteps = Array(9)
     errCode = FatigueEvent.SetStudyAssociationData(1, (VarNewStudyNames), (VarNewScales), (VarNewSteps))
     errCode = FatigueEvent.FatigueEventEndEdit()

     Set fatEv = FatigueOptions.GetFatigueEvent(0, errCode)
     Debug.Print "  Name of constant amplitude fatigue event is: " & fatEv.Name
     Debug.Print "  Number of loading events in this fatigue study: " & FatigueOptions.LoadingEventCount
     Debug.Print "  Result folder: " & FatigueOptions.ResultFolder
     Debug.Print "  Shell face option as defined in swsShellFace_e: " & FatigueOptions.ShellFace

     FatigueOptions.GetInfiniteLifeSettings2 bchecked, dcycles
     Debug.Print "  Fatigue study infinite life settings checked? (-1 = yes) " & bchecked
     Debug.Print "  Number of cycles to use: " & dcycles
     Debug.Print "  Event interaction type as defined in swsFatigueEventInteraction_e: " & FatigueOptions.ConstantAmplitudeEventInteractionOption
     Debug.Print "  Computing alternating stress option as defined in swsFatigueAlternatingStressOption_e: " & FatigueOptions.ComputingAlternatingStressOption
     Debug.Print "  Fatigue strength reduction factor: " & FatigueOptions.FatigueStrengthReductionFactor
     Debug.Print "  Mean stress correction option as defined in swsFatigueMeanStressCorrectionType_e: " & FatigueOptions.MeanStressCorrectionOption
    errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code " & errCode

    'Create variable amplitude fatigue study
     Debug.Print ""
     Debug.Print "Creating variable amplitude fatigue study Fatigue_StudyAPIVariable..."
     Set Study2 = StudyMngr.CreateNewStudy3("Fatigue_StudyAPIVariable", swsAnalysisStudyTypeFatigue, 1, errCode)
     If Study2 Is Nothing Then ErrorMsg SwApp, "Failed to create new study"

    errCode = Study2.SetFatigueResultOptions(1, (VarVertices))

    Set FatigueOptions2 = Study2.FatigueStudyOptions
     If FatigueOptions2 Is Nothing Then ErrorMsg SwApp, "Failed to get CWFatigueStudyOptions object"

    PointsX = Array(0, 1, 2, 3, 4, 5, 6.25714, 7, 8.3846, 9, 10)
     PointsY = Array(0, 11, 21, 33, 44, 21, 66.25714, 77, 88.3846, 99, 109)
     Set FatigueEvent2 = FatigueOptions2.AddFatigueEventForVariableAmplitude("Ready_Static", -0.002, 1, (PointsX), (PointsY), 0, 1#, errCode)

    Set fatEv = FatigueOptions2.GetFatigueEvent(0, errCode)
     Debug.Print "  Name of variable amplitude fatigue event is " & fatEv.Name
    Debug.Print "  Number of repeats: " & FatigueEvent2.NoOfRepeats
     Debug.Print "  Start times: " & FatigueEvent2.StartTimes

    FatigueEvent2.FatigueEventBeginEdit
     PointsX_2 = Array(0, 1, 2, 3, 4, 5, 6.25714, 7, 8.3846, 9, 10, 11, 20)
     PointsY_2 = Array(0, 11, 21, 33, 44, 21, 66.25714, 77, 88.3846, 99, 109, 66, 12)
     errCode = FatigueEvent2.SetLoadHistoryCurve((PointsX_2), (PointsY_2), 2, 1.8)
     errCode = FatigueEvent2.FatigueEventEndEdit()

     lhCurve = FatigueEvent2.GetLoadHistoryCurve(ntype, dsamplingrate)
     Debug.Print "  Type of load history curve as defined in swsFatigueLoadHistoryCurveType_e: " & ntype
     Debug.Print "  Sampling rate in seconds: " & dsamplingrate
     Debug.Print "  Number of pairs of load history curve data: " & lhCurve(0)
     Debug.Print "  Load history curve [time, amplitude] data:"
     Debug.Print "  " & lhCurve(1) & ", " & lhCurve(2)
     Debug.Print "  " & lhCurve(3) & ", " & lhCurve(4)
     Debug.Print "  " & lhCurve(5) & ", " & lhCurve(6)
     Debug.Print "  " & lhCurve(7) & ", " & lhCurve(8)
     Debug.Print "  " & lhCurve(9) & ", " & lhCurve(10)
     Debug.Print "  " & lhCurve(11) & ", " & lhCurve(12)
     Debug.Print "  " & lhCurve(13) & ", " & lhCurve(14)
     Debug.Print "  " & lhCurve(15) & ", " & lhCurve(16)
     Debug.Print "  " & lhCurve(17) & ", " & lhCurve(18)
     Debug.Print "  " & lhCurve(19) & ", " & lhCurve(20)
     Debug.Print "  " & lhCurve(21) & ", " & lhCurve(22)
     Debug.Print "  " & lhCurve(23) & ", " & lhCurve(24)
     Debug.Print "  " & lhCurve(25) & ", " & lhCurve(26)

    Debug.Print "  Number of loading events in this fatigue study: " & FatigueOptions2.LoadingEventCount
     Debug.Print "  Result folder: " & FatigueOptions2.ResultFolder
     Debug.Print "  Shell face option as defined in swsShellFace_e: " & FatigueOptions2.ShellFace

    FatigueOptions2.GetInfiniteLifeSettings bchecked, dcycles
     FatigueOptions2.GetVariableAmplitudeEventOptions nnoofbins, npercentfilterloadcycles
     Debug.Print "  Fatigue study infinite life settings checked? (1 = yes) " & bchecked
     Debug.Print "  Number of cycles to use: " & dcycles
     Debug.Print "  Number of equally spaced buckets in which to distribute the load: " & nnoofbins
     Debug.Print "  Filter load cycles below this percentage of maximum load: " & npercentfilterloadcycles
     Debug.Print "  Computing alternating stress option as defined in swsFatigueAlternatingStressOption_e: " & FatigueOptions2.ComputingAlternatingStressOption
     Debug.Print "  Fatigue strength reduction factor: " & FatigueOptions2.FatigueStrengthReductionFactor
     Debug.Print "  Mean stress correction option as defined in swsFatigueMeanStressCorrectionType_e: " & FatigueOptions2.MeanStressCorrectionOption

    errCode = Study2.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code " & errCode
    Set CWFeatObj = Study2.Results
     If CWFeatObj Is Nothing Then ErrorMsg SwApp, "Failed to get CWResults object"
    'Get minimum/maximum fatigue
     Disp = CWFeatObj.GetMinMaxFatigue(0, errCode)
     Debug.Print "  Minimum fatigue is " & Disp(1) & " at node " & Disp(0)
     Debug.Print "  Maximum fatigue is " & Disp(3) & " at node " & Disp(2)

 End Sub
```
