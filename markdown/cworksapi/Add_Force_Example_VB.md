---
title: "Add Nonuniform Force Distribution Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Force_Example_VB.htm"
---

# Add Nonuniform Force Distribution Example (VBA)

This example shows how to add a force of nonuniform distribution to a study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Verify that the specified assembly exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly.
 ' 2. Inserts a coordinate system.
 ' 3. Gets the Ready study.
 ' 4. Adds a force of nonuniform distribution to Ready.
 ' 5. Inspect the Immediate window.
 '
 ' NOTE: Because this assembly is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
   Dim SwApp As SldWorks.SldWorks
    Dim COSMOSWORKS As Object
    Dim COSMOSObject As CosmosWorksLib.CwAddincallback
    Dim ActDoc As CosmosWorksLib.CWModelDoc
    Dim StudyMngr As CosmosWorksLib.CWStudyManager
    Dim Study As CosmosWorksLib.CWStudy
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
    Dim CWForce As CosmosWorksLib.CWForce
    Dim selection1 As String
    Dim var1 As Variant
    Dim varArray1 As Variant
    Dim oSelect1 As Object
    Dim oSelect2 As Object
    Dim var2 As Variant
    Dim status As Long, warnings As Long
    Dim errCode As Long
    Dim boolstatus As Boolean
   Dim DistanceValues As Variant
    Dim ForceValues As Variant
    Dim ComponentValues As Variant
    Dim data(6) As Double

   Set SwApp = Application.SldWorks
    SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\mixedmesh-1.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", status, warnings
    Set swModel = SwApp.ActiveDoc()
    Set swModelDocExt = swModel.Extension

   ' Insert a coordinate system
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.019197250673983, 0.167840898512935, -3.53306093604147E-02, False, 1, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 1.80650048999951E-02, 0.166100889103177, 0.123043418741133, True, 2, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", 4.76117249541517E-02, 0.243477752733071, -4.18878531492055E-02, True, 4, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "EDGE", -8.21419006116457E-02, 0.165357357368464, -4.11028452107871E-02, True, 8, Nothing, 0)
    boolstatus = swModel.InsertCoordinateSystem(False, False, False)

    ' Get the coordinate system object
    selection1 = "189,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,124,0,0,0"
    selection1 = selection1 & ",Type=1"
    StringtoArray selection1, var2
    Set oSelect2 = swModelDocExt.GetObjectByPersistReference3((var2), status)

   ' Get the SOLIDWORKS Simulation object
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
    If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
   Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"

    Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
   Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"

   ' Get the Ready study
    Set Study = StudyMngr.GetStudy(0)
    If Study Is Nothing Then ErrorMsg SwApp, "No study"

   ' Get the face to which to apply a force
    selection1 = "13,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,"
    selection1 = selection1 & "0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,11,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,0,0,0,0,0,0"
   StringtoArray selection1, var1
   Set oSelect1 = swModelDocExt.GetObjectByPersistReference3((var1), status)
    varArray1 = Array(oSelect1)
   Set LBCMgr = Study.LoadsAndRestraintsManager
   data(0) = 2#
    data(1) = 3#
    data(2) = 1#
    data(3) = 1.5
    data(4) = 1#
    data(5) = 1#
    ComponentValues = data
   ' Add force
    Set CWForce = LBCMgr.AddForce3(swsForceTypeNormal, 0, -1, 0, 0, 0, (DistanceValues), (ForceValues), True, False, 0, 0, 0, 1#, (ComponentValues), False, False, (varArray1), Nothing, False, errCode)
    If errCode <> 0 Then ErrorMsg SwApp, "No force applied"

   ' Edit the force to be of nonuniform distribution
    CWForce.ForceBeginEdit
    CWForce.IncludeNonUniformDistribution = 1
    CWForce.SetCoordinateSystem oSelect2
    CWForce.EquationCoordinateSystemType = 1
    CWForce.EquationLinearUnit = 0
    CWForce.Equation = """x"" + ""y"" + ""z"""
    CWForce.ForceEndEdit

   Debug.Print "Force:"
    Debug.Print "  Type as defined in swsForceType_e: " & CWForce.ForceType
    Debug.Print "  Units as defined in swsForceUnit_e: " & CWForce.Unit
    Debug.Print "  Value: " & CWForce.NormalForceOrTorqueValue
    Debug.Print "  Nonuniform distribution? (1=yes, 0=no) " & CWForce.IncludeNonUniformDistribution
    If CWForce.IncludeNonUniformDistribution = 1 Then
       Debug.Print "  Coordinate system type as defined in swsCoordinateType_e: " & CWForce.EquationCoordinateSystemType
       Debug.Print "  Equation linear units as defined in swsLinearUnit_e: " & CWForce.EquationLinearUnit
       If CWForce.EquationCoordinateSystemType = 2 Or CWForce.EquationCoordinateSystemType = 3 Then
           Debug.Print "  Equation angular units as defined in " & CWForce.EquationAngularUnit
       End If
      If CWForce.Equation = "" Then
           Debug.Print "  Nonuniform force distribution equation not set."
       Else
           Debug.Print "  Nonuniform force distribution equation: " & CWForce.Equation
       End If
    End If
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
