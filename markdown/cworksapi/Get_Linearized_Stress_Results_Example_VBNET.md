---
title: "Get Linearized Stress Results Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Linearized_Stress_Results_Example_VBNET.htm"
---

# Get Linearized Stress Results Example (VB.NET)

This example shows how to get the stress results that are linearized along Stress Classification Lines for a pressure vessel study.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 '  2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '     click  Tools > References > SOLIDWORKS Simulation version type library).
 '  3. Open  pubic_documents\Simulation Examples\pressurevessel.sldprt.
 '  4. Open the Immediate window.
 '  5. Mesh Ready-Solids using a curvature-based mesh with a maximum of 10 elements.
 '  6. Analyze Ready-Solids.
 '  7. Create Pressure Vessel Design 1 study, using a linear combination of
 '      Ready-Solids with Factor = 1.
 '  8. Analyze Pressure Vessel Design 1.
 '  9. Create a default von Mises stress plot of the results.
 '
 ' Postconditions:
 '  1. Gets the following stress values linearized along Stress Classification Lines
 '     for the specified points on the planar section created by the Top plane:
 '     * Membrane stress
 '     * Bending (Point 1) stress
 '     * Membrane stress + bending (Point 1) stress
 '     * Bending (Point 2) stress
 '     * Membrane stress + Bending (Point 2) stress
 '     * Peak (Point 1)
 '     * Peak (Point 2)
 '  2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 ' ---------------------------------------------------------------------------

 Partial   Class   SolidWorksMacro

     Dim Part  As   ModelDoc2
       Dim COSMOSWORKS  As  Object
       Dim CWObject  As  CwAddincallback
       Dim ActDoc  As  CWModelDoc
       Dim StudyMngr  As  CWStudyManager
       Dim Study  As  CWStudy
       Dim CWResult  As  CWResults
       Dim CWPlot  As  CWPlot
       Dim ReferenceGeometryDispatchObj2  As  Feature
       Dim plotNames  As  Object
       Dim values  As  Object
       Dim errCode  As  Long
       Dim boolCode  As  Boolean

       Sub main()

           Part = swApp.ActiveDoc
           CWObject = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
           COSMOSWORKS = CWObject.CosmosWorks
           ActDoc = COSMOSWORKS.ActiveDoc()
           StudyMngr = ActDoc.StudyManager()
           Study = StudyMngr.GetStudy(4)
           StudyMngr.ActiveStudy = 4

           CWResult = Study.Results
           plotNames = CWResult.GetPlotNames
           boolCode = CWResult.ActivatePlot("Stress1")

           CWPlot = CWResult.GetPlot("Stress1", errCode)

           boolCode = Part.Extension.SelectByID2("Top",   "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           ReferenceGeometryDispatchObj2 = Part.SelectionManager.GetSelectedObject6(1, -1)

           values = CWPlot.GetLinearizedStressValuesAlongSCL(5, 0.29224, -1.08E-19, -0.00034826, 0.30464, -2.17E-19, -0.00054522, ReferenceGeometryDispatchObj2, errCode)

            Debug.Print("Linearized normal stresses in the X-direction:")
            Debug.Print("  Membrane:                     " & values(0))
            Debug.Print("  Bending (Point 1):            " & values(1))
            Debug.Print("  Membrane + Bending (Point 1): " & values(2))
            Debug.Print("  Bending (Point 2):            " & values(3))
            Debug.Print("  Membrane + Bending (Point 2): " & values(4))
            Debug.Print("  Peak (Point 1):               " & values(5))
            Debug.Print("  Peak (Point 2):               " & values(6))

       End  Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
