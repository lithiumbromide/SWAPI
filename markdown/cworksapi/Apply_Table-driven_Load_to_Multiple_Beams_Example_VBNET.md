---
title: "Apply Table-driven Load to Multiple Beams Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm"
---

# Apply Table-driven Load to Multiple Beams Example (VB.NET)

This example shows how to apply a table-driven elliptical load to multiple beams on a part.

```vb
'-------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open the Immediate window.
 ' 4. Ensure that the specified part exists.
 '
 ' Postconditions:
 ' 1. Applies a table-driven elliptical load to the part
 '    and prints its type and other force-related values
 '    in the Immediate window.
 ' 2. To verify, examine the External Loads folder
 '    in Study 3 in the Simulation tree.
 ' 3. Examine the Immediate window.
 '
 ' NOTE: Because this part document is used elsewhere,
 ' do not save any changes when closing it.
 '-------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Imports SolidWorks.Interop.cosworks

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swSelMgr As SelectionMgr
         Dim COSMOSWORKS As Object
         Dim COSMOSObject As CwAddincallback
         Dim swsActDoc As CWModelDoc
         Dim swsStudyMngr As CWStudyManager
         Dim swsStudy As CWStudy
         Dim swsLBCMgr As CWLoadsAndRestraintsManager
         Dim swsCWForce As CWForce
         Dim selBeam1 As Object
         Dim selBeam2 As Object
         Dim selBeam3 As Object
         Dim selBeam4 As Object
         Dim selTrimExtend1 As Object
         Dim selTrimExtend2 As Object
         Dim selTrimExtend3 As Object
         Dim selFace As Object
         Dim data(5) As Double
         Dim rowNum As Integer
         Dim distValue(2) As Double
         Dim forceValue(2) As Double
         Dim errors As Integer
         Dim warnings As Integer
         Dim errCode As Integer
         Dim forceType As String
         Dim fileName As String

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\Loop.sldprt"

         ' Open document
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModel.Extension

         ' Get the SOLIDWORKS Simulation object
         COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "No CWAddincallback object")
         COSMOSWORKS = COSMOSObject.CosmosWorks
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

         ' Get active document
         swsActDoc = COSMOSWORKS.ActiveDoc()
         If swsActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         ' Create new static study
         swsStudyMngr = swsActDoc.StudyManager()
         If swsStudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
         swsStudy = swsStudyMngr.GetStudy(2)
         If swsStudy Is Nothing Then ErrorMsg(swApp, "No CWStudy")

         swsLBCMgr = swsStudy.LoadsAndRestraintsManager

         swSelMgr = swModel.SelectionManager

         ' Select entities
         Call swModel.Extension.SelectByID2("Structural Member1[3]", "SOLIDBODY", 0.2669983091512, -0.4441139265177, -0.05999999999995, True, 0, Nothing, 0)
         selBeam1 = swSelMgr.GetSelectedObject6(1, -1)

         Call swModel.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0.5462661602309, 0.4984264234139, -0.02447052600974, True, 0, Nothing, 0)
         selBeam2 = swSelMgr.GetSelectedObject6(2, -1)

         Call swModel.Extension.SelectByID2("Structural Member1[4]", "SOLIDBODY", -0.364288009376, 0.3216654991368, -0.0596008827161, True, 0, Nothing, 0)
         selBeam3 = swSelMgr.GetSelectedObject6(3, -1)

         Call swModel.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 1.410399123355, -0.191782066378, -0.05999999999989, True, 0, Nothing, 0)
         selBeam4 = swSelMgr.GetSelectedObject6(4, -1)

         Call swModel.Extension.SelectByID2("Trim/Extend3[1]", "SOLIDBODY", 0.3090890041738, -0.1687816014703, -0.01999999999992, True, 0, Nothing, 0)
         selTrimExtend1 = swSelMgr.GetSelectedObject6(5, -1)

         Call swModel.Extension.SelectByID2("Trim/Extend3[2]", "SOLIDBODY", 0.7058778550122, -0.1651708212717, -0.01943888995868, True, 0, Nothing, 0)
         selTrimExtend2 = swSelMgr.GetSelectedObject6(6, -1)

         Call swModel.Extension.SelectByID2("Trim/Extend2[2]", "SOLIDBODY", 0.6681230178383, 0.1527188626094, -0.01999999999998, True, 0, Nothing, 0)
         selTrimExtend3 = swSelMgr.GetSelectedObject6(7, -1)

         Call swModel.Extension.SelectByID2("", "FACE", -0.4332349164914, -0.1431037474702, -0.05999999999989, True, 0, Nothing, 0)
         selFace = swSelMgr.GetSelectedObject6(8, -1)

         Dim beamArray As Object() = {selBeam1, selBeam2, selBeam3, selBeam4, selTrimExtend1, selTrimExtend2, selTrimExtend3}

         ' Create the force
         data(0) = 100.0#
         data(1) = 100.0#
         data(2) = 100.0#
         data(3) = 100.0#
         data(4) = 100.0#
         data(5) = 100.0#
         Dim forceArray As Object() = {data(0), data(1), data(2), data(3), data(4), data(5)}

         rowNum = 3

         distValue(0) = 10.0#
         distValue(1) = 50.0#
         distValue(2) = 100.0#

         forceValue(0) = 100.0#
         forceValue(1) = 0.0#
         forceValue(2) = 50.0#

         ' Table-driven Load: Elliptical
         swsCWForce = swsLBCMgr.AddForce3(swsForceType_e.swsForceTypeForceOrMoment, swsSelectionType_e.swsSelectionBeams, 2, swsTableDrivenInterpolationType_e.swsLinear, swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, True, True, swsBeamNonUniformLoadDef_e.swsTableDrivenLoad, swsBeamNonUniformLoadType_e.swsEllipticalLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
         forceType = "Table-drive Load: Multiple Beams"
         LoadError(swApp, forceType, errCode)
         Debug.Print("  Type as defined in swsForceType_e: " & swsCWForce.ForceType)
         Debug.Print("  Phase angle: " & swsCWForce.PhaseAngle)
         Debug.Print("  Phase unit as defined in swsPhaseAngle_e: " & swsCWForce.PhaseAngleUnit)
         Debug.Print("  Unit as defined in swsForceUnit_e: " & swsCWForce.Unit)
         Debug.Print("  Include nonuniform distribution (1 if nonuniform, 0 if uniform)? " & swsCWForce.IncludeNonUniformDistribution)
         Debug.Print("  Normal force or torque value: " & swsCWForce.IncludeNonUniformDistribution)

         swModel.ClearSelection2(True)

     End Sub

     Sub LoadError(ByVal swApp As Object, ByVal force As String, ByVal errorCode As Long)

         Select Case errorCode
             Case 18
                 ErrorMsg(swApp, "You cannot apply triangular and centered load distribution on multiple beams")
             Case 19
                 ErrorMsg(swApp, "You cannot apply a zero intensity load")
             Case 20
                 ErrorMsg(swApp, "Invalid selection")
             Case 21
                 ErrorMsg(swApp, "The table-driven data is invalid")
             Case 22
                 ErrorMsg(swApp, "In the table-driven distance data, the distance value from the previous row cannot be greater than the distance value in the next row")
             Case Is <> 0
                 ErrorMsg(swApp, "No forces applied")
             Case 0
                 Debug.Print(force)
         End Select
     End Sub

     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String)
         swApp.SendMsgToUser2(Message, 0, 0)
         swApp.RecordLine("'*** WARNING - General")
         swApp.RecordLine("'*** " & Message)
         swApp.RecordLine("")

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
