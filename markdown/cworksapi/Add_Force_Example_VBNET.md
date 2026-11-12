---
title: "Add Nonuniform Force Distribution Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Force_Example_VBNET.htm"
---

# Add Nonuniform Force Distribution Example (VB.NET)

This example shows how to add a force of nonuniform distribution to a study.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Verify that the assembly exists.
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
  '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports SolidWorks.Interop.cosworks
 Imports System.Diagnostics
 Imports System.Collections

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim COSMOSWORKS As CosmosWorks
         Dim COSMOSObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim LBCMgr As CWLoadsAndRestraintsManager
         Dim CWForce As CWForce
         Dim var1 As Object = Nothing
         Dim var2 As Object = Nothing
         Dim oSelect1 As Object, oSelect2 As Object
         Dim status As Integer, warnings As Integer
         Dim errCode As Integer
         Dim PIDCollection As New Collection
         Dim boolstatus As Boolean
         Dim DistanceValues As Object = Nothing
         Dim ForceValues As Object = Nothing
         Dim ComponentValues As Object
         Dim data(6) As Double

         ' Initialize PIDs
         PIDCollection = PIDInitializer()

         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\mixedmesh-1.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", status, warnings)
         swModel = swApp.ActiveDoc()
         swModelDocExt = swModel.Extension

         ' Insert a coordinate system
         boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.019197250673983, 0.167840898512935, -0.0353306093604147, False, 1, Nothing, 0)
         boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.0180650048999951, 0.166100889103177, 0.123043418741133, True, 2, Nothing, 0)
         boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.0476117249541517, 0.243477752733071, -0.0418878531492055, True, 4, Nothing, 0)
         boolstatus = swModelDocExt.SelectByID2("", "EDGE", -0.0821419006116457, 0.165357357368464, -0.0411028452107871, True, 8, Nothing, 0)
         boolstatus = swModel.InsertCoordinateSystem(False, False, False)

         ' Get the coordinate system object
         SelectByPID("selection2", PIDCollection, var2)
         oSelect2 = swModelDocExt.GetObjectByPersistReference3((var2), status)

         COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")

         COSMOSWORKS = COSMOSObject.CosmosWorks
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")

         ' Get the Ready study
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(swApp, "No study found")

         ' Get the face to which to apply the force
         SelectByPID("selection1", PIDCollection, var1)
         oSelect1 = swModelDocExt.GetObjectByPersistReference3((var1), status)
         Dim DispArray1 As Object() = {oSelect1}

         LBCMgr = Study.LoadsAndRestraintsManager

        Data(0) = 2.0#
         Data(1) = 3.0#
         Data(2) = 1.0#
         Data(3) = 1.5
         Data(4) = 1.0#
         Data(5) = 1.0#
         ComponentValues = data

         ' Add force
         CWForce = LBCMgr.AddForce3(swsForceType_e.swsForceTypeNormal, 0, -1, 0, 0, 0, (DistanceValues), (ForceValues), True, False, 0, 0, 0, 1.0#, (ComponentValues), False, False, (DispArray1), Nothing, False, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No force applied")

         ' Edit the force to be of nonuniform distribution
         CWForce.ForceBeginEdit()
         CWForce.IncludeNonUniformDistribution = 1
         CWForce.SetCoordinateSystem(oSelect2)
         CWForce.EquationCoordinateSystemType = 1
         CWForce.EquationLinearUnit = 0
         CWForce.Equation =  """x"" + ""y"" + ""z"""
         CWForce.ForceEndEdit()

         Debug.Print("Force:")
         Debug.Print("  Type as defined in swsForceType_e: " & CWForce.ForceType)
         Debug.Print("  Units as defined in swsForceUnit_e: " & CWForce.Unit)
         Debug.Print("  Value: " & CWForce.NormalForceOrTorqueValue)
         Debug.Print("  Nonuniform distribution? (1=yes, 0=no) " & CWForce.IncludeNonUniformDistribution)
         If CWForce.IncludeNonUniformDistribution = 1 Then
             Debug.Print("  Coordinate system type as defined in swsCoordinateType_e: " & CWForce.EquationCoordinateSystemType)
             Debug.Print("  Equation linear units as defined in swsLinearUnit_e: " & CWForce.EquationLinearUnit)
             If CWForce.EquationCoordinateSystemType = 2 Or CWForce.EquationCoordinateSystemType = 3 Then
                 Debug.Print("  Equation angular units as defined in " & CWForce.EquationAngularUnit)
             End If
             If CWForce.Equation = "" Then
                 Debug.Print("  Nonuniform force distribution equation not set.")
             Else
                 Debug.Print("  Nonuniform force distribution equation: " & CWForce.Equation)
             End If
         End If

     End Sub

     Private Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)

         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")

     End Sub

     Public Function PIDInitializer() As Collection

         ' Initialize PIDs
         Dim PIDCollection As New Collection
         Dim selection1 As String, selection2 As String

         ' Face
         selection1 = "13,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,"
         selection1 = selection1 & "0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,11,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,0,0,0,0,0,0"

         ' Coordinate System
         selection2 = "189,35,0,0,1,0,0,0,255,254,255,0,0,0,0,0,124,0,0,0"
         selection2 = selection2 & ",Type=1"

         ' Store constants in a collection
         PIDCollection.Add(selection1, "selection1")
         PIDCollection.Add(selection2, "selection2")

         PIDInitializer = PIDCollection

     End Function

     Private Sub SelectByPID(ByVal PIDName As String, ByVal PIDCollection As Collection, ByRef varEntity As Object)

         ' Select by PID
         Dim PID() As Byte
         Dim PIDVariant As Object
         Dim PIDString As String
         Dim i As Integer

         ' Get the string from the collection
         PIDString = ""
         PIDString = PIDCollection.Item(PIDName)

         ' Parse the string into an array
         PIDVariant = Split(PIDString, ",")
         ReDim PID(UBound(PIDVariant))

         ' Change the array to a byte array
         For i = 0 To (UBound(PIDVariant) - 1)
             PID(i) = Convert.ToByte(PIDVariant(i))
         Next i

         varEntity = PID

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>

     Public swApp As SldWorks

 End Class
```
