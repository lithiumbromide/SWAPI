---
title: "Create Body From Deformed Shape Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Body_From_Deformed_Shape_Example_VBNET.htm"
---

# Create Body From Deformed Shape Example (VB.NET)

This example shows how to save the deformed shape that results from running a static study.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that c:\temp exists.
 ' 4. Ensure that the specified model exists.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 '  1. Opens the model document.
 '  2. Adds a default elemental strain plot.
 '  3. Gets the static study.
 '  4. Meshes the model.
 '  5. Sets the solver type.
 '  6. Analyzes the study.
 '  7. Creates the Strain1 plot.
 '  8. Saves only the SOLIDWORKS body from the deformed shape in
 '     c:\temp\deformedBody.sldprt.
 '  9. Gets the size of the deform coordinate array.
 ' 10. Gets the plot definition of Strain1.
 ' 11. Inspect the Immediate window and c:\temp.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim fileName As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim errCode As Integer
         Dim COSMOSWORKS As CosmosWorks
         Dim CWAddinCallBack As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim StaticOptions As CWStaticStudyOptions
         Dim CWFeatObj As CWMesh
         Dim res As CWResults

         Const MeshEleSize As Double = 1.4769
         Const MeshTol As Double = 0.073847

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
         Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, 1, "", errors, warnings)

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS

         ActDoc = COSMOSWORKS.ActiveDoc()
         errCode = ActDoc.AddDefaultStaticStudyPlot(swsDefaultStaticResultTypes_e.swsStaticResultElementalStrain, swsStaticResultElementalStrainComponentTypes_e.swsStaticElementalStrain_ENERGY)

         StudyMngr = ActDoc.StudyManager()
         Study = StudyMngr.GetStudy(1)
         Study.ActivateConfiguration()
         StudyMngr.ActiveStudy = 1

         'Mesh
         CWFeatObj = Study.Mesh
         CWFeatObj.MesherType = 0
         CWFeatObj.Quality = 0
         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)
         CWFeatObj = Nothing

         'Set solver type to FFEPlus
         StaticOptions = Study.StaticStudyOptions
         StaticOptions.SolverType = 2

         'Run analysis
         errCode = Study.RunAnalysis

         res = Study.Results

         'Save only the SOLIDWORKS body from the deformed shape
         errCode = res.CreateDeformedBody2(swsCreateDeformedBodyOption_e.swsCreateDeformedBodyAsPart, swsCreateDeformedBodyAdvancedOption_e.swsCreateDeformedBodyAdvanced_OutputBodyOnly, 1, "deformedBody", "c:\temp")
         Debug.Print("Create deformed body result code as defined in swsCreateDeformedBodyError_e: " & errCode)
         Debug.Print("Option to use when the deformed body fails to sew into a solid object as defined in swsCreateDeformedBodyFailedSewOption_e: " & res.GetDeformedBodyFailedSewOption)

         Dim vCoord As Object
         Dim plotType As Integer
         Dim nComp As String = ""
         Dim bNodal As Boolean
         Dim bDeformed As Boolean
         Dim dScaleFactor As Double
         vCoord = res.GetDeformedCoord("Strain1", errCode)
         Debug.Print("Deformed coordinate array size: " & UBound(vCoord))

         errCode = res.GetPlotDefinition("Strain1", plotType, nComp, bNodal, bDeformed, dScaleFactor)
         Debug.Print("Plot definition")
         Debug.Print("  Name: Strain1")
         Debug.Print("  Type as defined in swsPlotResultTypes_e: " & plotType)
         Debug.Print("  Component name: " & nComp)
         Debug.Print("  Nodal? (True = nodal, False = elemental) " & bNodal)
         Debug.Print("  Deformed? " & bDeformed)
         Debug.Print("  Scale factor: " & dScaleFactor)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
