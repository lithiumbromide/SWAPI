---
title: "Apply Material to Bodies Example(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Bodies_Example_VBNET.htm"
---

# Apply Material to Bodies Example(VB.NET)

## Apply Material to Bodies Example (VB.NET)

This example shows how to apply user-defined and SOLIDWORKS-defined materials to different bodies.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).
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
'-------------------------------
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
            Dim errorCode As Long
            Dim longstatus As Long
            Dim longwarnings As Long
            Dim errCode As Long
            Dim CompCount As Integer
            Dim j As Integer
            Dim CWMat As CWMaterial
            Dim returnValue As Long
            Dim SName As String

            ' Get SOLIDWORKS Simulation object>
            COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
            If COSMOSObject Is Nothing Then ErrorMsg("No CWAddincallback object")
            COSMOSWORKS = COSMOSObject.CosmosWorks
            If COSMOSWORKS Is Nothing Then ErrorMsg("No COSMOSWORKS object")

            ' Open and get document
            swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\basketball_hoop.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
            ActDoc = COSMOSWORKS.ActiveDoc()
            If ActDoc Is Nothing Then ErrorMsg("No active document")

            ' Create new nonlinear study
            StudyMngr = ActDoc.StudyManager()
            If StudyMngr Is Nothing Then ErrorMsg("No CWStudyManager object")
            Study = StudyMngr.CreateNewStudy("Nonlinear", swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear, swsMeshType_e.swsMeshTypeSolid, errCode)
            If Study Is Nothing Then ErrorMsg("No CWStudy object")

            ' Get number of solid components
            SolidMgr = Study.SolidManager
            If SolidMgr Is Nothing Then ErrorMsg("No CWSolidManager object")
            CompCount = SolidMgr.ComponentCount
            SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
            If SolidComponent Is Nothing Then ErrorMsg("No CWSolidComponent object")

            ' Get name of solid component
            SName = SolidComponent.ComponentName

            ' Apply user-defined material for the first component in the tree
            SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
            If errCode <> 0 Then ErrorMsg("No solid body")
            If SolidBody Is Nothing Then ErrorMsg("No CWSolidBody object")
            CWMat = SolidBody.GetDefaultMaterial
            CWMat.MaterialUnits = 0
            If CWMat Is Nothing Then ErrorMsg("No CWMaterial object")
            CWMat.MaterialName = "Alloy Steel"
            CWMat.SetPropertyByName("EX", 210000000000.0#, 0)
        Debug.Print("Property EX: " & CWMat.GetPropertyByName(swsUnitSystem_e.swsUnitSystemSI, "EX", 0))
            CWMat.SetPropertyByName("NUXY", 0.28, 0)
            CWMat.SetPropertyByName("GXY", 79000000000.0#, 0)
            CWMat.SetPropertyByName("DENS", 7700, 0)
            CWMat.SetPropertyByName("SIGXT", 723825600, 0)
            CWMat.SetPropertyByName("SIGYLD", 620422000, 0)
            CWMat.SetPropertyByName("ALPX", 0.000013, 0)
            CWMat.SetPropertyByName("KX", 50, 0)
            CWMat.SetPropertyByName("C", 460, 0)
            errCode = SolidBody.SetSolidBodyMaterial(CWMat)
            If errCode <> 0 Then ErrorMsg("Failed to apply material")

            ' Apply a different SOLIDWORKS Simulation library material to rest of components
            SolidBody = Nothing
            SolidComponent = Nothing
            For j = 1 To (CompCount - 1)
                SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
                SName = SolidComponent.ComponentName
                SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
            If errCode <> 0 Then ErrorMsg("No CWSolidbody object")
                returnValue = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "2024 Alloy (SN)")
            If returnValue = 0 Then ErrorMsg("No material applied")
                SolidBody = Nothing
            Next j
        End Sub

        ' Error function
        Private Sub ErrorMsg(ByVal Message As String)
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
