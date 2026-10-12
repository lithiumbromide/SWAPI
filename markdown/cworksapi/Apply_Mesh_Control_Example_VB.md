---
title: "Apply Mesh Control Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Mesh_Control_Example_VB.htm"
---

# Apply Mesh Control Example (VBA)

This example shows how to get and set beams and joints, create a mesh, and apply a mesh control.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).
' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Ensure that the specified part and material library exist.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Creates a static study named frame.
' 2. Gets beam information.
' 3. Applies Plain Carbon Steel material to all beams.
' 4. Calculates joints for all beams, gets a neutral axis for each beam,
'    and gets the pinball tolerance value and unit.
' 5. Sets the mesher type to alternate curvature based.
' 6. Applies a mesh control and gets its values.
' 7. Creates a mixed mesh and gets its type and state.
'    NOTE: This can take several seconds to complete.
' 8. Inspect the Immediate window.
'
' NOTES:
' *  Beam elements are created by default for parts with structural members.
' *  Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

```vb
Option Explicit

Sub main()
    Dim SwApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
    Dim COSMOSObject As CosmosWorksLib.CwAddincallback
    Dim ActDoc As CosmosWorksLib.CWModelDoc
    Dim StudyMngr As CosmosWorksLib.CWStudyManager
    Dim Study As CosmosWorksLib.CWStudy
    Dim BeamMgr As CosmosWorksLib.CWBeamManager
    Dim BeamBody As CosmosWorksLib.CWBeamBody
    Dim Joints As CosmosWorksLib.CWJoints
    Dim Mesh As CosmosWorksLib.CWMesh
    Dim MeshControl As CosmosWorksLib.CWMeshControl
    Dim nbrBeamBodies As Long
    Dim beamBodyType As Long
    Dim ElementSize As Double
    Dim Tolerance As Double
    Dim errors As Long, warnings As Long
    Dim errCode As Long
    Dim j As Integer
    Dim bApp As Boolean
    Dim keepJointUpdates As Boolean
    Dim status As Boolean
    Dim selEntity As Object
    Dim selEntities(7) As Object

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
     Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"

    Set swModel = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     Set Study = StudyMngr.CreateNewStudy3("frame", swsAnalysisStudyTypeStatic, 0, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Study not created"

    Set BeamMgr = Study.BeamManager
     nbrBeamBodies = BeamMgr.BeamCount
     Debug.Print "Beams..."
     Debug.Print "  Number of beams: " & nbrBeamBodies
     Set BeamBody = Nothing
     For j = 0 To (nbrBeamBodies - 1)
         Set BeamBody = BeamMgr.GetBeamBodyAt(j, errCode)
         If errCode <> 0 Then ErrorMsg SwApp, "No beam body"
         Debug.Print "    Name of beam body: " & BeamBody.BeamBodyName
         beamBodyType = BeamBody.BeamType
         If beamBodyType = 0 Then
             Debug.Print "      Type of beam body: beam"
         Else
             Debug.Print "      Type of beam body: truss"
         End If
         bApp = BeamBody.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Plain Carbon Steel")
         If bApp = False Then ErrorMsg SwApp, "No material applied"
         Set BeamBody = Nothing
     Next j

    ' Calculate joints
     Set Joints = BeamMgr.GetJointGroup(errCode)
     Debug.Print " "
     Debug.Print "Joints..."
     If errCode <> 0 Then ErrorMsg SwApp, "No joint group"
     Joints.JointsBeginEdit
     Joints.IncludeAllSelectedBeam = True
     Joints.IncludeDisplayNeutralAxis = True
     Joints.CalculateJoints
     Joints.JointsEndEdit
     keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate
     If (keepJointUpdates = True) Then
         Debug.Print ("  Keep joint updates? yes")
     Else
         Debug.Print ("  Keep joint updates? no")
     End If
     Debug.Print "  Overwrite the pinball value: " & Joints.IncludeTreatAsJointForClearanceLessThan
     Debug.Print "  Pinball radius: " & Joints.PinBallRadius * 0.001
     Select Case Joints.PinBallRadiusUnit
         Case 0
             Debug.Print "  Pinball radius unit: mm"
         Case 1
             Debug.Print "  Pinball radius unit: cm"
         Case 2
             Debug.Print "  Pinball radius unit: m"
         Case 3
             Debug.Print "  Pinball radius unit: in"
         Case 4
             Debug.Print "  Pinball radius unit: ft"
         Case 5
             Debug.Print "  Pinball radius unit: ft-in"
         Case 6
             Debug.Print "  Pinball radius unit: am"
         Case 7
             Debug.Print "  Pinball radius unit: nm"
         Case 8
             Debug.Print "  Pinball radius unit: micron"
         Case 9
             Debug.Print "  Pinball radius unit: mil"
         Case 10
             Debug.Print "  Pinball radius unit: micronIn"
     End Select

     Set Mesh = Study.Mesh
     If Mesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
     Mesh.Quality = swsMeshQualityHigh
     Mesh.MesherType = swsMesherTypeAlternateCB
     Mesh.GetDefaultElementSizeAndTolerance swsLinearUnitMillimeters, ElementSize, Tolerance

    ' Select structural members for mesh control
     Debug.Print ""
     Debug.Print ("Mesh control...")

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[4]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(0) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[3]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(1) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[2]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(2) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[1]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(3) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[8]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(4) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[6]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(5) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Sb beam 80 X 6(1)[2]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(6) = selEntity
     Set selEntity = Nothing

    status = swModelDocExt.SelectByID2("Sb beam 80 X 6(1)[1]", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
     Set selEntity = swSelMgr.GetSelectedObject6(1, -1)
     Set selEntities(7) = selEntity
     Set selEntity = Nothing

    Set MeshControl = Mesh.ApplyMeshControl(selEntities, errCode)
     MeshControl.MeshControlBeginEdit
     MeshControl.BeamSelected2 = 0
     MeshControl.MinimumElementSize_BlendedCurved = 4
     MeshControl.MinNumOfElementsPerCircle_BlendedCurved = 8
     MeshControl.MeshControlEndEdit
     Debug.Print "  Name of mesh control: " & MeshControl.Name
     Debug.Print "  Beam selected? (True = yes; False = no) " & MeshControl.BeamSelected2
     Debug.Print "  Element size for mesh control (m): " & MeshControl.ElementSize
     Debug.Print "  Number of entities in mesh control: " & MeshControl.EntityCount
     Debug.Print "  Number of elements for beams: " & MeshControl.NumofElementsforBeams
     Debug.Print "  Ratio of the average element size (layer i)/(layer i-1): " & MeshControl.Ratio
     Debug.Print "  State of mesh control (0 = suppressed; 1 = not suppressed): " & MeshControl.State
     Debug.Print "  Minimum element size for boundaries with highest curvature: " & MeshControl.MinimumElementSizeForBlendedCurveMesher
     Debug.Print "  Minimum number of elements in a circle to determine the maximum angle: " & MeshControl.MinNumOfElementsPerCircleForBlendedCurveMesher

    Debug.Print "  Number of mesh controls: " & Mesh.MeshControlCount

    errCode = Study.CreateMeshForMeshControl(MeshControl.Name)

    ' Mesh the part
     Debug.Print " "
     Debug.Print "*** Creating a mesh next, which can take several seconds. Please wait. ***"
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, ElementSize, Tolerance)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

    Debug.Print " "
     Debug.Print "Mesh..."
     Debug.Print "  Time to create (hh:mm:ss): " & Mesh.TimeToCompleteMesh
     Debug.Print "  Type: "
     Select Case Mesh.MeshType
         Case 0
             Debug.Print "    Solid"
         Case 1
             Debug.Print "    Midsurface"
         Case 2
             Debug.Print "    Surface"
         Case 3
             Debug.Print "    Mixed"
         Case 4
             Debug.Print "    Beam"
     End Select

    Debug.Print "  State: "
     Select Case Mesh.MeshState
         Case 0
             Debug.Print "    No mesh"
         Case 1
             Debug.Print "    Exists and is current"
         Case 2
             Debug.Print "    Exists and is not current"
         Case 3
             Debug.Print "    Failed"
         Case 4
             Debug.Print "    Interrupted"
     End Select

End Sub
 Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
