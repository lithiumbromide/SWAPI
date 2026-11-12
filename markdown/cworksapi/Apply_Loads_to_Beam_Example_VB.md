---
title: "Apply Loads to Beams Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Loads_to_Beam_Example_VB.htm"
---

# Apply Loads to Beams Example (VBA)

This example shows how to apply the total force, or load, along the length of a beam in various types of distributions.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).
' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Open the Immediate window.
' 4. Ensure that the specified part document exists.
'
' Postconditions:
' 1. Loads are applied to the part, and their
'    distribution types are shown in the Immediate
'    window.
' 2. To verify, examine the External Loads folder
'    in Study 3 in the Simulation tree.
'
' NOTE: Because this part document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
   Dim swApp As SldWorks.SldWorks
   Dim swModel As SldWorks.ModelDoc2
   Dim swModelDocExt As SldWorks.ModelDocExtension
   Dim swSelMgr As SldWorks.SelectionMgr
   Dim COSMOSWORKS As Object
   Dim COSMOSObject As CosmosWorksLib.CwAddincallback
   Dim swsActDoc As CosmosWorksLib.CWModelDoc
   Dim swsStudyMngr As CosmosWorksLib.CWStudyManager
   Dim swsStudy As CosmosWorksLib.CWStudy
   Dim swsLBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
   Dim swsCWForce As CosmosWorksLib.CWForce
   Dim beamArray As Variant
   Dim selBeam As Object
   Dim selFace As Object
   Dim forceArray As Variant
   Dim data(6) As Double
   Dim rowNum As Long
   Dim distValue(3) As Double
   Dim forceValue(3) As Double
   Dim errors As Long
   Dim warnings As Long
   Dim errCode As Long
   Dim forceType As String
```

```
   Const fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\Loop.sldprt"
```

```
   ' Open document
   Set swApp = Application.SldWorks
   Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
   Set swModelDocExt = swModel.Extension
```

```
   ' Get the SOLIDWORKS Simulation object
   Set COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
   If COSMOSObject Is Nothing Then ErrorMsg swApp, "No CwAddincallback object"
   Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
   If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "No COSMOSWORKS object"
```

```
   ' Open and get active document
   Set swsActDoc = COSMOSWORKS.ActiveDoc()
   If swsActDoc Is Nothing Then ErrorMsg swApp, "No active document"
```

```
   ' Get the static study
   Set swsStudyMngr = swsActDoc.StudyManager()
   If swsStudyMngr Is Nothing Then ErrorMsg swApp, "No CWStudyManager object"
   Set swsStudy = swsStudyMngr.GetStudy(2)
   If swsStudy Is Nothing Then ErrorMsg swApp, "No CWStudy object"
```

```
   Set swsLBCMgr = swsStudy.LoadsAndRestraintsManager
```

```
   Set swSelMgr = swModel.SelectionManager
```

```
   ' Select the beam and the face to which to apply the force
   Call swModel.Extension.SelectByID2("Structural Member1[3]", "SOLIDBODY", 0.2669983091512, -0.4441139265177, -0.05999999999995, True, 0, Nothing, 0)
   Set selBeam = swSelMgr.GetSelectedObject6(1, -1)
```

```
   Call swModel.Extension.SelectByID2("", "FACE", -0.4332349164914, -0.1431037474702, -0.05999999999989, True, 0, Nothing, 0)
   Set selFace = swSelMgr.GetSelectedObject6(2, -1)
```

```
   beamArray = Array(selBeam)
```

```
   ' Create the force
   data(0) = 100
   data(1) = 100#
   data(2) = 100#
   data(3) = 100#
   data(4) = 100#
   data(5) = 100#
   forceArray = data
```

```
   rowNum = 3
```

```
   distValue(0) = 10#
   distValue(1) = 50#
   distValue(2) = 100#
```

```
   forceValue(0) = 100#
   forceValue(1) = 0#
   forceValue(2) = 50#
```

```
   ' Add force: Total Load - Triangular
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsTotalLoad, swsTriangularLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Total Load - Triangular"
   LoadError swApp, forceType, errCode
```

```
   ' Add force: Total Load - Elliptical
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsTotalLoad, swsEllipticalLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Total Load - Elliptical"
   LoadError swApp, forceType, errCode
```

```
   ' Add force: Total Load - Parabolic
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsTotalLoad, swsParabolicLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Total Load - Parabolic"
   LoadError swApp, forceType, errCode
```

```
   ' Add force: Centered Load - Triangular
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsCentralLoad, swsTriangularLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Centered Load - Triangular"
   LoadError swApp, forceType, errCode
```

```
   ' Add force: Centered Load - Elliptical
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsCentralLoad, swsEllipticalLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Centered Load - Elliptical"
   LoadError swApp, forceType, errCode
```

```
   ' Add force: Centered Load - Parabolic
   Set swsCWForce = swsLBCMgr.AddForce3(swsForceTypeForceOrMoment, swsSelectionBeams, 2, swsLinear, swsPercentage, rowNum, distValue, forceValue, True, True, swsCentralLoad, swsParabolicLoad, 4, 100, (forceArray), False, False, (beamArray), selFace, True, errCode)
   forceType = "Centered Load - Parabolic"
   LoadError swApp, forceType, errCode
```

```
End Sub
```

```
Function LoadError(swApp As Object, force As String, errorCode As Long)
```

```
   Select Case errorCode
        Case 18
            ErrorMsg swApp, "You cannot apply triangular and centered-load distribution on multiple beams"
        Case 19
            ErrorMsg swApp, "You cannot apply a zero-intensity load"
        Case 20
            ErrorMsg swApp, "Invalid selection"
        Case 21
            ErrorMsg swApp, "The table-driven data is invalid"
        Case 22
            ErrorMsg swApp, "In the table-driven distance data, the distance value from the previous row cannot be greater than the distance value in the next row"
        Case Is <> 0
            ErrorMsg swApp, "No forces applied"
        Case 0
            Debug.Print (force)
   End Select
End Function
```

```
Function ErrorMsg(swApp As Object, Message As String)
   swApp.SendMsgToUser2 Message, 0, 0
   swApp.RecordLine "'*** WARNING - General"
   swApp.RecordLine "'*** " & Message
   swApp.RecordLine ""

End Function
```
