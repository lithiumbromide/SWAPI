---
title: "Create Frequency Study with Solid Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm"
---

# Create Frequency Study with Solid Mesh Example (VB.NET)

This example shows how to create a frequency study with solid mesh.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim COSMOSWORKS As Object
        Dim COSMOSObject As CwAddincallback
        Dim ActDoc As CWModelDoc
        Dim StudyMngr As CWStudyManager
        Dim Study As CWStudy
        Dim SolidMgr As CWSolidManager
        Dim SolidComponent As CWSolidComponent
        Dim SolidBody As CWSolidBody
        Dim CwMesh As CwMesh
        Dim CWResult As CWResults
        Dim FrequencyOptions As CWFrequencyStudyOptions
        Dim longstatus As Integer, longwarnings As Integer
        Dim errCode As Integer, errorCode As Integer
        Dim CompCount As Integer
        Dim BodyCount As Integer
        Dim j As Integer
        Dim i As Integer
        Dim bApp As Boolean
        Dim Freq As Object
        Dim MassPart As Object
        Dim el As Double, tl As Double

        ' Get SOLIDWORKS Simulation object
        COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
        If COSMOSObject Is Nothing Then ErrorMsg("COSMOSObject object not found")
        COSMOSWORKS = COSMOSObject.COSMOSWORKS
        If COSMOSWORKS Is Nothing Then ErrorMsg("COSMOSWORKS object not found")

        ' Get active document
        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
        ActDoc = COSMOSWORKS.ActiveDoc()
        If ActDoc Is Nothing Then ErrorMsg("No active document")
```

```vb
        ' Add default frequency study results plots of resultant amplitudes for all mode shapes
         errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(True, 0, True, swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES)
```

```vb
        ' Create new frequency study
        StudyMngr = ActDoc.StudyManager()
        If StudyMngr Is Nothing Then ErrorMsg("No CWStudyManager object")
        Study = StudyMngr.CreateNewStudy3("Frequency", swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, swsMeshType_e.swsMeshTypeSolid, errCode)
        If Study Is Nothing Then ErrorMsg("Study not created")

        ' Get number of solid components
        SolidMgr = Study.SolidManager
        If SolidMgr Is Nothing Then ErrorMsg("No CWSolidManager object")
        CompCount = SolidMgr.ComponentCount

        ' Apply SOLIDWORKS material to rest of components
        SolidBody = Nothing
        SolidComponent = Nothing
        For j = 0 To (CompCount - 1)
            SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
            BodyCount = SolidComponent.SolidBodyCount
            For i = 0 To (BodyCount - 1)
                SolidBody = SolidComponent.GetSolidBodyAt(i, errCode)
                If errCode <> 0 Then ErrorMsg("No solid body")
                bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
                If bApp = False Then ErrorMsg("No material applied")
                SolidBody = Nothing
            Next i
        Next j

        ' Set meshing
        CwMesh = Study.Mesh
        If CwMesh Is Nothing Then ErrorMsg("No mesh object")
        CwMesh.Quality = 1
        Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
        errCode = Study.CreateMesh(0, el, tl)
        If errCode <> 0 Then ErrorMsg("Mesh failed")

          ' Set frequency study options
         FrequencyOptions = Study.FrequencyStudyOptions
         If FrequencyOptions Is Nothing Then ErrorMsg("No CWFrequencyStudyOptions object")

         FrequencyOptions.Options = swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies
         FrequencyOptions.NoOfFrequencies = 8

         Debug.Print("Study: " & Study.Name)
         Debug.Print("  Option as defined in swsFrequencyStudyOption_e: " & FrequencyOptions.Options)
         If FrequencyOptions.Options = 1 Then
             Debug.Print("  Upper-bound frequency: " & FrequencyOptions.UpperBoundFrequency)
         ElseIf FrequencyOptions.Options = 0 Then
             Debug.Print("  Number of frequencies: " & FrequencyOptions.NoOfFrequencies)
             Debug.Print("  Calculate frequencies around a specified frequency? (True=yes, False=no): " & FrequencyOptions.UseLowerBoundFrequency2)
             If FrequencyOptions.UseLowerBoundFrequency2 Then
                 Debug.Print("    Lower bound frequency: " & FrequencyOptions.LowerBoundFrequency)
             End If
         End If

         Debug.Print("  Result folder: " & FrequencyOptions.ResultFolder)
         Debug.Print("  Solver type as defined in swsSolverType_e: " & FrequencyOptions.SolverType)
         Debug.Print("  Use soft spring to stabilize the model? (True=yes, False=no): " & FrequencyOptions.UseSoftSpring2)
         Dim zeroStrainTemp As Double
         Dim tempUnit As Integer
         FrequencyOptions.GetZeroStrainTemperature(zeroStrainTemp, tempUnit)
         Debug.Print("  Flow/Thermal Effects:")
         Debug.Print("    Temperature source as defined in swsThermalOption_e: " & FrequencyOptions.ThermalResults)
         Debug.Print("    Temperature source:")
         If FrequencyOptions.ThermalResults = 1 Then
             Debug.Print("        Thermal study: " & FrequencyOptions.ThermalStudyName)
             Debug.Print("        Time step of transient thermal study: " & FrequencyOptions.TimeStep)
         ElseIf FrequencyOptions.ThermalResults = 2 Then
             Debug.Print("        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowTemperatureFile)
         Else
             Debug.Print("        Model")
         End If
         Debug.Print("    Reference temperature at zero strain: " & zeroStrainTemp)
         Debug.Print("    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (True=yes, False=no): " & FrequencyOptions.CheckFlowPressure2)
         If FrequencyOptions.CheckFlowPressure2 Then
             Debug.Print("        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowPressureFile)
             Debug.Print("        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & FrequencyOptions.ReferencePressureOption)
             If Not FrequencyOptions.ReferencePressureOption Then
                 Debug.Print("          Reference pressure offset: " & FrequencyOptions.DefinedReferencePressure)
             End If
             Debug.Print("        Run as legacy study and import only the normal component of the pressure load? (True=yes, False=no): " & FrequencyOptions.CheckRunAsLegacy2)
         End If

        ' Run analysis
        errCode = Study.RunAnalysis
        If errCode <> 0 Then ErrorMsg("Analysis failed")
        ' Get results: frequencies and mass participation factors
        CWResult = Study.Results
        If CWResult Is Nothing Then ErrorMsg("No result object")
        Freq = CWResult.GetResonantFrequencies(errCode)
        MassPart = CWResult.GetMassParticipation(errCode)
    End Sub

    ' Error routine
    Private Sub ErrorMsg(ByVal Message As String)
        swApp.SendMsgToUser2(Message, 0, 0)
        swApp.RecordLine("'*** WARNING - General")
        swApp.RecordLine("'*** " & Message)
        swApp.RecordLine("")
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
