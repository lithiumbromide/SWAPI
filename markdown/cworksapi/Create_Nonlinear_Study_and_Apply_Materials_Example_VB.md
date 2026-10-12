---
title: "Create Nonlinear Study and Apply Materials Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm"
---

# Create Nonlinear Study and Apply Materials Example (VBA)

This example shows how to create a nonlinear study and apply user-defined and SOLIDWORKS materials to an assembly's components.

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
' 3. Applies user-defined material to the first component and
'    SOLIDWORKS material to the remaining components.
' 4. To verify, expand the Parts folder in the Simulation Study tree,
'    which is located beneath the FeatureManager design tree, and
'    observe the names of the materials applied to holder-1 and pipe-1.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
Sub main()

   Dim SwApp As SldWorks.SldWorks
   Dim COSMOSWORKS As Object
   Dim COSMOSObject As Object
   Dim ActDoc As CosmosWorksLib.CWModelDoc
   Dim StudyMngr As CosmosWorksLib.CWStudyManager
   Dim Study As CosmosWorksLib.CWStudy
   Dim SolidMgr As CosmosWorksLib.CWSolidManager
   Dim SolidComponent As CosmosWorksLib.CWSolidComponent
   Dim SolidBody As CosmosWorksLib.CWSolidBody
   Dim SName As String
   Dim errors As Long, warnings As Long
   Dim errorCode As Long
   Dim errCode As Long
   Dim CompCount As Integer
   Dim j As Integer
   Dim CWMat As CosmosWorksLib.CWMaterial
   Dim bApp As Boolean
   Dim swVersion As Long
   Dim cwVersion As Long
   Dim cwProgID As String

    ' Connect to SOLIDWORKS
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

   'Determine host SOLIDWORKS version

     swVersion  = Left(SwApp.RevisionNumber, 2)

     'Calculate the correct Simulation ProgID for this version of SOLIDWORKS

     cwVersion  =  swVersion  -  15

     cwProgID  =  "SldWorks.Simulation." & cwVersion

     Debug.Print (cwProgID)

    ' Get the SOLIDWORKS Simulation object
    Set COSMOSObject = SwApp.GetAddInObject(cwProgID)
    If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found", True
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
    If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found", True

    ' Open and get the active document
    SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Nonlinear\nl_pipe_holder.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document", True

    ' Create new nonlinear study
    Set StudyMngr = ActDoc.StudyManager()
    If StudyMngr Is Nothing Then ErrorMsg SwApp, "CWStudyManager object not created", True
    Set Study = StudyMngr.CreateNewStudy("NonLinear", swsAnalysisStudyTypeNonlinear, swsMeshTypeSolid, errCode)

    If Study Is Nothing Then ErrorMsg SwApp, "Study not created", True

    ' Get number of solid components
    Set SolidMgr = Study.SolidManager
    If SolidMgr Is Nothing Then ErrorMsg SwApp, "CWSolidManager object not created", True
    CompCount = SolidMgr.ComponentCount
    Set SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
    If SolidComponent Is Nothing Then ErrorMsg SwApp, "CWSolidComponent object not created", True

    ' Get name of solid component
    SName = SolidComponent.ComponentName

    ' Apply user-defined material to the first component in the tree
    Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
    If errCode <> 0 Then ErrorMsg SwApp, "No solid body", True
    If SolidBody Is Nothing Then ErrorMsg SwApp, "CWSolidBody object not created", True
    Set CWMat = SolidBody.GetDefaultMaterial
    CWMat.MaterialUnits = 0
    If CWMat Is Nothing Then ErrorMsg SwApp, "No default material object", True
    CWMat.MaterialName = "Alloy Steel"
    Call CWMat.SetPropertyByName("EX", 210000000000#, 0)
    Call CWMat.SetPropertyByName("NUXY", 0.28, 0)
    Call CWMat.SetPropertyByName("GXY", 79000000000#, 0)
    Call CWMat.SetPropertyByName("DENS", 7700, 0)
    Call CWMat.SetPropertyByName("SIGXT", 723825600, 0)
    Call CWMat.SetPropertyByName("SIGYLD", 620422000, 0)
    Call CWMat.SetPropertyByName("ALPX", 0.000013, 0)
    Call CWMat.SetPropertyByName("KX", 50, 0)
    Call CWMat.SetPropertyByName("C", 460, 0)
    errCode = SolidBody.SetSolidBodyMaterial(CWMat)
    If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material", True

    ' Apply SOLIDWORKS library material to rest of components
    Set SolidBody = Nothing
    Set SolidComponent = Nothing
    For j = 1 To (CompCount - 1)
        Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
        SName = SolidComponent.ComponentName
        Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
        If errCode <> 0 Then ErrorMsg SwApp, "No solid body", True
        bApp = SolidBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Gray Cast Iron (SN)")
        If bApp = False Then ErrorMsg SwApp, "No material applied", True
        Set SolidBody = Nothing
    Next j

End Sub

' Error function
Function ErrorMsg(SwApp As SldWorks.SldWorks, Message As String, EndTest As Boolean)
    SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""
    If EndTest Then
    End If
End Function
```
