---
title: "Create Nonlinear Study and Apply Materials Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm"
---

# Create Nonlinear Study and Apply Materials Example (VB.NET)

This example shows how to create a nonlinear study and apply user-defined and SOLIDWORKS materials to assembly components.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).

 ' 3. Add System.Windows.Forms as a reference.
' 4. Verify that the specified material library exists.
' 5. Verify that the specified assembly exists.
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
' NOTE: Because the assembly document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics
Imports System.Windows.Forms

 Partial Class SolidWorksMacro
     Public Sub main()

         Dim COSMOSWORKS As Object
         Dim COSMOSObject As Object
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim SolidMgr As CWSolidManager
         Dim SolidComponent As CWSolidComponent
         Dim SolidBody As CWSolidBody
         Dim SName As String
         Dim errors As Integer, warnings As Integer
         Dim errorCode As Integer
         Dim errCode As Integer
         Dim CompCount As Integer
         Dim j As Integer
         Dim CWMat As CWMaterial
         Dim bApp As Boolean
         Dim swVersion As Integer
         Dim cwVersion As Integer
         Dim cwProgID As String

         'Determine host SOLIDWORKS version
         swVersion = Convert.ToInt32(swApp.RevisionNumber().Substring(0, 2))
         'Calculate the correct Simulation ProgID for this version of SOLIDWORKS
         cwVersion = swVersion - 15
         cwProgID = String.Format("SldWorks.Simulation.{0}", cwVersion)
         Debug.Print(cwProgID)

         ' Get the SOLIDWORKS Simulation object
         COSMOSObject = swApp.GetAddInObject(cwProgID)
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found", True)
         COSMOSWORKS = COSMOSObject.CosmosWorks
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found", True)

         ' Open and get the active document
         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Nonlinear\nl_pipe_holder.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document", True)

         ' Create new nonlinear study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "CWStudyManager object not created", True)
         Study = StudyMngr.CreateNewStudy("Nonlinear", swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear, swsMeshType_e.swsMeshTypeSolid, errCode)
         If Study Is Nothing Then ErrorMsg(swApp, "Study not created", True)

         ' Get number of solid components
         SolidMgr = Study.SolidManager
         If SolidMgr Is Nothing Then ErrorMsg(swApp, "CWSolidManager object not created", True)
         CompCount = SolidMgr.ComponentCount
         SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
         If SolidComponent Is Nothing Then ErrorMsg(swApp, "CWSolidComponent object not created", True)

         ' Get name of solid component
         SName = SolidComponent.ComponentName

         ' Apply user-defined material to the first component in the tree
         SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No solid body", True)
         If SolidBody Is Nothing Then ErrorMsg(swApp, "CWSolidBody object not created", True)
         CWMat = SolidBody.GetDefaultMaterial
         CWMat.MaterialUnits = 0
         If CWMat Is Nothing Then ErrorMsg(swApp, "No default material object", True)
         CWMat.MaterialName = "Alloy Steel"
         Call CWMat.SetPropertyByName("EX", 210000000000.0#, 0)
         Call CWMat.SetPropertyByName("NUXY", 0.28, 0)
         Call CWMat.SetPropertyByName("GXY", 79000000000.0#, 0)
         Call CWMat.SetPropertyByName("DENS", 7700, 0)
         Call CWMat.SetPropertyByName("SIGXT", 723825600, 0)
         Call CWMat.SetPropertyByName("SIGYLD", 620422000, 0)
         Call CWMat.SetPropertyByName("ALPX", 0.000013, 0)
         Call CWMat.SetPropertyByName("KX", 50, 0)
         Call CWMat.SetPropertyByName("C", 460, 0)
         errCode = SolidBody.SetSolidBodyMaterial(CWMat)
         If errCode <> 0 Then ErrorMsg(swApp, "Failed to apply material", True)

         ' Apply SOLIDWORKS library material to rest of components
         SolidBody = Nothing
         SolidComponent = Nothing
         For j = 1 To (CompCount - 1)
             SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
             SName = SolidComponent.ComponentName
             SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
             If errCode <> 0 Then ErrorMsg(swApp, "No solid body", True)
             bApp = SolidBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Gray Cast Iron (SN)")
             If bApp = False Then ErrorMsg(swApp, "No material applied", True)
             SolidBody = Nothing
         Next j

     End Sub
     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String, ByVal EndTest As Boolean)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
         If EndTest Then
         End If
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
 End Class
```
