---
title: "Apply Material to Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Bodies_Example_VB.htm"
---

# Apply Material to Bodies Example (VBA)

This example shows how to apply user-defined and SOLIDWORKS-defined material to different bodies.

```vb
 '----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click

'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,

'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Verify that the specified material library exists.
' 4. Verify that the specified assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates a nonlinear study.
' 3. Gets the number of components.
' 4. Applies materials to all components.
' 5. Expand the Parts folder in the Simulation Study tree
'    to verify step 4.
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
   Dim SolidMgr As CosmosWorksLib.CWSolidManager
   Dim SolidComponent As CosmosWorksLib.CWSolidComponent
   Dim SolidBody As CosmosWorksLib.CWSolidBody
   Dim errorCode As Long
   Dim longstatus As Long
   Dim longwarnings As Long
   Dim errCode As Long
   Dim CompCount As Integer
   Dim j As Integer
   Dim CWMat As CosmosWorksLib.CWMaterial
   Dim returnValue As Long
   Dim SName As String

   ' Connect to SOLIDWORKS
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    ' Get SOLIDWORKS Simulation object>
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
    If COSMOSObject Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

    ' Open and get document
    SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\basketball_hoop.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    ' Create new nonlinear study
    Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
    Set Study = StudyMngr.CreateNewStudy("Nonlinear", swsAnalysisStudyTypeNonlinear, swsMeshTypeSolid, errCode)
    If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

    ' Get number of solid components
    Set SolidMgr = Study.SolidManager
    If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
    CompCount = SolidMgr.ComponentCount
    Set SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
    If SolidComponent Is Nothing Then ErrorMsg SwApp, "No CWSolidComponent object"

    ' Get name of solid component
    SName = SolidComponent.ComponentName

    ' Apply user-defined material for the first component in the tree
    Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
    If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
    If SolidBody Is Nothing Then ErrorMsg SwApp, "No CWSolidBody object"
    Set CWMat = SolidBody.GetDefaultMaterial
    CWMat.MaterialUnits = 0
    If CWMat Is Nothing Then ErrorMsg SwApp, "No CWMaterial object"
    CWMat.MaterialName = "Alloy Steel"
    CWMat.SetPropertyByName "EX", 210000000000#, 0
    Debug.Print "Property EX: " & CWMat.GetPropertyByName(swsUnitSystemSI, "EX", 0)
    CWMat.SetPropertyByName "NUXY", 0.28, 0
    CWMat.SetPropertyByName "GXY", 79000000000#, 0
    CWMat.SetPropertyByName "DENS", 7700, 0
    CWMat.SetPropertyByName "SIGXT", 723825600, 0
    CWMat.SetPropertyByName "SIGYLD", 620422000, 0
    CWMat.SetPropertyByName "ALPX", 0.000013, 0
    CWMat.SetPropertyByName "KX", 50, 0
    CWMat.SetPropertyByName "C", 460, 0
    errCode = SolidBody.SetSolidBodyMaterial(CWMat)
    If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material"

    ' Apply a different SOLIDWORKS Simulation library material to other components
    Set SolidBody = Nothing
    Set SolidComponent = Nothing
         For j = 1 To (CompCount - 1)
            Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
            SName = SolidComponent.ComponentName
            Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
            If errCode <> 0 Then ErrorMsg SwApp, "No CWSolidBody object"
            returnValue = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "2024 Alloy (SN)")
            If returnValue = 0 Then ErrorMsg SwApp, "No material applied"
            Set SolidBody = Nothing
        Next j
End Sub

' Error function
Function ErrorMsg(SwApp As Object, Message As String)
    SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""

End Function
```
