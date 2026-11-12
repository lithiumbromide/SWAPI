---
title: "Simultaneously Edit Multiple Contact Sets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Simultaneously_Edit_Multiple_Contact_Sets_Example_VB.htm"
---

# Simultaneously Edit Multiple Contact Sets Example (VBA)

This example shows how to add multiple contact sets to a frequency study and simultaneously edit them.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model document exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Gets the Ready study.
 ' 3. Adds two contact sets.
 ' 4. Simultaneously edits the contact sets to change types
 '    from Bonded to Allow Penetration.
 ' 5. Creates a mesh.
 ' 6. Runs an analysis.
 ' 7. Inspect the Immediate window and the Simulation Study tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim SwApp As SldWorks.SldWorks
     Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim COSMOSObject As CosmosWorksLib.CwAddincallback
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CWMesh As CosmosWorksLib.CWMesh
     Dim CWResult As CosmosWorksLib.CWResults
     Dim Part As SldWorks.ModelDoc2
     Dim ContactMgr As CosmosWorksLib.CWContactManager
     Dim CWContactSet As CosmosWorksLib.CWContactSet
     Dim pDisp1 As Object, pDisp2 As Object, pDisp3 As Object
     Dim var8 As Variant, var9 As Variant, var10 As Variant
     Dim varArray3 As Variant, varArray4 As Variant, varArray5 As Variant
     Dim Freq As Variant
     Dim str1 As String, str2 As String, str3 As String
     Dim longstatus As Long, longwarnings As Long
     Dim errCode As Long
     Dim el As Double, tl As Double
     Dim i As Long

    Set SwApp = Application.SldWorks
     SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
     Set Part = SwApp.ActiveDoc()
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
    ' Gets the Ready study
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
    Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No study found"
    ' Get selections for multiple contact sets

     ' Shaft source
     str1 = "189,35,0,0,3,0,0,0,255,254,255,23,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,13,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,58,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,"
     str1 = str1 & "9,128,255,254,255,15,111,0,118,0,101,0,114,0,101,0,110,0,100,0,101,0,114,0,32,0,115,0,104,0,97,0,102,0,116,0,2,0,0,5,73,58,52,255,254,255,0,0,123,22,28,65,1,0,0,0,0,0,0,0,35,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,45,0,0,0,0,0,0,0,123,22,28,65,10,0,0,0,65,73,58,52,1,0,0,0,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,13,0,0,0,97,73,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,14,0,0,0,108,73,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str1 = str1 & ",Type=1"
    StringtoArray str1, var8
     Set pDisp1 = Part.Extension.GetObjectByPersistReference3((var8), longstatus)

    ' Bore 1 target
     str2 = "189,35,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,50,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,46,0,8"
     str2 = str2 & "3,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,255,254,255,0,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,15,0,0,0,58,68,58,52,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,15,0,0,0,58,68,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,19,0,0,0,141,68,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str2 = str2 & ",Type=1"
    StringtoArray str2, var9
     Set pDisp2 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

    ' Bore 2 target
     str3 = "189,35,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,20,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,46,0,8"
     str3 = str3 & "3,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,255,254,255,0,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,15,0,0,0,58,68,58,52,1,0,0,0,255,255,255,255,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,15,0,0,0,58,68,58,52,1,0,0,0,0,0,12,128,0,0,5,128,8,0,19,0,0,0,141,68,58,52,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str3 = str3 & ",Type=1"
    StringtoArray str3, var10
     Set pDisp3 = Part.Extension.GetObjectByPersistReference3((var10), longstatus)

    ' Create arrays
     varArray3 = Array(pDisp1)
     varArray4 = Array(pDisp2)
     varArray5 = Array(pDisp3)

    ' Add bonded contact sets
     Set ContactMgr = Study.ContactManager
     If errCode <> 0 Then ErrorMsg SwApp, "No ContactManager object"

    Set CWContactSet = ContactMgr.CreateContactSet2(swsContactTypeBonded, 0, (varArray3), (varArray4), errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No CWContactSet object"

    Set CWContactSet = ContactMgr.CreateContactSet2(swsContactTypeBonded, 0, (varArray3), (varArray5), errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No CWContactSet object"

    ' Simultaneously edit both contact sets
     Dim multCSEM As CWMultipleContactSetsEditManager
     Set multCSEM = Study.MultipleContactSetsEditManager

    errCode = multCSEM.AddContactSet("Contact Set-1")
     errCode = multCSEM.AddContactSet("Contact Set-2")
     Debug.Print "Number of contact sets added: " & multCSEM.GetContactSetCount
     multCSEM.MultipleContactSetsBeginEdit
     errCode = multCSEM.SetAsDefaultContactSet("Contact Set-1")
     errCode = multCSEM.SetContactType(swsContactTypeFreeOrInsulated)
     multCSEM.MultipleContactSetsEndEdit

    ' Mesh
     Set CWMesh = Study.Mesh
     If CWMesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
    CWMesh.Quality = 1
     Call CWMesh.GetDefaultElementSizeAndTolerance(swsLinearUnitMillimeters, el, tl)
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    ' Get results
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "No result object"
    Freq = CWResult.GetResonantFrequencies(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No frequency result"

    Debug.Print "Resonant frequencies:"
    For i = 0 To UBound(Freq)
        Debug.Print Freq(i)
     Next i
End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
   SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""
End Sub
Function StringtoArray(inputSTR As String, varEntity As Variant)
   Dim PID() As Byte
    Dim i As Integer
   varEntity = Split(inputSTR, ",")
    ReDim PID(UBound(varEntity))
   For i = 0 To (UBound(varEntity) - 1)
     PID(i) = varEntity(i)
    Next i
   varEntity = PID
End Function
```
