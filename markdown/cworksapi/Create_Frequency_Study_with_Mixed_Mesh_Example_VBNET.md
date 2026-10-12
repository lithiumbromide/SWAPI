---
title: "Create Frequency Study with Mixed Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm"
---

# Create Frequency Study with Mixed Mesh Example (VB.NET)

This example shows how to create a frequency study using a mixed mesh.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified material library exists.
 ' 4. Ensure that the specified model document exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Creates a frequency mixed-mesh study.
 ' 3. Applies material.
 ' 4. Adds a fixed restraint.
 ' 5. Adds a bonded contact set.
 ' 6. Creates a mesh.
 ' 7. Runs an analysis.
 ' 8. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

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
        Dim Shell As CWShell
        Dim CwMesh As CWMesh
        Dim CWResult As CWResults
        Dim Part As ModelDoc2
        Dim ShellMgr As CWShellManager
        Dim LBCMgr As CWLoadsAndRestraintsManager
        Dim ContactMgr As CWContactManager
        Dim CWContactSet As CWContactSet
        Dim CWRes1 As CWRestraint
        Dim pDisp1 As Object, pDisp2 As Object
        Dim oselect1 As Object, oselect2 As Object, oselect3 As Object, oselect4 As Object, oselect5 As Object
        Dim oselect6 As Object
        Dim var1 As Object = Nothing
        Dim var2 As Object = Nothing
        Dim var3 As Object = Nothing
        Dim var4 As Object = Nothing
        Dim var5 As Object = Nothing
        Dim var6 As Object = Nothing
        Dim var8 As Object = Nothing
        Dim var9 As Object = Nothing
        Dim Freq As Object
        Dim bApp As Boolean
        Dim str1 As String, str2 As String
        Dim selection1 As String
        Dim selection2 As String
        Dim selection3 As String
        Dim selection4 As String
        Dim selection5 As String
        Dim selection6 As String
        Dim longstatus As Long, longwarnings As Long
        Dim errCode As Long
        Dim el As Double, tl As Double
        Dim i as Long

        ' Open document
        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\mixedmesh-1.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
        Part = swApp.ActiveDoc()

        ' Get the SOLIDWORKS Simulation object
        COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
        If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
        COSMOSWORKS = COSMOSObject.COSMOSWORKS
        If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

        ' Open and get active document
        ActDoc = COSMOSWORKS.ActiveDoc()
        If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

        ' Create new frequency study
        StudyMngr = ActDoc.StudyManager()
        If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
        Study = StudyMngr.CreateNewStudy3("Frequency_Mixed", swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, errCode)
        If Study Is Nothing Then ErrorMsg(swApp, "Frequency study not created")

        ' Get selections for restraint
        ' Faces of the six holes in the solid
        selection1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection1 = selection1 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,16,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection1 = selection1 & ",Type=1"
        StringtoArray(selection1, var1)
        oselect1 = Part.Extension.GetObjectByPersistReference3((var1), longstatus)
        selection2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection2 = selection2 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,15,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection2 = selection2 & ",Type=1"
        StringtoArray(selection2, var2)
        oselect2 = Part.Extension.GetObjectByPersistReference3((var2), longstatus)
        selection3 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection3 = selection3 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,14,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection3 = selection3 & ",Type=1"
        StringtoArray(selection3, var3)
        oselect3 = Part.Extension.GetObjectByPersistReference3((var3), longstatus)
        selection4 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection4 = selection4 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,11,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection4 = selection4 & ",Type=1"
        StringtoArray(selection4, var4)
        oselect4 = Part.Extension.GetObjectByPersistReference3((var4), longstatus)
        selection5 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection5 = selection5 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,12,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection5 = selection5 & ",Type=1"
        StringtoArray(selection5, var5)
        oselect5 = Part.Extension.GetObjectByPersistReference3((var5), longstatus)
        selection6 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
        selection6 = selection6 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,13,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
        selection6 = selection6 & ",Type=1"
        StringtoArray(selection6, var6)
        oselect6 = Part.Extension.GetObjectByPersistReference3((var6), longstatus)

        ' Get selections for contact set
        ' Shell edge
        str1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109"
        str1 = str1 & ",0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,9,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,14,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,0,0,0,0"
        StringtoArray(str1, var8)
        pDisp1 = Part.Extension.GetObjectByPersistReference3((var8), longstatus)
        ' Solid face
        str2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0"
        str2 = str2 & ",112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,11,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
        StringtoArray(str2, var9)
        pDisp2 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

        ' Create arrays
        Dim varArray2 As Object() = {oselect1, oselect2, oselect3, oselect4, oselect5, oselect6}
        Dim varArray3 As Object() = {pDisp1}
        Dim varArray4 As Object() = {pDisp2}

        ' Add bonded contact set
        ContactMgr = Study.ContactManager
        If errCode <> 0 Then ErrorMsg(swApp, "No CWContactManager object")
        CWContactSet = ContactMgr.CreateContactSet2(swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray4), errCode)
        If errCode <> 0 Then ErrorMsg(swApp, "No CWContactSet object")
          Debug.Print(CWContactSet.ContactName & " is suppressed? (1=yes, 0=no) " & CWContactSet.State)

         ' If contact set is suppressed, unsuppress it
         If CWContactSet.State = 1 Then
             errCode = ContactMgr.SuppressUnsuppressContactPair(CWContactSet.ContactName, 0)
         End If

        ' Apply material to shell
        ShellMgr = Study.ShellManager
        If ShellMgr Is Nothing Then ErrorMsg(swApp, "No CWShellManager object")
        Shell = ShellMgr.GetShellAt(0, errCode)
        bApp = Shell.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
        If bApp = False Then ErrorMsg(swApp, "No material applied")

        ' Define shell properties
        Shell.ShellBeginEdit()
        Shell.Formulation = 0
        Shell.ShellUnit = 0
        Shell.ShellThickness = 5.0#
        errCode = Shell.ShellEndEdit
        If errCode <> 0 Then ErrorMsg(swApp, "Shell not created")

        ' Apply material to solid
        SolidMgr = Study.SolidManager
        If SolidMgr Is Nothing Then ErrorMsg(swApp, "No CWSolidManager object")
        SolidComponent = SolidMgr.GetComponentAt(1, errCode)
        If errCode <> 0 Then ErrorMsg(swApp, "No solid component")
        SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
        If errCode <> 0 Then ErrorMsg(swApp, "No solid body")
        bApp = SolidBody.SetLibraryMaterial2("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
        If bApp = False Then ErrorMsg(swApp, "No material applied")

        ' Add fixed restraint
        LBCMgr = Study.LoadsAndRestraintsManager
        CWRes1 = LBCMgr.AddRestraint(swsRestraintType_e.swsRestraintTypeFixed, (varArray2), Nothing, errCode)
        If errCode <> 0 Then ErrorMsg(swApp, "No fixed restraint created")

        ' Set meshing
        CwMesh = Study.Mesh
        If CwMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
        CwMesh.Quality = 1
        Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
        errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
        If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

        ' Run analysis
        errCode = Study.RunAnalysis
        If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

        ' Get results
        CWResult = Study.Results
        If CWResult Is Nothing Then ErrorMsg(swApp, "No CWResults object")
        Freq = CWResult.GetResonantFrequencies(errCode)
        If errCode <> 0 Then ErrorMsg(swApp, "No frequency result")
        Debug.Print("Resonant frequencies:)
        For i = 0 To UBound(Freq)
            Debug.Print (Freq(i))
        Next i

    End Sub

    Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
        swApp.SendMsgToUser2(Message, 0, 0)
        swApp.RecordLine("'*** WARNING - General")
        swApp.RecordLine("'*** " & Message)
        swApp.RecordLine("")

    End Sub

    Private Sub StringtoArray(ByVal inputSTR As String, ByRef varEntity As Object)
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
