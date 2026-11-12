---
title: "Get Thermal Values at Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Thermal_Values_at_Points_Example_VBNET.htm"
---

# Get Thermal Values at Points Example (VB.NET)

## Get Thermal Values Example (VB.NET)

This example shows how to get thermal values in a thermal study.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified model exists.
 ' 4. Modify the path to solidworks materials.sldmat if needed.
  ' 5. Uncomment the thermal method whose return values you want to see.
 ' 6. Open the Immediate window.
 '
 ' Postconditions:
 ' 1.  Opens document.
 ' 2.  Creates Thermal_One study.
 ' 3.  Applies user-defined and SOLIDWORKS materials to components.
  ' 4.  Gets objects by persistent reference and populates input arrays.
 ' 5.  Sets thermal study options.
  ' 6.  Assigns initial temperatures to assembly components.
  ' 7.  Adds heat power and convection to assembly components.
  ' 8.  Assigns thermostat location and the temperature range.
 ' 9.  Meshes the assembly.
 ' 10. Analyzes the study.
  ' 11. Prints thermal values at solution step 60 to the Immediate window.
 '
 ' NOTES:
 '  * To get persistent reference identifiers (PIDs) for model selections,
 '    use pidcollector.exe or IModelDocExtension::GetPersistReference3.
  '  * Solving this study can take some time. Examine the Immediate window
  '    to monitor the macro's progress. Done! indicates that the macro
 '    has finished.
 '  * Because this assembly document is used by a SOLIDWORKS Simulation
 '    online tutorial, do not save any changes.
  '--------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As CosmosWorks
         Dim CWObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim SolidMgr As CWSolidManager
         Dim SolidComp As CWSolidComponent
         Dim SolidBody As CWSolidBody
         Dim ThermalOptions As CWThermalStudyOptions
         Dim CWConv As CWConvection
         Dim CWHeatPower As CWHeatPower
         Dim CwMesh As CWMesh
         Dim CWResult As CWResults
         Dim CWMat As CWMaterial
         Dim CWTemp As CWTemperature
         Dim Part As ModelDoc2
         Dim LBCMgr As CWLoadsAndRestraintsManager
         Dim oselect1 As Object, oselect2 As Object, oselect3 As Object
         Dim oselect4 As Object, oselect5 As Object, oselect6 As Object
         Dim oselect7 As Object, oselect8 As Object, oselect9 As Object, oselect10 As Object
         Dim therm1 As Object
         Dim var1 As Object = Nothing, var2 As Object = Nothing, var3 As Object = Nothing, var4 As Object = Nothing
         Dim var5 As Object = Nothing, var6 As Object = Nothing, var7 As Object = Nothing, var8 As Object = Nothing
         Dim var9 As Object = Nothing, var10 As Object = Nothing, var11 As Object = Nothing
         Dim Temp As Object
         Dim bApp As Boolean
         Dim selection1 As String, selection2 As String, selection3 As String
         Dim selection4 As String, selection5 As String, selection6 As String
         Dim selection7 As String, selection8 As String, selection9 As String
         Dim selection10 As String, selection11 As String
         Dim longstatus As Integer, longwarnings As Integer
         Dim errCode As Integer
         Dim el As Double, tl As Double
         Dim nStep As Integer

         ' Open document
         Debug.Print("Opening document...")
         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Thermal\CoffeeJar.SLDASM", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)

         If Part Is Nothing Then ErrorMsg(swApp, "Failed to open document", True)

         ' Get the SOLIDWORKS Simulation add-in object
         CWObject = swApp.GetAddInObject("SldWorks.Simulation")
         If CWObject Is Nothing Then ErrorMsg(swApp, "No CwAddincallback object", True)

         COSMOSWORKS = CWObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No CosmosWorks object", True)

         ' Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document", True)

         ' Create new thermal study
         Debug.Print("Creating thermal study...")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager object", True)

         Study = StudyMngr.CreateNewStudy3("Thermal_One", swsAnalysisStudyType_e.swsAnalysisStudyTypeThermal, swsMeshType_e.swsMeshTypeSolid, errCode)
         If Study Is Nothing Then ErrorMsg(swApp, "No study", True)

         ' Get first solid component
         SolidMgr = Study.SolidManager
         If SolidMgr Is Nothing Then ErrorMsg(swApp, "No solid manager object", True)

         SolidComp = SolidMgr.GetComponentAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid component", True)

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid body", True)

         ' Add material
         CWMat = SolidBody.GetDefaultMaterial
         If CWMat Is Nothing Then ErrorMsg(swApp, "No default material", True)

         CWMat.MaterialName = "Coffee"

         Call CWMat.SetPropertyByName("DENS", 1000, 0)
         Call CWMat.SetPropertyByName("KX", 40, 0)
         Call CWMat.SetPropertyByName("C", 4200.0#, 0)

         errCode = SolidBody.SetSolidBodyMaterial(CWMat)
         If errCode <> 0 Then ErrorMsg(swApp, "Solid body material not set", True)

         ' Get second solid component
         SolidComp = SolidMgr.GetComponentAt(1, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid component", True)

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid body", True)

         ' Add material
         bApp = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Glass")
         If bApp = False Then ErrorMsg(swApp, "No glass material applied", True)

         ' Get third solid component
         SolidComp = SolidMgr.GetComponentAt(2, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid component", True)

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid body", True)

         ' Add material
         bApp = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Nylon 6/10")
         If bApp = False Then ErrorMsg(swApp, " No Nylon 6/10 material applied", True)

         ' CoffeePot
         selection1 = "216,14,0,0,5,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0"
         selection1 = selection1 & ",Type=1"
         StringtoArray(selection1, var1)
         oselect1 = Part.Extension.GetObjectByPersistReference3((var1), longstatus)

         ' Coffee
         selection2 = "216,14,0,0,5,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0"
         selection2 = selection2 & ",Type=1"
         StringtoArray(selection2, var2)
         oselect2 = Part.Extension.GetObjectByPersistReference3((var2), longstatus)

         ' Top
         selection3 = "216,14,0,0,5,0,0,0,255,254,255,15,84,0,111,0,112,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,13,0,0,0"
         selection3 = selection3 & ",Type=1"
         StringtoArray(selection3, var3)
         oselect3 = Part.Extension.GetObjectByPersistReference3((var3), longstatus)

         ' Get the four coffee faces that make up the surface of coffee in the coffee pot
         ' Face 1
         selection4 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,10"
         selection4 = selection4 & "8,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,5,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,19,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,0,0,0,0,0,0"
         selection4 = selection4 & ",Type=1"
         StringtoArray(selection4, var4)
         oselect4 = Part.Extension.GetObjectByPersistReference3((var4), longstatus)

         ' Face 2
         selection5 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,"
         selection5 = selection5 & "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,6,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,19,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,0,0,0,0,0,0"
         selection5 = selection5 & ",Type=1"
         StringtoArray(selection5, var5)
         oselect5 = Part.Extension.GetObjectByPersistReference3((var5), longstatus)

         ' Face 3
         selection6 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,"
         selection6 = selection6 & "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,2,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,19,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,0,0,0,0,0,0"
         selection6 = selection6 & ",Type=1"
         StringtoArray(selection6, var6)
         oselect6 = Part.Extension.GetObjectByPersistReference3((var6), longstatus)

         ' Face 4
         selection7 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,"
         selection7 = selection7 & "108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,11,0,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,5,128,8,0,92,0,0,0,241,69,48,63,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,21,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,16,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,0,0,0,0,0,0"
         selection7 = selection7 & ",Type=1"
         StringtoArray(selection7, var7)
         oselect7 = Part.Extension.GetObjectByPersistReference3((var7), longstatus)

         ' Get the selections for convection
         ' Top-outer face of coffee pot
         selection8 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,"
         selection8 = selection8 & "114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,3,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,2,0,0,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,4,0,0,0,0,0,0,0,0,0"
         selection8 = selection8 & ",Type=1"
         StringtoArray(selection8, var8)
         oselect8 = Part.Extension.GetObjectByPersistReference3((var8), longstatus)

         ' Lower-outer face of coffee pot
         selection9 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,"
         selection9 = selection9 & "0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,2,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,3,0,0,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,1,0,0,0,0,0,0,0,0,0"
         selection9 = selection9 & ",Type=1"
         StringtoArray(selection9, var9)
         oselect9 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

         ' Get the selections for heat power
         ' Vertex located on the top of the bottom face of the coffee pot
         selection10 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,99,0,111,0,102,0,102,0,101,0,101,0,106,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,8,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,"
         selection10 = selection10 & "1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,"
         selection10 = selection10 & "0,101,0,114,0,109,0,97,0,108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,"
         selection10 = selection10 & "110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,"
         selection10 = selection10 & "135,69,48,63,5,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,5,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,"
         selection10 = selection10 & "5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,2,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,6,0,0,0,4,0,0,0,0,0,0,0"
         selection10 = selection10 & ",Type=1"
         StringtoArray(selection10, var10)
         therm1 = Part.Extension.GetObjectByPersistReference3((var10), longstatus)

         ' Vertex where sensor (thermostat) is located
         selection11 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,3,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,"
         selection11 = selection11 & "114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,1,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,2,0,0,0,0,0,0,0,0,0"
         selection11 = selection11 & ",Type=1"
         StringtoArray(selection11, var11)
         oselect10 = Part.Extension.GetObjectByPersistReference3((var11), longstatus)

         ' Create arrays
         Dim varArray1 As Object() = {oselect1, oselect3}
         Dim varArray2 As Object() = {oselect2}
         Dim varArray3 As Object() = {oselect4, oselect5, oselect6, oselect7}
         Dim varArray4 As Object() = {oselect8, oselect9}
         Dim varArray5 As Object() = {therm1}
         Dim varArray6 As Object() = {oselect10}
         Dim varArray7 As Object() = {-19.63, 31.23, 173.15}

         ' Set transient thermal study with solver type FFEPlus
         Debug.Print("Setting transient thermal study with solver type FFEPlus...")
         ThermalOptions = Study.ThermalStudyOptions
         Study.ThermalStudyOptions.SolutionType = 0
         If ThermalOptions Is Nothing Then ErrorMsg(swApp, "No thermal options", False)

         ThermalOptions.SolverType = 2
         ThermalOptions.TotalTime = 3600
         ThermalOptions.TimeIncrement = 60

         ' Apply initial temperature to coffee pot and top
         Debug.Print("Applying initial temperature to coffee pot and top...")

         LBCMgr = Study.LoadsAndRestraintsManager
         If LBCMgr Is Nothing Then ErrorMsg(swApp, "No loads and restraints manager", False)

         CWTemp = LBCMgr.AddTemperature((varArray1), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No temperature applied", True)

         CWTemp.TemperatureBeginEdit()
         CWTemp.TemperatureType = 0
         CWTemp.Unit = 1
         CWTemp.TemperatureValue = 72

         errCode = CWTemp.TemperatureEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "No temperature applied", True)

         ' Apply initial temperature to coffee
         Debug.Print("Applying initial temperature to coffee...")

         CWTemp = LBCMgr.AddTemperature((varArray2), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No temperature applied", True)

         CWTemp.TemperatureBeginEdit()
         CWTemp.TemperatureType = 0
         CWTemp.Unit = 1
         CWTemp.TemperatureValue = 195

         errCode = CWTemp.TemperatureEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "No temperature applied", True)

         ' Create convection for coffee component
         Debug.Print("Creating convection for coffee component...")

         CWConv = LBCMgr.AddConvection((varArray3), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No convection added", True)

         CWConv.ConvectionBeginEdit()
         CWConv.Unit = 1
         CWConv.ConvectionCoefficient = 0.0000085
         CWConv.BulkAmbientTemperature = 72

         errCode = CWConv.ConvectionEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Convection end-edit failed for coffee", True)

         ' Create convection for coffee pot component
         Debug.Print("Creating convection for coffee pot component...")
         CWConv = LBCMgr.AddConvection((varArray4), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No convection added", True)

         CWConv.ConvectionBeginEdit()
         CWConv.Unit = 1
         CWConv.ConvectionCoefficient = 0.000061
         CWConv.BulkAmbientTemperature = 72

         errCode = CWConv.ConvectionEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Convection end-edit failed for coffee pot", True)

         ' Create heat power for face
         Debug.Print("Creating heat power for face...")

         CWHeatPower = LBCMgr.AddHeatPower((varArray6), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No heat power created", True)

         CWHeatPower.HeatPowerBeginEdit()
         CWHeatPower.Unit = 0
         CWHeatPower.HPValue = 2000

         ' Set thermostat to a vertex
         Debug.Print("Setting thermostat to a vertex...")
         CWHeatPower.IncludeThermostat = True
         CWHeatPower.SetThermostat(therm1)
         CWHeatPower.ThermostatUnits = 1
         CWHeatPower.SetCutOffTemperatures(190, 200)
         errCode = CWHeatPower.HeatPowerEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Heat power not updated", True)

         ' Create mesh
         Debug.Print("Creating mesh...")
         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(swApp, "No mesh object", False)
         CwMesh.Quality = 1
         CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed", True)

         ' Run analysis
         Debug.Print("Running analysis...")
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed", True)

         ' Get thermal results
         Debug.Print("Getting thermal results...")
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No results object", False)

         nStep = CWResult.GetMaximumAvailableSteps ' solution step 60

         ' Get temperature value at point {-19.63, 31.23, 173.15} at solution step 60
         Temp = CWResult.GetThermalValuesAtPoints(swsThermalComponent_e.swsThermalComponentTEMP, nStep, Nothing, (varArray7), swsTemperatureUnit_e.swsTemperatureUnitKelvin, errCode)

         ' Get temperature values at all nodes at solution step 60
         'Temp = CWResult.GetThermalValues(nStep, Nothing, swsTemperatureUnitKelvin, errCode)

         ' Get heat energy values for the specified vertex at solution step 60
         'Temp = CWResult.GetHeatPowerOrEnergy2(-1, (varArray6), swsUnitSI, 1, nStep, errCode) ' Heat energy

         ' Get temperature values for all steps at node 9236
         'Temp = CWResult.GetThermalComponentForAllStepsAtNode(swsThermalComponentTEMP, 9236, Nothing, swsTemperatureUnitKelvin, errCode)

         ' Get temperature values for the specified entities at solution step 60
         'Temp = CWResult.GetThermalForEntities(swsThermalComponentTEMP, nStep, Nothing, (varArray4), swsTemperatureUnitKelvin, errCode)

         If errCode <> 0 Then ErrorMsg(swApp, "No temperature result", True)

         ' Print out the contents of Temp
         ' See the Simulation API Help for information about the contents of the returned array
         Dim i As Integer
         For i = 0 To UBound(Temp)
             Debug.Print(Temp(i))
         Next

         Debug.Print("Done!")

     End Sub

     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)
         swApp.SendMsgToUser2(Message, 0, 0)
         swApp.RecordLine("'*** WARNING - General")
         swApp.RecordLine("'*** " & Message)
         swApp.RecordLine("")
     End Sub

     Sub StringtoArray(ByVal inputSTR As String, ByRef varEntity As Object)
         Dim PID() As Byte
         Dim i As Integer

         varEntity = Split(inputSTR, ",")
         ReDim PID(UBound(varEntity))
         For i = 0 To (UBound(varEntity) - 1)
             PID(i) = varEntity(i)
         Next i
         varEntity = PID
     End Sub

     Public swApp As SldWorks

 End Class
```
