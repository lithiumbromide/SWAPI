---
title: "Calculate Edge Weld Results Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Calculate_Edge_Weld_Results_Example_VBNET.htm"
---

# Calculate Edge Weld Results Example (VB.NET)

This example shows how to calculate the edge weld results for a specific edge weld connector.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open the Immediate window.
 ' 4. Verify that the specified model exists.
 '
 ' Postconditions:
 ' 1. Opens the part document.
 ' 2. Meshes the part.
 ' 3. Sets the solver type.
 ' 4. Runs the analysis.
 ' 5. Gets the edge weld results for Edge Weld Connector-1.
  ' 6. Prints the edge weld results to the Immediate window.
 '
 ' NOTE: Because this part document is used elsewhere,
 ' do not save any changes when closing the document.
  '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim Part As ModelDoc2
         Dim fileName As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim errCode As Integer
         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWAddinCallBack As CWAddinCallBack
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim StaticOptions As CWStaticStudyOptions
         Dim CWFeatObj As Object
         Dim ConnectorName As String
         Dim PassFail As Boolean
         Dim EdgeResult As Object

         'Tolerances and baselines
         Const MeshEleSize As Double = 1.4769 'mm
         Const MeshTol As Double = 0.073847 'mm

         'Open document
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
         Part = SwApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, 1, "", errors, warnings)

         'Add-in callback
         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS

         'Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()

         'Get study
         StudyMngr = ActDoc.StudyManager()
         Study = StudyMngr.GetStudy(0)
         Study.ActivateConfiguration
         StudyMngr.ActiveStudy = 0

         'Mesh
         CWFeatObj = Study.Mesh
         CWFeatObj.MesherType = 0
         CWFeatObj.Quality = 0
         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
         CWFeatObj = Nothing

         'Set solver type as FFEPlus
         StaticOptions = Study.StaticStudyOptions
         StaticOptions.SolverType = 2

         'Run analysis
         errCode = Study.RunAnalysis

         CWFeatObj = Study.Results

         'Get edge weld results
         ConnectorName = "Edge Weld Connector-1"
         EdgeResult = CWFeatObj.GetEdgeWeldResults(ConnectorName, swsUnit_e.swsUnitSI, PassFail, errCode)

         'Print results to Immediate window
         Dim i As Long
         Debug.Print("Results: ")
         For i = 0 To UBound(EdgeResult)
             Debug.Print("  " & EdgeResult(i))
         Next i

         'Delete study
         Call StudyMngr.DeleteStudy(Study.Name)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
