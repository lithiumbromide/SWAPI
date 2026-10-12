---
title: "Get and Set Beams and Joints Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_and_Set_Beams_and_Joints_Example_VBNET.htm"
---

# Get and Set Beams and Joints Example (VB.NET)

This example shows how to get and set beams and joints.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified part exists.
 ' 4. Ensure that the specified material library exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates static study, frame.
 ' 2. Prints beam information to the Immediate window.
 ' 3. Applies Plain Carbon Steel material to all beams.
 ' 4. Calculates joints for all beams and displays a neutral axis for
 '    each beam.
 ' 5. Prints the pinball tolerance value and unit to the Immediate window.
 ' 6. Creates a mixed mesh and prints its type and state to the
 '    Immediate window.
 '
 ' NOTES:
 ' *  Creates beam elements by default for parts with structural members.
 ' *  Because the part document is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Public Sub main()
        Dim COSMOSWORKS As CosmosWorks
        Dim COSMOSObject As CwAddincallback
        Dim ActDoc As CWModelDoc
        Dim StudyMngr As CWStudyManager
        Dim Study As CWStudy
        Dim BeamMgr As CWBeamManager
        Dim BeamBody As CWBeamBody
        Dim Joints As CWJoints
        Dim Mesh As CWMesh
        Dim nbrBeamBodies As Integer
        Dim beamBodyType As Integer
        Dim ElementSize As Double
        Dim Tolerance As Double
        Dim errors As Integer, warnings As Integer
        Dim errCode As Integer
        Dim j As Integer
        Dim bApp As Boolean
```

Dim keepJointUpdates As Boolean

```vb
        'Get the SOLIDWORKS Simulation object
        COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
        If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
        COSMOSWORKS = COSMOSObject.CosmosWorks
        If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

        'Open and get the active document
        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        ActDoc = COSMOSWORKS.ActiveDoc()
        If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

        'Create new static study named frame
        StudyMngr = ActDoc.StudyManager()
        If StudyMngr Is Nothing Then ErrorMsg(swApp, "CWStudyManager object not found")
        Study = StudyMngr.CreateNewStudy3("frame", swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, errCode)
        If Study Is Nothing Then ErrorMsg(swApp, "Study not created")

        'Get and set beam info
        BeamMgr = Study.BeamManager
        nbrBeamBodies = BeamMgr.BeamCount
        Debug.Print("Beams...")
        Debug.Print("  Number of beams: " & nbrBeamBodies)
        BeamBody = Nothing
        For j = 0 To (nbrBeamBodies - 1)
            BeamBody = BeamMgr.GetBeamBodyAt(j, errCode)
            If errCode <> 0 Then ErrorMsg(swApp, "No beam body")
            Debug.Print("    Name of beam body: " & BeamBody.BeamBodyName)
            beamBodyType = BeamBody.BeamType
            If beamBodyType = 0 Then
                Debug.Print("      Type of beam body: beam")
            Else
                Debug.Print("      Type of beam body: truss")
            End If
             Debug.Print("      Beam cross-section properties:")

             Debug.Print("         Maximum distance from the shear center to the furthest point: " & BeamBody.BeamDistForMaxShearStress)

             Debug.Print("         Beam shear:")

             Debug.Print("           Direction 1: " & BeamBody.BeamShearY)

             Debug.Print("           Direction 2: " & BeamBody.BeamShearZ)

             Debug.Print("         Beam torsional stiffness constant: " & BeamBody.BeamTorsionalConstant)

             Debug.Print("           Units of length as defined in swsLinearUnit_e: " & BeamBody.BeamTorsionalConstantUnit)
            bApp = BeamBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Plain Carbon Steel")
            If bApp = False Then ErrorMsg(swApp, "No material applied")
            BeamBody = Nothing
        Next j

        'Calculate joints
        Joints = BeamMgr.GetJointGroup(errCode)
        Debug.Print(" ")
        Debug.Print("Joints...")
        If errCode <> 0 Then ErrorMsg(swApp, "No joint group")
        Joints.JointsBeginEdit()
        Joints.IncludeAllSelectedBeam = True
        Joints.IncludeDisplayNeutralAxis = True
        Joints.CalculateJoints()
        Joints.JointsEndEdit()
```

```vb
        keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate
        If (keepJointUpdates = True) Then
           Debug.Print(" Keep joint updates: yes")
        Else
           Debug.Print(" Keep joint updates: no")
        End If
        Debug.Print(" Overwrite pinball value: " & Joints.IncludeTreatAsJointForClearanceLessThan)
```

```vb
        Debug.Print("  Pinball radius: " & Joints.PinBallRadius * 0.001)
        Select Case Joints.PinBallRadiusUnit
            Case 0
                Debug.Print("  Pinball radius unit: mm")
            Case 1
                Debug.Print("  Pinball radius unit: cm")
            Case 2
                Debug.Print("  Pinball radius unit: m")
            Case 3
                Debug.Print("  Pinball radius unit: in")
            Case 4
                Debug.Print("  Pinball radius unit: ft")
            Case 5
                Debug.Print("  Pinball radius unit: ft-in")
            Case 6
                Debug.Print("  Pinball radius unit: am")
            Case 7
                Debug.Print("  Pinball radius unit: nm")
            Case 8
                Debug.Print("  Pinball radius unit: micron")
            Case 9
                Debug.Print("  Pinball radius unit: mil")
            Case 10
                Debug.Print("  Pinball radius unit: MicroIn")
        End Select

        'Mesh the part
        Mesh = Study.Mesh
        If Mesh Is Nothing Then ErrorMsg(swApp, "No mesh object")
        Mesh.Quality = swsMeshQuality_e.swsMeshQualityHigh
        Mesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance)
        errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance)
        If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")
        Debug.Print(" ")
        Debug.Print("Mesh...")
        Debug.Print("  Time to create mesh (hh:mm:ss): " & Mesh.TimeToCompleteMesh)
        Select Case Mesh.MeshType
            Case 0
                Debug.Print("  Mesh type: solid")
            Case 1
                Debug.Print("  Mesh type: midsurface")
            Case 2
                Debug.Print("  Mesh type: surface")
            Case 3
                Debug.Print("  Mesh type: mixed")
            Case 4
                Debug.Print("  Mesh type: beam")
        End Select
        Debug.Print("  Number of mesh controls: " & Mesh.MeshControlCount)
        Select Case Mesh.MeshState
            Case 0
                Debug.Print("  Mesh state: no mesh")
            Case 1
                Debug.Print("  Mesh state: exists and is current")
            Case 2
                Debug.Print("  Mesh state: exists and is not current")
            Case 3
                Debug.Print("  Mesh state: failed")
            Case 4
                Debug.Print("  Mesh state: interrupted")
        End Select
    End Sub
    Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
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
