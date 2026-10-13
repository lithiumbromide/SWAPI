---
title: "Get Frequencies in Mode Shape Plots Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Frequencies_in_Mode_Shape_Plots_Example_VBNET.htm"
---

# Get Frequencies in Mode Shape Plots Example (VB.NET)

This example shows how to get frequencies for all mode shapes in amplitude plots.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim COSMOSWORKS As COSMOSWORKS
     Dim CWAddinCallBack As CwAddincallback
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim CWResult As CWResults
     Dim mesh As CWMesh
     Dim errorCode As Integer
     Dim longstatus As Integer, longwarnings As Integer
     Dim TimeorFrequency As Object
     Dim ModeShapeNumber As Integer

     Const MeshEleSize As Double = 47.9 'mm
     Const MeshTol As Double = 2.39 'mm

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Dynamics\ac_unit.sldasm", swDocumentTypes_e.swDocASSEMBLY, 1, "", longstatus, longwarnings)

         CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
         ActDoc = COSMOSWORKS.ActiveDoc()
         StudyMngr = ActDoc.StudyManager()
         StudyMngr.ActiveStudy = 0
         Study = StudyMngr.GetStudy(0)

         mesh = Study.mesh
         mesh.MesherType = 0
         mesh.Quality = 0
         errorCode = Study.CreateMesh(0, MeshEleSize, MeshTol)

         errorCode = Study.RunAnalysis
         CWResult = Study.Results

         ModeShapeNumber = 2
         TimeorFrequency = CWResult.GetTimeOrFrequencyAtEachStep2(0, errorCode)
         MsgBox("Frequency for mode shape 2: " & TimeorFrequency(ModeShapeNumber - 1))

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
