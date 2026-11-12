---
title: "Create Frequency Study with Solid Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm"
---

# Create Frequency Study with Solid Mesh Example (VBA)

This example shows how to create a frequency study with solid mesh.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model exists.
 ' 4. Ensure that the specified material library exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly.
 ' 2. Specifies the default frequency study results plots.
 ' 3. Creates a frequency study.
 ' 4. Applies the same material to all bodies.
 ' 5. Creates a mesh with default global size and tolerance parameters.
 ' 6. Sets the number of frequencies.
 ' 7. Runs the analysis.
 ' 8. Gets the result frequencies and mass participation factors.
 ' 9. Inspect the results plots and the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 ' -----------------------------------------------------------------
Option Explicit

Sub main()

   Dim swApp As SldWorks.SldWorks
   Dim COSMOSWORKS As Object
   Dim COSMOSObject As CosmosWorksLib.CwAddincallback
   Dim ActDoc As CosmosWorksLib.CWModelDoc
   Dim StudyMngr As CosmosWorksLib.CWStudyManager
   Dim Study As CosmosWorksLib.CWStudy
   Dim SolidMgr As CosmosWorksLib.CWSolidManager
   Dim SolidComponent As CosmosWorksLib.CWSolidComponent
   Dim SolidBody As CosmosWorksLib.CWSolidBody
   Dim CwMesh As CosmosWorksLib.CwMesh
   Dim CWResult As CosmosWorksLib.CWResults
   Dim FrequencyOptions As CosmosWorksLib.CWFrequencyStudyOptions
   Dim CWMat As CosmosWorksLib.CWMaterial
   Dim longstatus As Long, longwarnings As Long
   Dim errCode As Long, errorCode As Long, pValue As Long
   Dim lStatus As Long
   Dim CompCount As Integer
   Dim BodyCount As Integer
   Dim j As Integer
   Dim i As Integer
   Dim bApp As Boolean
   Dim Freq As Variant
   Dim MassPart As Variant
   Dim el As Double, tl As Double

    ' Connect to SolidWork software
    If swApp Is Nothing Then Set swApp = Application.SldWorks

    ' Get SOLIDWORKS Simulation object
    Set COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
    If COSMOSObject Is Nothing Then ErrorMsg swApp, "COSMOSObject object not found"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "COSMOSWORKS object not found"

    ' Get active document
    swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg swApp, "No active document"

     ' Add default frequency study results plots of resultant amplitudes for all mode shapes
     errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(True, 0, True, swsFrequencyBucklingDisplacement_URES)

    ' Create new frequency study
    Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg swApp, "No CWStudyManager object"
    Set Study = StudyMngr.CreateNewStudy3("Frequency", swsAnalysisStudyTypeFrequency, swsMeshTypeSolid, errCode)
    If Study Is Nothing Then ErrorMsg swApp, "Study not created"

    ' Get number of solid components
    Set SolidMgr = Study.SolidManager
    If SolidMgr Is Nothing Then ErrorMsg swApp, "No CWSolidManager object"
    CompCount = SolidMgr.ComponentCount

    ' Apply SOLIDWORKS material to rest of components
    Set SolidBody = Nothing
    Set SolidComponent = Nothing
        For j = 0 To (CompCount - 1)
            Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
                BodyCount = SolidComponent.SolidBodyCount
          For i = 0 To (BodyCount - 1)
            Set SolidBody = SolidComponent.GetSolidBodyAt(i, errCode)
            If errCode <> 0 Then ErrorMsg swApp, "No solid body"
            bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
            If bApp = False Then ErrorMsg swApp, "No material applied"
            Set SolidBody = Nothing
          Next i
        Next j

    ' Set meshing
    Set CwMesh = Study.Mesh
    If CwMesh Is Nothing Then ErrorMsg swApp, "No mesh object"
    CwMesh.Quality = 1
    Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
    errCode = Study.CreateMesh(0, el, tl)
    If errCode <> 0 Then ErrorMsg swApp, "Mesh failed"

    ' Set frequency study options
     Set FrequencyOptions = Study.FrequencyStudyOptions
     If FrequencyOptions Is Nothing Then ErrorMsg swApp, "No CWFrequencyStudyOptions object"

    FrequencyOptions.Options = swsFrequencyStudyOptionNumberFrequencies
     FrequencyOptions.NoOfFrequencies = 8

    Debug.Print "Study: " & Study.Name
     Debug.Print "  Option as defined in swsFrequencyStudyOption_e: " & FrequencyOptions.Options
     If FrequencyOptions.Options = 1 Then
         Debug.Print "  Upper-bound frequency: " & FrequencyOptions.UpperBoundFrequency
     ElseIf FrequencyOptions.Options = 0 Then
         Debug.Print "  Number of frequencies: " & FrequencyOptions.NoOfFrequencies
         Debug.Print "  Calculate frequencies around a specified frequency? (True=yes, False=no): " & FrequencyOptions.UseLowerBoundFrequency
         If FrequencyOptions.UseLowerBoundFrequency2 Then
             Debug.Print "    Lower bound frequency: " & FrequencyOptions.LowerBoundFrequency
         End If
     End If

    Debug.Print "  Result folder: " & FrequencyOptions.ResultFolder
     Debug.Print "  Solver type as defined in swsSolverType_e: " & FrequencyOptions.SolverType
     Debug.Print "  Use soft spring to stabilize the model? (True=yes, False=no): " & FrequencyOptions.UseSoftSpring2
     Dim zeroStrainTemp As Double
     Dim tempUnit As Long
     FrequencyOptions.GetZeroStrainTemperature zeroStrainTemp, tempUnit
     Debug.Print "  Flow/Thermal Effects:"
     Debug.Print "    Temperature source as defined in swsThermalOption_e: " & FrequencyOptions.ThermalResults
     Debug.Print "    Temperature source:"
     If FrequencyOptions.ThermalResults = 1 Then
         Debug.Print "        Thermal study: " & FrequencyOptions.ThermalStudyName
         Debug.Print "        Time step of transient thermal study: " & FrequencyOptions.TimeStep
     ElseIf FrequencyOptions.ThermalResults = 2 Then
         Debug.Print "        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowTemperatureFile
     Else
         Debug.Print "        Model"
     End If
     Debug.Print "    Reference temperature at zero strain: " & zeroStrainTemp
    Debug.Print "    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (True=yes, False=no): " & FrequencyOptions.CheckFlowPressure2
     If FrequencyOptions.CheckFlowPressure2 Then
         Debug.Print "        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowPressureFile
         Debug.Print "        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & FrequencyOptions.ReferencePressureOption
         If Not FrequencyOptions.ReferencePressureOption Then
             Debug.Print "          Reference pressure offset: " & FrequencyOptions.DefinedReferencePressure
         End If
         Debug.Print "        Run as legacy study and import only the normal component of the pressure load? (True=yes, False=no): " & FrequencyOptions.CheckRunAsLegacy2
     End If

    ' Run analysis
    errCode = Study.RunAnalysis
    If errCode <> 0 Then ErrorMsg swApp, "Analysis failed"

    ' Get results: frequencies and mass participation factors
    Set CWResult = Study.Results
    If CWResult Is Nothing Then ErrorMsg swApp, "No result object"
    Freq = CWResult.GetResonantFrequencies(errCode)
    MassPart = CWResult.GetMassParticipation(errCode)
End Sub

' Error function
Function ErrorMsg(swApp As SldWorks.SldWorks, Message As String)
    swApp.SendMsgToUser2 Message, 0, 0
    swApp.RecordLine "'*** WARNING - General"
    swApp.RecordLine "'*** " & Message
    swApp.RecordLine ""
End Function
```
