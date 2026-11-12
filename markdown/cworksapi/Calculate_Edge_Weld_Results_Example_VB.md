---
title: "Calculate Edge Weld Results Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Calculate_Edge_Weld_Results_Example_VB.htm"
---

# Calculate Edge Weld Results Example (VBA)

This example shows how to calculate the edge weld results for a specific edge weld connector.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
     Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim fileName        As String
     Dim errors          As Long
     Dim warnings        As Long
     Dim errCode         As Long
     Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc          As CosmosWorksLib.CWModelDoc
     Dim StudyMngr       As CosmosWorksLib.CWStudyManager
     Dim Study           As CosmosWorksLib.CWStudy
     Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
     Dim CWFeatObj       As Object
     Dim ConnectorName   As String
     Dim PassFail        As Boolean
     Dim EdgeResult      As Variant
     'Tolerances and baselines
     Const MeshEleSize       As Double = 1.4769 'mm
     Const MeshTol           As Double = 0.073847 'mm
     'Connect to SOLIDWORKS
     Set SwApp = Application.SldWorks
     If SwApp Is Nothing Then Exit Sub
     'Open document
     fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
     Set Part = SwApp.OpenDoc6(fileName, swDocPART, 1, "", errors, warnings)
     'Add-in callback
     Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     'Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     'Get study
     Set StudyMngr = ActDoc.StudyManager()
     Set Study = StudyMngr.GetStudy(0)
     Study.ActivateConfiguration
     StudyMngr.ActiveStudy = 0
     'Mesh
     Set CWFeatObj = Study.Mesh
     CWFeatObj.MesherType = 0
     CWFeatObj.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
     Set CWFeatObj = Nothing
     'Set solver type as FFEPlus
     Set StaticOptions = Study.StaticStudyOptions
     StaticOptions.SolverType = 2
     'Run analysis
     errCode = Study.RunAnalysis
     Set CWFeatObj = Study.Results
     'Get edge weld results
     ConnectorName = "Edge Weld Connector-1"
     EdgeResult = CWFeatObj.GetEdgeWeldResults(ConnectorName, swsUnitSI, PassFail, errCode)

     'Print results to Immediate window
     Dim i As Long
     Debug.Print ("Results: ")
     For i = 0 To UBound(EdgeResult)
         Debug.Print ("  " & EdgeResult(i))
     Next i

     'Delete study
     Call StudyMngr.DeleteStudy(Study.Name)

End Sub
```
