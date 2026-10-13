---
title: "Analyze Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Analyze_Part_Example_VB.htm"
---

# Analyze Part Example (VBA)

This example shows how to perform a static analysis of a part and plot nodal strain results.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 '  1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '     Tools > Add-ins > SOLIDWORKS Simulation > OK).
 '  2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '     click Tools > References > SOLIDWORKS Simulation version type library).
 '  3. Modify the path to solidworks materials.sldmat as needed.
 '  4. Ensure that the specified part exists.
 '  5. Open the Immediate window.
 '
 ' Postconditions:
 '  1. Adds a default static study results plot.
 '  2. Creates study, Static_solid.
 '  3. Applies material to the model.
 '  4. Applies restraints and pressure to the selected faces.
 '  5. Creates a mesh.
 '  6. Runs the analysis.
 '  7. Prints strain and stress results to the Immediate window.
 '  8. Creates a nodal equivalent strain plot of the results.
 '  9. Prints plot data to the Immediate window.
 ' 10. Hides fixture and force symbols. Examine the graphics area
 '     to verify.
 ' 11. Press F5 to continue.
 ' 12. Shows fixture and force symbols. Examine the graphics area
 '     to verify.
 ' 13. Inspect the plots.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '-----------------------------------------------------------------------------
Option Explicit
Sub main()
     Dim SwApp As SldWorks.SldWorks
     Dim COSMOSWORKS As Object
     Dim CWObject As CosmosWorksLib.CwAddincallback
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim SolidMgr As CosmosWorksLib.CWSolidManager
     Dim SolidComponent As CosmosWorksLib.CWSolidComponent
     Dim SolidBody As CosmosWorksLib.CWSolidBody
     Dim CwMesh As CosmosWorksLib.CwMesh
     Dim CWResult As CosmosWorksLib.CWResults
     Dim Part As SldWorks.ModelDoc2
     Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim CWPressure As CosmosWorksLib.CWPressure
     Dim CWRes1 As CosmosWorksLib.CWRestraint
     Dim pointer1 As Object, pointer2 As Object, pointer3 As Object, pointer4 As Object
     Dim CWMat As CosmosWorksLib.CWMaterial
     Dim var1 As Variant, var2 As Variant, var3 As Variant, var4 As Variant
     Dim varArray1 As Variant
     Dim varArray2 As Variant
     Dim stress As Variant
     Dim bApp As Boolean
     Dim selection1 As String
     Dim selection2 As String
     Dim selection3 As String
     Dim selection4 As String
     Dim longstatus As Long, longwarnings As Long
     Dim errCode As Long
     Dim NSource As Long
     Dim el As Double, tl As Double
     Dim errorCode As Long
     Dim results As Variant
     Dim plot As CosmosWorksLib.CWPlot
     Dim plotName As String
     Dim i As Long
     Dim status As Long
     Dim entity(0) As SldWorks.entity
     Dim nType As Long
     Dim nBase As Long
     Dim nContour As Long
     Dim BFlip As Boolean
     Dim BSpecifyColorLimit As Boolean
     Dim VarColor As Variant
     Dim vDispOptions As Variant
     Dim vPlotPosFormatOptions As Variant
     Dim vPlotSettings As Variant
     Dim Name As Variant
     Dim Color As Variant
     Dim selEntity As Variant
     Dim InputVar1 as Variant
     Dim Var as Variant
    Dim oSelect2 As Object
     Dim boolstatus As Boolean

     ' Connect to SOLIDWORKS
     If SwApp Is Nothing Then Set SwApp = Application.SldWorks
     ' Open SOLIDWORKS part document
     Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Tutor1.SLDPRT ", swDocPART, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Tutor1.SLDPRT."

    ' Insert a coordinate system
     boolstatus = Part.Extension.SelectByID2("", "FACE", 0.170849242404917, 8.98492424049175E-02, -0.031, False, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.101612421576135, 1.02144219597449E-02, -3.03238444132603E-04, True, 2, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.16010192941178, 1.63935978611676E-02, -3.91019294117427E-02, True, 4, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.160121414911089, 9.91414669255164E-03, -2.84339843419161E-02, True, 8, Nothing, 0)
     boolstatus = Part.InsertCoordinateSystem(False, False, False)

    selection1 = "233,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,131,0,0,0"
     selection1 = selection1 & ",Type=1"
    StringtoArray selection1, var2
     Set oSelect2 = Part.Extension.GetObjectByPersistReference3((var2), status)
     'Get SOLIDWORKS Simulation object
     Set CWObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWObject Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
     Set COSMOSWORKS = CWObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No CosmosWorks object"
     ' Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

     ' Add default static study results plot
     errCode = ActDoc.AddDefaultStaticStudyPlot(swsStaticResultElementalStrain, swsStaticElementalStrain_ENERGY)

    ' Set default plot boundary color
     errCode = ActDoc.SetSimulationOptionDefaultPlotsBoundaryColorInRGB(swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh, 0, 0, 255)
     errCode = ActDoc.SetSimulationOptionDefaultPlotsBoundaryColorInRGB(swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_TranslucentSingleColor, 255, 0, 0)
    ' Get default plot model or mesh boundary color
     Dim colorObj As Variant
     colorObj = ActDoc.GetSimulationOptionDefaultPlotsBoundaryColorInRGB(swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh, errCode)
     Debug.Print "RGB values for model or mesh:"
     For i = 0 To UBound(colorObj)
         Debug.Print colorObj(i)
     Next
     ' Create new static study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     Set Study = StudyMngr.CreateNewStudy3("Static_solid", swsAnalysisStudyTypeStatic, swsMeshTypeSolid, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"
     ' Set material from the SOLIDWORKS material library
     Set SolidMgr = Study.SolidManager
     If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
     Set SolidComponent = SolidMgr.GetComponentAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No solid component"
     Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
     bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
     If bApp = False Then ErrorMsg SwApp, "No material applied"
     Set CWMat = SolidBody.GetDefaultMaterial
     NSource = CWMat.Source

    ' Get the PIDs of the faces
     ' First two selections are the faces for restraints
     ' Third selection is the face where pressure is applied
     ' Fourth selection is the direction reference face
     selection1 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,21,0,109,111,76,80,97,116,116,101,114,110,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,65,0,0,0,0"
     selection1 = selection1 & ",2,0,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,17,0,0,0,156,231,186,50,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,14,0,0,0,88,231,186,50,3,0,0,0,1,0,0,0,0,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,0,0,17,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,0,0,0,0,255,255,255,255,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"
     StringtoArray selection1, var1
     Set pointer1 = Part.Extension.GetObjectByPersistReference3((var1), longstatus)
    selection2 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,"
     selection2 = selection2 & "65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,14,0,0,0,88,231,186,50,3,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,0,0,14,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,0,0,0,0,255,255,255,255,0,0,0,0,0,0"
     selection2 = selection2 & ",Type=1"
     StringtoArray selection2, var2
     Set pointer2 = Part.Extension.GetObjectByPersistReference3((var2), longstatus)
    selection3 = "216,14,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,84,0,117,0,116,0,111,0,114,0,49,0,123,228,186,50,11,128,255,254,255,62,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,87,0,111,0,114,0,107,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,84,0,117,0,116,0,111,0,114,0,49,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,97,23,28,65,0,0,0,0,2,0,"
     selection3 = selection3 & "1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,51,230,186,50,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,218,229,186,50,4,0,0,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,1,0,0,0,2,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,1,0,0,0,1,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,2,0,0,0,3,0,0,0,17,128,0,0,5,128,8,0,31,0,0,0,210,195,223,50,17,128,0,0,5,128,8,0,23,0,0,0,160,192,223,50,14,"
     selection3 = selection3 & "128,0,0,5,128,8,0,19,0,0,0,181,233,186,50,1,0,0,0,2,0,0,0,4,0,0,0,0,0,0,0,0,0"
     selection3 = selection3 & ",Type=1"
     StringtoArray selection3, var3
     Set pointer3 = Part.Extension.GetObjectByPersistReference3((var3), longstatus)
    selection4 = "189,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,10,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,77,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,49,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,117,0,116,0,111,0,114,0,49,0,2,0,0,123,228,186,50,255"
     selection4 = selection4 & ",254,255,0,0,97,23,28,65,1,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,97,23,28,65,6,0,0,0,211,228,186,50,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,13,0,0,0,1,231,186,50,1,0,0,0,3,128,0,0,5,128,8,0,8,0,0,0,218,229,186,50,1,0,0,0,255,255,255,255,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,2,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,3,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,4,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,5,0,0,0,12,128,0,0,5,128,8,0,6,0,0,0,211,228,186,50,6,0,0,0,12,128,0,0,5,128,8,0,13,0,0,0,1,231,186,50,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection4 = selection4 & ",Type=1"
     StringtoArray selection4, var4
     Set pointer4 = Part.Extension.GetObjectByPersistReference3((var4), longstatus)
    varArray1 = Array(pointer1, pointer2)
     varArray2 = Array(pointer3)
    ' Add a restraint that uses reference geometry
     Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "No CWLoadsAndRestraintsManager object"
     Set CWRes1 = LBCMgr.AddRestraint(5, (varArray1), pointer4, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No restraint created"

    CWRes1.RestraintBeginEdit
     CWRes1.SetTranslationComponentsValues 1, 1, 1, 1, 1, 1
     errCode = CWRes1.RestraintEndEdit

    Debug.Print "Coordinate system type as defined in swsCoordinateType_e: " & CWRes1.GetCoordinateType
     Debug.Print "Restraint type as defined in swsRestraintType_e: " & CWRes1.RestraintType
     Debug.Print "Units of translation as defined in swsLinearUnit_e: " & CWRes1.Unit

    Dim bval1 As Long, bval2 As Long, bval3 As Long
     Dim brev1 As Long, brev2 As Long, brev3 As Long, brev4 As Long, brev5 As Long, brev6 As Long
     Dim dval1 As Double, dval2 As Double, dval3 As Double

    CWRes1.GetReverseDirections brev1, brev2, brev3, brev4, brev5, brev6
    CWRes1.GetTranslationComponentsValues bval1, bval2, bval3, dval1, dval2, dval3

     If bval1 = 1 Then
         Debug.Print " Translation along plane direction 1: " & dval1
         Debug.Print "      Reverse? (1=yes, 0=no): " & brev4
     End If
     If bval2 = 1 Then
         Debug.Print " Translation along plane direction 2: " & dval2
         Debug.Print "      Reverse? (1=yes, 0=no): " & brev5
     End If
     If bval3 = 1 Then
         Debug.Print " Translation along direction normal to the plane: " & dval3
         Debug.Print "      Reverse? (1=yes, 0=no): " & brev6
     End If

     ' Apply a nonuniform pressure normal to the selected face
     Set CWPressure = LBCMgr.AddPressure(0, (varArray2), Nothing, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No CWPressure object"
     Call CWPressure.PressureBeginEdit
     CWPressure.Unit = 1
     CWPressure.Value = 1000
     CWPressure.IncludeNonUniformDistribution = 1
     CWPressure.SetCoordinateSystem oSelect2
     CWPressure.CoordSystemType = swsCoordinateTypeCartesian
     CWPressure.Equation = ".4*""x"" + .8* ""y"" + .6* ""z"""
     errCode = CWPressure.PressureEndEdit
     If errCode <> 0 Then ErrorMsg SwApp, "Pressure not set with error code as defined in swsPressureEndEditError_e: " & errCode
    Debug.Print "Pressure type as defined in swsPressureType_e: " & CWPressure.PressureType
     Debug.Print "Pressure: " & CWPressure.Value
     Debug.Print "  Reverse direction? (True=yes, False=no) " & CWPressure.ReverseDirection2
     Debug.Print "  Include nonuniform distribution of pressure? (1=yes, 0=no) " & CWPressure.IncludeNonUniformDistribution

    If CWPressure.IncludeNonUniformDistribution = 1 Then
         Debug.Print "  Equation: " & CWPressure.Equation
         Debug.Print "  Coordinate system type as defined in swsCoordinateType_e: " & CWPressure.CoordSystemType
         If CWPressure.CoordSystemType = 1 Then
             Debug.Print "  Equation linear units as defined in swsLinearUnit_e: " & CWPressure.EquationLinearUnit
         End If
         If CWPressure.CoordSystemType = 2 Or CWPressure.CoordSystemType = 3 Then
             Debug.Print "  Equation angular units as defined in " & CWPressure.EquationAngularUnit
         End If
     End If
    ' Mesh
     Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CwMesh.Quality = 1
     Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
     ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No CWResults object"
     stress = CWResult.GetMinMaxStress(0, 0, 1, Nothing, 0, errCode)
     ' Get strain and stress results for
     ' first face selected for restraint

     Set entity(0) = pointer1
     i = 0
     Debug.Print "  Strain value by node:"
     For Each selEntity In CWResult.GetStrainForEntities3(True, swsStrainComponent_e.swsStrainComponentESTRN, 1, Nothing, (entity), status, 0, False, errCode)
         Debug.Print "     " & selEntity
     Next
     Debug.Print " "
     Debug.Print "  Stress value by node:"
     For Each selEntity In CWResult.GetStressForEntities3(True, swsStressComponent_e.swsStressComponentVON, 1, Nothing, (entity), swsStrengthUnitPascal, status, 0, False, errCode)
         Debug.Print "     " & selEntity
     Next
    ' Create a nodal equivalent strain plot
     Set plot = CWResult.CreatePlot(3, swsStaticNodalStrain_ESTRN, swsUnitSI, False, errorCode)
    errorCode = plot.ActivatePlot
     errorCode = plot.GetPlotName(plotName)
     errorCode = plot.ApplyNameViewOrientation("*Front")
     results = plot.GetMinMaxResultValues(errorCode)
     errorCode = plot.SetPlotTitle("Nodal Equivalent Strain")
     plot.SetFOSPlot (False)
     plot.Set2DPlanarRevolveAngle (0#)
     plot.SetNormalizeModeShape (False)
     plot.ShowAs3DPlot (True)
     plot.ShowTensorOrVector (False)
     plot.ShowShellin3D (False)
     plot.ShowNormalizeValuesFrom0To1 (True)
     errorCode = plot.ShowDeformedPlot(True, swsAutomatic, 0, True)
     plot.ShowBeamProfile (False)
     plot.ShowAvgResultsAcrossBoundaryForParts (False)
    Debug.Print "Result plot created: " & plotName
     Debug.Print "Node " & results(0) & " " & "has minimum strain value: " & results(1)
     Debug.Print "Node " & results(2) & " " & "has maximum strain value: " & results(3)
     Debug.Print "Number of plots for these results: " & CWResult.GetPlotCount
    For Each Name In CWResult.GetPlotNames
         Debug.Print ""
         Debug.Print "Plot: " & Name
         errorCode = CWResult.GetPlotColorOptions(Name, nType, nBase, nContour, BFlip, BSpecifyColorLimit, VarColor)
         Debug.Print "Plot color options:"
         Debug.Print "  Color map as defined in swsColorChartOptionLegendTypeValue_e: " & nType
         Debug.Print "  Number of base colors in color map: " & nBase
         Debug.Print "  Number of gradient colors in color map: " & nContour
         Debug.Print "  Reverse the color mapping? " & BFlip
         Debug.Print "  Specify a color for values above the yield limit? " & BSpecifyColorLimit
         Debug.Print "  Color for values above the yield limit and user-defined colors (RGB): "
         Dim rgb As String
         rgb = "{"
         Dim rgbInd As Long
         rgbInd = 1
         Dim size As Long
         size = UBound(VarColor)
         Dim ind As Long
         ind = 1
         ' Create RGB triplet for each color
         For Each Color In VarColor
             If rgbInd < 3 Then
                 rgb = rgb & Color & ","
                 rgbInd = rgbInd + 1
             Else
                 rgb = rgb & Color & "}"
                 rgbInd = 1
                 If Not ind = size + 1 Then
                     rgb = rgb & "{"
                 End If
             End If
             ind = ind + 1
         Next
         Debug.Print "  " & rgb

         errorCode = CWResult.GetLegendContourColors(Name, VarColor)

        Debug.Print ""
         Debug.Print "Legend colors {R,G,B}: "

         rgb = "{"
         rgbInd = 1
         size = UBound(VarColor)
         ind = 1

         ' Create RGB triplet for each color
         For Each Color In VarColor
             If rgbInd < 3 Then
                 rgb = rgb & Color & ","
                 rgbInd = rgbInd + 1
             Else
                 rgb = rgb & Color & "}"
                 rgbInd = 1
                 If Not ind = size + 1 Then
                   rgb = rgb & "{"
                 End If
             End If
             ind = ind + 1
         Next
         Debug.Print rgb
        vDispOptions = CWResult.GetPlotDisplayOptions(Name, errorCode)
         Debug.Print ""
         Debug.Print "Plot display options:"
         Debug.Print "  Display the minimum value? " & vDispOptions(0)
         Debug.Print "  Display the maximum value? " & vDispOptions(1)
         Debug.Print "  Display the plot details? " & vDispOptions(2)
         Debug.Print "  Display the legend? " & vDispOptions(3)
         Debug.Print "  Display the minimum/maximum range only for parts? " & vDispOptions(4)
         Debug.Print "  Allow a user-defined minimum/maximum? " & vDispOptions(5)
         Debug.Print "    User-defined minimum: " & vDispOptions(6)
         Debug.Print "    User-defined maximum: " & vDispOptions(7)
        vPlotPosFormatOptions = CWResult.GetPlotPositionFormatOptions(Name, errorCode)
         Debug.Print ""
         Debug.Print "Plot position/format options:"
         Debug.Print "  Percentage of the window width: " & vPlotPosFormatOptions(0)
         Debug.Print "  Percentage of the window height: " & vPlotPosFormatOptions(1)
         Debug.Print "  Chart thickness option as defined in swsColorChartWidthOptionValue_e: " & vPlotPosFormatOptions(2)
         Debug.Print "  Chart number format as defined in swsColorChartNumberFormatOptionValue_e: " & vPlotPosFormatOptions(3)
         Debug.Print "  Number of decimal places to display: " & vPlotPosFormatOptions(4)
         Debug.Print "  Display chart numbers with a 1000 comma separator? " & vPlotPosFormatOptions(5)
         Debug.Print "  Use different number format for small numbers? " & vPlotPosFormatOptions(6)
         Debug.Print "    Number format for small numbers as defined in swsColorNumberFormatUseDiffNumberFormatOptionValue_e: " & vPlotPosFormatOptions(7)
        vPlotSettings = CWResult.GetPlotSettings(Name, errorCode)
         Debug.Print ""
         Debug.Print "Plot settings:"
         Debug.Print "  Display option for active fringe plot as defined in swsPlotFringeSettingsOptionValue_e: " & vPlotSettings(0)
         Debug.Print "  Display option for model boundary as defined in swsPlotBoundarySettingsOptionValue_e: " & vPlotSettings(1)
         Debug.Print "  R value for model/mesh color: " & vPlotSettings(2)
         Debug.Print "  G value for model/mesh color: " & vPlotSettings(3)
         Debug.Print "  B value for model/mesh color: " & vPlotSettings(4)
         Debug.Print "  Superimpose the un-deformed model on the deformed model? " & vPlotSettings(5)
         Debug.Print "    Deformed plot translucent option as defined in swsPlotDeformedShapeOptionSuperImposeValue_e: " & vPlotSettings(6)
         Debug.Print "  R value for single translucent color: " & vPlotSettings(7)
         Debug.Print "  G value for single translucent color: " & vPlotSettings(8)
         Debug.Print "  B value for single translucent color: " & vPlotSettings(9)
         Debug.Print "  Color intensity [0,1]: " & vPlotSettings(10)

         InputVar1 = Array(True, 0, 255, 0, 0, 0.75, True, 0, 0, 0, 255, 0.2)
         errorCode = CWResult.SetPlotSettingsOptionForHiddenAndExcludedBody(Name, InputVar1)

         Var = CWResult.GetPlotSettingsOptionForHiddenAndExcludedBody(Name, errorCode)
         Debug.Print ""
         Debug.Print "  Show hidden bodies? (1 = true, 0 = false) " & Var(0)
         Debug.Print "    Translucent color option as defined in swsPlotShowHiddenBodiesOptionValue_e: " & Var(1)
         Debug.Print "    R value for single translucent color: " & Var(2)
         Debug.Print "    G value for single translucent color: " & Var(3)
         Debug.Print "    B value for single translucent color: " & Var(4)
         Debug.Print "    Color intensity [0, 1]: " & Var(5)
         Debug.Print "  Show excluded bodies? (1 = true, 0 = false) " & Var(6)
         Debug.Print "    Translucent color option as defined in swsPlotShowExcludedBodiesOptionValue_e: " & Var(7)
         Debug.Print "    R value for single translucent color: " & Var(8)
         Debug.Print "    G value for single translucent color: " & Var(9)
         Debug.Print "    B value for single translucent color: " & Var(10)
         Debug.Print "    Color intensity [0, 1]: " & Var(11)

     Next
     'Hide fixture and force symbols
     Study.ShowOrHideFixtures = False
     Study.ShowOrHideForce = False
     Stop
     'Show fixture and force symbols
     Study.ShowOrHideFixtures = True
     Study.ShowOrHideForce = True

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)

     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""

 End Sub

 Sub StringtoArray(inputSTR As String, varEntity As Variant)

     Dim PID() As Byte
     Dim i As Integer
     varEntity = Split(inputSTR, ",")
     ReDim PID(UBound(varEntity))
     For i = 0 To (UBound(varEntity) - 1)
     PID(i) = varEntity(i)
     Next i
     varEntity = PID

 End Sub
```
