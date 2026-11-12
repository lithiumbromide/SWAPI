---
title: "Apply Thermostat-controlled Heat Power for Transient Thermal Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm"
---

# Apply Thermostat-controlled Heat Power for Transient Thermal Study Example (VB.NET)

This example shows how to apply thermostat-controlled heat power and flux in a transient thermal study.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that c:\temp exists.
  ' 4. Ensure that the specified material library exists.
  ' 5. Ensure that the specified model document exists.
 ' 6. Open the Immediate window.
 '
 ' Postconditions:
 '  1. Opens the specified model document.
 '  2. Creates Thermal_One study.
  '  3. Defines default thermal study results plot and plot options.
 '  4. Applies user-defined and SOLIDWORKS materials to components.
  '  5. Specifies initial temperatures for assembly components.
  '  6. Specifies thermostat location and the temperature range.
  '  7. Prints heat flux properties to the Immediate window.
 '  8. Prints radiation properties to the Immediate window.
 '  9. Meshes the model.
 ' 10. Analyzes Thermal_One.
 ' 11. Creates 60 thermal plots.
 ' 12. Saves the Thermal1 results plot as an eDrawings document in c:\temp.
 ' 13. Exports Thermal_One study to the NASTRAN finite-element analysis program
 '     in c:\temp.
 ' 14. Renames Thermal_One study to TransientThermal.
  ' 15. Inspect the Immediate window, the Simulation study tree,
 '     and the graphics area.
 '
 ' NOTES:
 '  * To get persistent reference identifiers (PIDs) for model selections,
 '    you can use pidcollector.exe or IModelDocExtension::GetPersistReference3.
  '  * Solving this study can take some time. Examine the Immediate window
 '    to monitor the macro's progress. Done! indicates that the macro
 '    has finished.
 '  * Because the assembly is used elsewhere, do not save any changes.
  '--------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As COSMOSWORKS
         Dim CWObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim SolidMgr As CWSolidManager
         Dim SolidComp As CWSolidComponent
         Dim SolidBody As CWSolidBody
         Dim ThermalOptions As CWThermalStudyOptions
         Dim CWConv As CWConvection
         Dim CwMesh As CWMesh
         Dim CWResult As CWResults
         Dim CWMat As CWMaterial
         Dim CWTemp As CWTemperature
         Dim Part As ModelDoc2
         Dim LBCMgr As CWLoadsAndRestraintsManager
         Dim heatFlux As CWHeatFlux
         Dim CWHeatPower As CWHeatPower
         Dim rad As CWRadiation
         Dim oselect1 As Object, oselect2 As Object, oselect3 As Object
         Dim oselect4 As Object, oselect5 As Object, oselect6 As Object
         Dim oselect7 As Object, oselect8 As Object, oselect9 As Object, oselect10 As Object
         Dim therm1 As Object
         Dim var1 As Object = Nothing
         Dim var2 As Object = Nothing
         Dim var3 As Object = Nothing
         Dim var4 As Object = Nothing
         Dim var5 As Object = Nothing
         Dim var6 As Object = Nothing
         Dim var7 As Object = Nothing
         Dim var8 As Object = Nothing
         Dim var9 As Object = Nothing
         Dim var10 As Object = Nothing
         Dim var11 As Object = Nothing
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
         Dim res As Integer

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Thermal\CoffeeJar.SLDASM", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(swApp, "Failed to open document")

         ' Get the SOLIDWORKS Simulation add-in object
         CWObject = swApp.GetAddInObject("SldWorks.Simulation")
         If CWObject Is Nothing Then ErrorMsg(swApp, "Failed to get Simulation add-in")

         COSMOSWORKS = CWObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "Failed to get CosmosWorks object")

         ' Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "Failed to get active document")

         ' Add a default thermal study results plot
         res = ActDoc.AddDefaultThermalStudyPlot(swsThermalResultComponentTypes_e.swsThermalResultComponentTypes_TEMP, True)

         ' Set default thermal plot options
         ' Show maximum value annotation on the plot
         bApp = ActDoc.SetSimulationOptionToggle(swsUserPreferenceToggle_e.swsPlotAnnotationShowMaxValue, True)
         Debug.Print("Show maximum value annotation on the plot? " & ActDoc.GetSimulationOptionToggle(swsUserPreferenceToggle_e.swsPlotAnnotationShowMaxValue))

         ' Set sub-folder option
         bApp = ActDoc.SetSimulationOptionToggle(swsUserPreferenceToggle_e.swsResultFolderUnderSubFolder, True)
         Debug.Print("Set sub-folder option? " & ActDoc.GetSimulationOptionToggle(swsUserPreferenceToggle_e.swsResultFolderUnderSubFolder))

         ' Put results in C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Thermal\temp
         bApp = ActDoc.SetSimulationOptionStringValue(swsUserPreferenceStringValue_e.swsSolidWorksDocumentFolderSubFolderLocation, "temp")
         Debug.Print("Place results in model document sub-folder, " & ActDoc.GetSimulationOptionStringValue(swsUserPreferenceStringValue_e.swsSolidWorksDocumentFolderSubFolderLocation))

         ' Set boundary settings option to translucent single color
         bApp = ActDoc.SetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotSettingsBoundaryOption, swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryTranslucentSingleColor)
         Debug.Print("Boundary settings option as defined in swsPlotSettingsBoundaryOption is " & ActDoc.GetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotSettingsBoundaryOption))

         ' Set boundary color; Red 1 is 0xFF0000 in http://cloford.com/resources/colours/500col.htm
         ' Reverse the hexadecimal (&H0000FF) in the call below
         bApp = ActDoc.SetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotBoundaryOptionTranslucentSingleColorSetting, &HFF)
         Debug.Print("Boundary color is " & ActDoc.GetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotBoundaryOptionTranslucentSingleColorSetting))

         ' Set boundary transparency of translucent part color to 50%
         bApp = ActDoc.SetSimulationOptionDoubleValue(swsUserPreferenceDoubleValue_e.swsPlotBoundaryTransparency, 50.0#)
         Debug.Print("Transparency of boundary translucent part color is " & ActDoc.GetSimulationOptionDoubleValue(swsUserPreferenceDoubleValue_e.swsPlotBoundaryTransparency))

         ' Create new thermal study
         Debug.Print("Creating thermal study...")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")

         Study = StudyMngr.CreateNewStudy3("Thermal_One", swsAnalysisStudyType_e.swsAnalysisStudyTypeThermal, swsMeshType_e.swsMeshTypeSolid, errCode)
         If Study Is Nothing Then ErrorMsg(swApp, "Failed to create study")

         ' Get first solid component
         SolidMgr = Study.SolidManager
         If SolidMgr Is Nothing Then ErrorMsg(swApp, "No CWSolidManager object")

         SolidComp = SolidMgr.GetComponentAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component")

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component body")

         ' Add material
         CWMat = SolidBody.GetDefaultMaterial
         If CWMat Is Nothing Then ErrorMsg(swApp, "No CWMaterial object")

         CWMat.MaterialName = "Coffee"
         Call CWMat.SetPropertyByName("DENS", 1000, 0)
         Call CWMat.SetPropertyByName("KX", 40, 0)
         Call CWMat.SetPropertyByName("C", 4200.0#, 0)

         errCode = SolidBody.SetSolidBodyMaterial(CWMat)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to set material")

         ' Get second solid component
         SolidComp = SolidMgr.GetComponentAt(1, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component")

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component body")

         ' Add material
         bApp = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Glass")
         If bApp = False Then ErrorMsg(swApp, "Failed to apply glass material")

         ' Get third solid component
         SolidComp = SolidMgr.GetComponentAt(2, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component")

         SolidBody = SolidComp.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to get component body")

         ' Add material
         bApp = SolidBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Nylon 6/10")
         If bApp = False Then ErrorMsg(swApp, "Failed to apply Nylon 6/10 material")

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

         ' Bottom-outer face of coffee pot
         selection9 = "216,14,0,0,3,0,0,0,255,254,255,21,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,45,0,49,0,64,0,67,0,111,0,102,0,102,0,101,0,101,0,74,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,9,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,174,232,47,63,11,128,255,254,255,60,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,"
         selection9 = selection9 & "0,114,0,115,0,92,0,84,0,104,0,101,0,114,0,109,0,97,0,108,0,92,0,67,0,111,0,102,0,102,0,101,0,101,0,80,0,111,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,153,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,5,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,39,0,0,0,234,237,47,63,2,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,3,0,0,0,0,0,3,128,0,0,5,128,8,0,39,0,0,0,234,237,47,63,1,0,0,0,0,0,0,0,0,0"
         selection9 = selection9 & ",Type=1"
         StringtoArray(selection9, var9)
         oselect9 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

         ' Thermostat sensor located on the top of the bottom face of the coffee pot
         selection10 = "216,14,0,0,3,0,0,0,255,254,255,18,67,0,111,0,102,0,102,0,101,0,101,0,45,0,49,0,64,0,99,0,111,0,102,0,102,0,101,0,101,0,106,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,13,0,109,111,86,101,114,116,101,120,82,101,102,95,99,255,255,255,255,255,255,255,255,8,0,0,0,0,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,18,0,109,111,80,76,105,110,101,80,114,111,106,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,"
         selection10 = selection10 & "1,0,14,0,109,111,79,98,106,70,105,108,101,68,101,102,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,6,99,0,111,0,102,0,102,0,101,0,101,0,126,253,47,63,11,128,255,254,255,57,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,84,0,104,"
         selection10 = selection10 & "0,101,0,114,0,109,0,97,0,108,0,92,0,99,0,111,0,102,0,102,0,101,0,101,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,90,14,28,65,0,0,0,0,2,0,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,241,69,48,63,255,255,1,0,18,0,109,111,80,76,105,110,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,90,0,0,0,219,69,48,63,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,"
         selection10 = selection10 & "110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,3,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,"
         selection10 = selection10 & "135,69,48,63,5,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,5,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,1,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,"
         selection10 = selection10 & "5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,2,0,0,0,2,0,0,0,14,128,0,0,5,128,8,0,92,0,0,0,241,69,48,63,14,128,0,0,5,128,8,0,90,0,0,0,219,69,48,63,17,128,0,0,5,128,8,0,88,0,0,0,135,69,48,63,5,0,0,0,1,0,0,0,6,0,0,0,4,0,0,0,0,0,0,0"
         selection10 = selection10 & ",Type=1"
         StringtoArray(selection10, var10)
         therm1 = Part.Extension.GetObjectByPersistReference3((var10), longstatus)

         ' Face to which to apply heat power and flux
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

         ' Set transient thermal study options
         Debug.Print("Setting transient thermal study options...")
         ThermalOptions = Study.ThermalStudyOptions
         If ThermalOptions Is Nothing Then ErrorMsg(swApp, "No CWThermalStudyOptions object")
         ThermalOptions.CheckFlowConvectionCoef2 = 0
         ThermalOptions.SolutionType = 0
         ThermalOptions.SolverType = 2
         ThermalOptions.TotalTime = 3600
         ThermalOptions.TimeIncrement = 60

         ' Apply initial temperature to coffee pot and top
         Debug.Print("Applying initial temperature to coffee pot and top...")
         LBCMgr = Study.LoadsAndRestraintsManager
         If LBCMgr Is Nothing Then ErrorMsg(swApp, "No CWLoadsAndRestraintsManager object")

         CWTemp = LBCMgr.AddTemperature((varArray1), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add temperature load")

         CWTemp.TemperatureBeginEdit()
         CWTemp.TemperatureType = 0
         CWTemp.Unit = 1
         CWTemp.TemperatureValue = 72

         errCode = CWTemp.TemperatureEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit temperature load")

         ' Apply initial temperature to coffee
         Debug.Print("Applying initial temperature to coffee...")
         CWTemp = LBCMgr.AddTemperature((varArray2), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add temperature load")

         CWTemp.TemperatureBeginEdit()
         CWTemp.TemperatureType = 0
         CWTemp.Unit = 1
         CWTemp.TemperatureValue = 195

         errCode = CWTemp.TemperatureEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit temperature load")

         ' Create convection for coffee component
         Debug.Print("Creating convection for coffee component...")
         CWConv = LBCMgr.AddConvection((varArray3), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add convection load")

         CWConv.ConvectionBeginEdit()
         CWConv.Unit = 1
         CWConv.ConvectionCoefficient = 0.0000085
         CWConv.BulkAmbientTemperature = 72

         errCode = CWConv.ConvectionEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit convection load")

         ' Create convection for coffee pot component
         Debug.Print("Creating convection for coffee pot component...")
         CWConv = LBCMgr.AddConvection((varArray4), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add convection")

         CWConv.ConvectionBeginEdit()
         CWConv.Unit = 1
         CWConv.ConvectionCoefficient = 0.000061
         CWConv.BulkAmbientTemperature = 72

         errCode = CWConv.ConvectionEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit convection load")

         ' Add heat power
         Debug.Print("Creating heat power for face...")
         CWHeatPower = LBCMgr.AddHeatPower((varArray6), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add heat power")
         CWHeatPower.HeatPowerBeginEdit()
         CWHeatPower.Unit = 0
         CWHeatPower.HPValue = 2000
         CWHeatPower.ReverseDirection2 = 0
         Debug.Print("  Setting thermostat to a vertex...")
         CWHeatPower.IncludeThermostat2 = True
         CWHeatPower.SetThermostat(therm1)
         CWHeatPower.ThermostatUnits = 1
         CWHeatPower.SetCutOffTemperatures(190, 200)
         errCode = CWHeatPower.HeatPowerEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit heat power")

         ' Add heat flux
         Debug.Print("Creating heat flux for face...")
         heatFlux = LBCMgr.AddHeatFlux((varArray6), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add heat flux")
         heatFlux.HeatFluxBeginEdit()
         heatFlux.HFValue = 100
         heatFlux.SetThermostat(therm1)
         errCode = heatFlux.HeatFluxEndEdit
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit heat flux")
         Dim dval1 As Double, dval2 As Double
         heatFlux.GetCutOffTemperatures(dval1, dval2)
         Debug.Print("  Thermostat lower-bound temperature: " & dval1)
         Debug.Print("  Thermostat upper-bound temperature: " & dval2)
         Debug.Print("  Heat flux: " & heatFlux.HFValue)
         Debug.Print("    Reverse direction? (False = no, True = yes) " & heatFlux.ReverseDirection2)
         Debug.Print("  Include thermostat effects? (False = no, True = yes) " & heatFlux.IncludeThermostat2)
         Debug.Print("  Thermostat units as defined in swsTemperatureUnit_e: " & heatFlux.ThermostatUnits)
         Debug.Print("  Use temperature curve? (False = no, True = yes) " & heatFlux.UseTemperatureCurve2)
         Debug.Print("  Use time curve? (False = no, True = yes) " & heatFlux.UseTimeCurve2)
         Debug.Print("  Units as defined in swsTemperatureUnit_e: " & heatFlux.Unit)

         ' Add radiation
         Debug.Print("Creating radiation for face...")
         rad = LBCMgr.AddRadiation(swsRadiationType_e.swsRadiationTypeSurfaceToAmbient, (varArray6), errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to add radiation")
         rad.RadiationBeginEdit()
         rad.Emmisivity = 0.5
         rad.ViewFactor = 0.5
         errCode = rad.RadiationEndEdit
         Debug.Print("  Ambient temperature: " & rad.AmbientTemperature)
         Debug.Print("  Emissivity: " & rad.Emmisivity)
         Debug.Print("  View factor: " & rad.ViewFactor)
         Debug.Print("  Open system? (False = no, True = yes) " & rad.OpenSystem2)
         Debug.Print("  Use temperature curve? (False = no, True = yes) " & rad.UseTemperatureCurve2)
         Debug.Print("  Use time curve? (False = no, True = yes) " & rad.UseTimeCurve2)
         Debug.Print("  Units as defined in swsTemperatureUnit_e: " & rad.Unit)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to edit radiation")

         ' Mesh model
         Debug.Print("Creating mesh...")
         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")

         CwMesh.Quality = 1
         Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to create mesh")

         ' Analyze study
         Debug.Print("Running analysis...")
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

         Debug.Print("Getting results...")
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(swApp, "No CWResults object")

         ' Get temperature at vertex
         Debug.Print("Getting temperature at vertex...")
         nStep = CWResult.GetMaximumAvailableSteps
         Temp = CWResult.GetThermalForEntities(0, nStep, Nothing, (varArray5), 2, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No temperature result")

         ' Save Thermal1 plot as eDrawing
         CWResult.SavePlotsAseDrawings("c:\temp", "ThermalPlot", "Thermal1")

         ' Export this study to the NASTRAN finite-element analysis program
         res = Study.ExportSimulationStudy("c:\temp", "ThermalStudyExport", swsNastranExportOption_e.swsNastranExportOption_LongFixed, 0, 0, swsStudyExportOption_e.swsStudyExportOption_Nastran, swsNastranExportUnit_e.swsNastranExportUnit_IPS)

         ' Rename the study
         res = StudyMngr.RenameStudyFromName("Thermal_One", "TransientThermal")

         Debug.Print("Done!")

     End Sub

     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String)
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

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
