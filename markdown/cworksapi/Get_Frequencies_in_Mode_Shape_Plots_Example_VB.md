---
title: "Get Frequencies in Mode Shape Plots Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Frequencies_in_Mode_Shape_Plots_Example_VB.htm"
---

# Get Frequencies in Mode Shape Plots Example (VBA)

This example shows how to get frequencies for all mode shapes in amplitude plots.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model exists.
 '
 ' Postconditions:
 ' 1. Meshes the model.
 ' 2. Analyzes the study.
 ' 3. Gets the frequencies of all amplitude plot mode shapes.
 ' 4. Displays a message box with the frequency for mode shape 2.
 ' 5. Click OK.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim CWResult As CosmosWorksLib.CWResults
 Dim mesh As CosmosWorksLib.CWMesh
 Dim errorCode As Long
 Dim longstatus As Long, longwarnings As Long
 Dim TimeorFrequency As Variant
 Dim ModeShapeNumber As Integer
Const MeshEleSize As Double = 47.9 'mm
 Const MeshTol As Double = 2.39 'mm
Option Explicit
 Sub main()

    Set SwApp = Application.SldWorks
     Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Dynamics\ac_unit.sldasm", swDocASSEMBLY, 1, "", longstatus, longwarnings)

    Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     Set StudyMngr = ActDoc.StudyManager()
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(0)
    Set mesh = Study.mesh
     mesh.MesherType = 0
     mesh.Quality = 0
     errorCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
    errorCode = Study.RunAnalysis
     Set CWResult = Study.Results

    ModeShapeNumber = 2
     TimeorFrequency = CWResult.GetTimeOrFrequencyAtEachStep2(0, errorCode)
     MsgBox ("Frequency for mode shape 2: " & TimeorFrequency(ModeShapeNumber - 1))

End Sub
```
