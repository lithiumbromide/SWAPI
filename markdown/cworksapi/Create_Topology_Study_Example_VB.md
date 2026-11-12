---
title: "Create Topology Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Topology_Study_Example_VB.htm"
---

# Create Topology Study Example (VBA)

This example shows how to create a topology study, constraints, and manufacturing controls.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 '
 ' Postconditions:
 ' 1. Creates Coordinate System1.
 ' 2. Creates Topology Study 1.
 ' 3. Applies Plain Carbon Steel to the solid body.
 ' 4. Creates Fixed-1 fixture.
 ' 5. Creates Pressure-1 load.
 ' 6. Creates a Minimize Maximum Displacement goal.
 ' 7. Creates constraints:
 '       Mass Constraint1
 '       DisplacementConstraint1
 '       Stress Constraint1(replaced by Factor of Safety Constraint1)
 '       Frequency Constraint1(renamed to New Frequency Constraint)
 '       Displacement Constraint2
 ' 8. Creates manufacturing controls:
 '       Preserved Region1
 '       Thickness control1
 '       De-mold control1
 '       Symmetry control1
 ' 9. If an error occurs at any point, a dialog box appears.
 '    Close the dialog box. The macro ends.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
```

```vb
    Dim swApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2
     Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim CWTopoMinimizeMaximiumDisplacementGoalObj As CosmosWorksLib.CWTopologyMinimizeMaximumDisplacementGoal
     Dim ActiveDocObj As ICWModelDoc
     Dim StudyManagerObj As ICWStudyManager
     Dim LoadsAndRestraintsManagerObj As ICWLoadsAndRestraintsManager
     Dim ErrorCodeObj As Long
     Dim motionStudyMgr As Object
     Dim NewStudyName As String
     Dim CWNewStudy As ICWStudy
     Dim StudyObj As ICWStudy
     Dim CWTopologyStudyManagerObj As CosmosWorksLib.CWTopologyStudyManager
     Dim CWTopologyStudyOptionsObj As CosmosWorksLib.CWTopologyStudyOptions
     Dim CWTopoMassConstraintObj As CosmosWorksLib.CWTopologyMassConstraint
     Dim CWTopoDisplacementConstraintObj As CosmosWorksLib.CWTopologyDisplacementConstraint
     Dim CWTopoStressConstraintObj As CosmosWorksLib.CWTopologyStressConstraint
     Dim CWTopoFOSConstraintObj As CosmosWorksLib.CWTopologyFactorOfSafetyConstraint
     Dim CWTopoFreqConstraintObj As CosmosWorksLib.CWTopologyFrequencyConstraint
     Dim SolidManagerObj As CosmosWorksLib.CWSolidManager
     Dim DispArray As Variant
     Dim CWRestraintObj As CosmosWorksLib.CWRestraint
     Dim ReferenceGeometryDispatchObj As Object
     Dim CWPressure As CosmosWorksLib.CWPressure
     Dim NPropVal As Integer
     Dim sObjName As String
     Dim NPropDblVal As Double
     Dim DispArrayForPreservedRegion As Variant
     Dim sDispObjPlane As Object
     Dim sDispObjEdge As Object
     Dim sDispObjPlane1, sDispObjPlane2, sDispObjPlane3 As Object
     Dim boolstatus As Boolean
     Dim DispatchObj1, DispatchObj2 As Object
     Dim DispObj As Object
     Dim DispatchObjSelVertexForConstraint_Displacement_constraint_1 As Object
     Dim DispatchObjSelCoordSysForConstraint_Displacement_constraint_1 As Object
     Dim DispatchObjSelVertexForConstraint_Displacement_constraint_2 As Object
     Dim DispatchObjSelCoordSysForConstraint_Displacement_constraint_2 As Object
     Dim sMassConstraintName, sFreqConstraintName, sFreqConstraintNameForVerif As String
     Dim sDisplacementConstraintName, sFOSConstraintName, sStressConstraintName As String
     Dim sManufacControlName As String
    Dim varModeShapes, varComparators, varFrequencyValues As Variant
     Dim varModeShapesForVerif, varComparatorsForVerif, varFrequencyValuesForVerif As Variant
     Dim DispatchObjSelCoordSysForGoal_Minimize_Maximum_Displacement As Object
     Dim DispArrayForGoal_Minimize_Maximum_Displacement As Variant
     Dim CWTopoPreservedRegionObj As CosmosWorksLib.CWTopologyPreservedRegion
     Dim CWTopoThicknessControlObj As CosmosWorksLib.CWTopologyThicknessControl
     Dim CWTopoDemoldControlObj As CosmosWorksLib.CWTopologyDemoldControl
     Dim CWTopoSymmetryControlObj As CosmosWorksLib.CWTopologySymmetryControl

     Option Explicit

     Sub Main()

        Set swApp = Application.SldWorks
        If swApp Is Nothing Then Exit Sub

        Set Part = swApp.ActiveDoc

        ' Create Coordinate System1

        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0, 0, -0.025, 0, 0, -1, 9.1414694894147E-04, 3, False, 1, 0)
        boolstatus = Part.Extension.SelectByRay(3.38772104607721E-02, -6.72166874221669E-04, 0, 0, 0, -1, 9.1414694894147E-04, 1, True, 2, 0)
        boolstatus = Part.Extension.SelectByRay(-5.3773349937733E-04, 3.8985678704855E-03, -2.49999999999773E-02, 0, 0, -1, 9.1414694894147E-04, 1, True, 4, 0)
        boolstatus = Part.InsertCoordinateSystem(False, False, False)
        sMassConstraintName = "Mass Constraint 1"
        sDisplacementConstraintName = "Displacement Constraint 1"
        sFOSConstraintName = "Factor of Safety Constraint 1"
        sStressConstraintName = "Stress Constraint 1"
        sFreqConstraintName = "Frequency Constraint 1"
        sFreqConstraintNameForVerif = "New Frequency Constraint"

        Set CWAddinCallBack = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
        If CWAddinCallBack Is Nothing Then ErrorMsg swApp, "CWAddinCallBack object not found"
        Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
        If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "COSMOSWORKS object not found"

        Set ActiveDocObj = COSMOSWORKS.ActiveDoc()
        Set StudyManagerObj = ActiveDocObj.StudyManager()
        StudyManagerObj.ActiveStudy = 0

        Set motionStudyMgr = Part.Extension.GetMotionStudyManager()
        StudyManagerObj.ActiveStudy = 1

        ' Create Topology Study 1

        NewStudyName = "Topology Study 1"
        StudyManagerObj.DeleteStudy NewStudyName

        Set CWNewStudy = StudyManagerObj.CreateNewStudy3(NewStudyName, 13, 0, ErrorCodeObj)
        boolstatus = Part.Extension.SelectByID2("Split Line2", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        Set StudyObj = StudyManagerObj.GetStudy(1)
        Set SolidManagerObj = StudyObj.SolidManager()
        ErrorCodeObj = SolidManagerObj.SetFavLibraryMaterialToSelectedEntities("solidworks materials", "Plain Carbon Steel")
        Part.ClearSelection2 True
        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(3.05868083703444E-02, 5.02190380473166E-03, -4.57115266419237E-02, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.30969659309385E-03, 2, True, 0, 0)

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(9.60370122901963E-02, 5.75743614780322E-03, -4.61775206132984E-02, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.30969659309385E-03, 2, True, 0, 0)

        Part.GraphicsRedraw2
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        DispArray = Array(DispatchObj1, DispatchObj2)

        Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()
        Set CWRestraintObj = LoadsAndRestraintsManagerObj.AddRestraint(0, (DispArray), Nothing, ErrorCodeObj)
        Part.ClearSelection2 True
        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(0.14771358462832, 0.100969471635494, -3.10000000001196E-02, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.30969659309385E-03, 2, True, 0, 0)

        Part.GraphicsRedraw2
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        DispArray = Array(DispatchObj1)
        Set CWPressure = LoadsAndRestraintsManagerObj.AddPressure(0, (DispArray), ReferenceGeometryDispatchObj, ErrorCodeObj)
        CWPressure.PressureBeginEdit
        CWPressure.DirectionType = 0
        CWPressure.PressureType = 0
        CWPressure.Value = 1000
        CWPressure.Unit = 1
        CWPressure.ReverseDirection = False
        CWPressure.PressureEndEdit

        Part.ClearSelection2 True

        Part.GraphicsRedraw2

         Set CWTopologyStudyManagerObj = StudyObj.TopologyStudyManager
        Set CWTopologyStudyOptionsObj = StudyObj.TopologyStudyOptions
        CWTopologyStudyOptionsObj.SetConvergenceCheck 1

        ' Create topology minimize maximum displacement goal

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(0.025, 0.01, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.025, 0, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)

        CWTopologyStudyManagerObj.BeginEdit

        ErrorCodeObj = CWTopologyStudyManagerObj.CreateGoal(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create minimize maximum displacement goal.": GoTo LastLine
        Set CWTopoMinimizeMaximiumDisplacementGoalObj = CWTopologyStudyManagerObj.MinimizeMaximumDisplacementGoal()
        CWTopoMinimizeMaximiumDisplacementGoalObj.BeginEdit
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetComponent(3)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set component.": GoTo LastLine
        DispArrayForGoal_Minimize_Maximum_Displacement = Array(DispatchObj1, DispatchObj2)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetVertices((DispArrayForGoal_Minimize_Maximum_Displacement))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set vertices.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0.025, 0.01, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.025, 0, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)

        ' Edit minimize maximum displacement goal

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoMinimizeMaximiumDisplacementGoalObj = CWTopologyStudyManagerObj.MinimizeMaximumDisplacementGoal()
        CWTopoMinimizeMaximiumDisplacementGoalObj.BeginEdit
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetComponent(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set component.": GoTo LastLine
        DispArrayForGoal_Minimize_Maximum_Displacement = Array(DispatchObj1, DispatchObj2)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetVertices((DispArrayForGoal_Minimize_Maximum_Displacement))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set vertices.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetCoordinateSystemPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set coordinate system preference.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Edit mass constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoMassConstraintObj = CWTopologyStudyManagerObj.GetMassConstraint("Mass Constraint 1", ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get mass constraint.": GoTo LastLine
        CWTopoMassConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoMassConstraintObj.SetMassPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set mass preference.": GoTo LastLine
        ErrorCodeObj = CWTopoMassConstraintObj.SetValue(0.2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoMassConstraintObj.SetUnit(2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set unit.": GoTo LastLine
        ErrorCodeObj = CWTopoMassConstraintObj.EndEdit
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Create topology displacement constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.CreateDisplacementConstraint(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create displacement constraint.": GoTo LastLine
        sDisplacementConstraintName = CWTopoDisplacementConstraintObj.GetName

        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.GetDisplacementConstraint(sDisplacementConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get displacement constraint.": GoTo LastLine
        CWTopoDisplacementConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetName(sDisplacementConstraintName)
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComponent(3)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set component.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComparator(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set comparator.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValuationPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set valuation preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValue(1.2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetLocationPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set location preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Set coordinate system and vertexes for minimize maximum displacement goal

        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0.025, 0.01, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.025, 0, 0, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByRay(0.156, 0.054, -0.031, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.35592872061701E-04, 3, True, 0, 0)

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoMinimizeMaximiumDisplacementGoalObj = CWTopologyStudyManagerObj.MinimizeMaximumDisplacementGoal()
        CWTopoMinimizeMaximiumDisplacementGoalObj.BeginEdit
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        Set DispatchObjSelCoordSysForGoal_Minimize_Maximum_Displacement = Part.SelectionManager.GetSelectedObject6(3, -1)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetComponent(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set component.": GoTo LastLine
        DispArrayForGoal_Minimize_Maximum_Displacement = Array(DispatchObj1, DispatchObj2)
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetVertices((DispArrayForGoal_Minimize_Maximum_Displacement))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set vertices.": GoTo LastLine
        CWTopoMinimizeMaximiumDisplacementGoalObj.RemoveAllVertices
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetVertices((DispArrayForGoal_Minimize_Maximum_Displacement))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set vertices.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetCoordinateSystemPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set coordinate system preference.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetCoordinateSystem(DispatchObjSelCoordSysForGoal_Minimize_Maximum_Displacement)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set coordinate system.": GoTo LastLine
        CWTopoMinimizeMaximiumDisplacementGoalObj.RemoveCoordinateSys
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.SetCoordinateSystem(DispatchObjSelCoordSysForGoal_Minimize_Maximum_Displacement)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to set coordinate system.": GoTo LastLine
        ErrorCodeObj = CWTopoMinimizeMaximiumDisplacementGoalObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Minimize maximum displacement goal: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Edit mass constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoMassConstraintObj = CWTopologyStudyManagerObj.GetMassConstraint(sMassConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get mass constraint.": GoTo LastLine
        CWTopoMassConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoMassConstraintObj.SetMassPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set mass preference.": GoTo LastLine
        ErrorCodeObj = CWTopoMassConstraintObj.SetValue(200)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoMassConstraintObj.SetUnit(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to set unit.": GoTo LastLine
        sObjName = CWTopoMassConstraintObj.GetName()
        ErrorCodeObj = CWTopoMassConstraintObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Mass constraint: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Edit displacement constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.GetDisplacementConstraint(sDisplacementConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get displacement constraint.": GoTo LastLine
        CWTopoDisplacementConstraintObj.BeginEdit
        Set DispatchObjSelVertexForConstraint_Displacement_constraint_1 = Part.SelectionManager.GetSelectedObject6(4, -1)
        DispArray = Array(DispatchObjSelVertexForConstraint_Displacement_constraint_1)
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComponent(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set component.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComparator(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set comparator.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValuationPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set valuation preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValue(5)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetUnit(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set unit.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetLocationPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set location preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetVertices((DispArray))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set vertex.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystemPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set coordinate system preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0.025, 0.01, 0, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.24206498779656E-03, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.025, 0, 0, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.24206498779656E-03, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByRay(0.156, 0.054, -0.031, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.24206498779656E-03, 3, True, 0, 0)

        ' Edit displacement constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.GetDisplacementConstraint(sDisplacementConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get displacement constraint.": GoTo LastLine
        CWTopoDisplacementConstraintObj.BeginEdit
        Set DispatchObjSelVertexForConstraint_Displacement_constraint_1 = Part.SelectionManager.GetSelectedObject6(2, -1)
        DispArray = Array(DispatchObjSelVertexForConstraint_Displacement_constraint_1)
        Set DispatchObjSelCoordSysForConstraint_Displacement_constraint_1 = Part.SelectionManager.GetSelectedObject6(3, -1)
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComponent(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set component.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComparator(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set comparator.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValuationPreference(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set valuation preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValue(0.005)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetUnit(2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set unit.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetLocationPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set location preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetVertices((DispArray))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set vertex.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystemPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set coordinate system preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystem(DispatchObjSelCoordSysForConstraint_Displacement_constraint_1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set coordinate system.": GoTo LastLine
        CWTopoDisplacementConstraintObj.RemoveCoordinateSys
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystem(DispatchObjSelCoordSysForConstraint_Displacement_constraint_1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to set coordinate system.": GoTo LastLine
        sObjName = CWTopoDisplacementConstraintObj.GetName()
        ErrorCodeObj = CWTopoDisplacementConstraintObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Displacement constraint: Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Create topology stress constraint

        CWTopologyStudyManagerObj.BeginEdit

        Set CWTopoStressConstraintObj = CWTopologyStudyManagerObj.CreateStressConstraint(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create stress constraint.": GoTo LastLine
        sStressConstraintName = CWTopoStressConstraintObj.GetName

        Set CWTopoStressConstraintObj = CWTopologyStudyManagerObj.GetStressConstraint(sStressConstraintName, ErrorCodeObj)
        CWTopoStressConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoStressConstraintObj.SetName(sStressConstraintName)
        ErrorCodeObj = CWTopoStressConstraintObj.SetComponent(0)
        ErrorCodeObj = CWTopoStressConstraintObj.SetComparator(0)
        ErrorCodeObj = CWTopoStressConstraintObj.SetValuationPreference(1)
        ErrorCodeObj = CWTopoStressConstraintObj.SetValue(20)
        ErrorCodeObj = CWTopoStressConstraintObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        sObjName = CWTopoStressConstraintObj.GetName()
        If sObjName <> sStressConstraintName Then ErrorMsg swApp, "Stress constraint: Failed to get name.": GoTo LastLine

        ' Edit stress constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoStressConstraintObj = CWTopologyStudyManagerObj.GetStressConstraint(sStressConstraintName, ErrorCodeObj)
        CWTopoStressConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoStressConstraintObj.SetComponent(0)
        ErrorCodeObj = CWTopoStressConstraintObj.SetComparator(0)
        ErrorCodeObj = CWTopoStressConstraintObj.SetValuationPreference(0)
        ErrorCodeObj = CWTopoStressConstraintObj.SetValue(6200)
        ErrorCodeObj = CWTopoStressConstraintObj.SetUnit(1)
        sObjName = CWTopoStressConstraintObj.GetName()
        If sObjName <> sStressConstraintName Then ErrorMsg swApp, "Stress constraint: Failed to get name.": GoTo LastLine
        ErrorCodeObj = CWTopoStressConstraintObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Check whether Factor Of Safety constraint exists

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoFOSConstraintObj = CWTopologyStudyManagerObj.GetFactorOfSafetyConstraint(sFOSConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 9 Then ErrorMsg swApp, "Failed: Factor Of Safety constraint exists.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Replace topology stress constraint with Factor Of Safety constraint

        CWTopologyStudyManagerObj.BeginEdit
        ErrorCodeObj = CWTopologyStudyManagerObj.RemoveConstraint("Stress Constraint 1")
        Set CWTopoFOSConstraintObj = CWTopologyStudyManagerObj.CreateFactorOfSafetyConstraint(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create Factor Of Safety constraint.": GoTo LastLine
        sFOSConstraintName = CWTopoFOSConstraintObj.GetName

        Set CWTopoFOSConstraintObj = CWTopologyStudyManagerObj.GetFactorOfSafetyConstraint(sFOSConstraintName, ErrorCodeObj)
        CWTopoFOSConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoFOSConstraintObj.SetName(sFOSConstraintName)
        ErrorCodeObj = CWTopoFOSConstraintObj.SetComponent(0)
        ErrorCodeObj = CWTopoFOSConstraintObj.SetComparator(1)
        ErrorCodeObj = CWTopoFOSConstraintObj.SetValue(4)
        sObjName = CWTopoFOSConstraintObj.GetName()
        If sObjName <> sFOSConstraintName Then ErrorMsg swApp, "Factor of Safety constraint: Failed to get name.": GoTo LastLine
        ErrorCodeObj = CWTopoFOSConstraintObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Check whether stress constraint still exists

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoStressConstraintObj = CWTopologyStudyManagerObj.GetStressConstraint(sStressConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 9 Then ErrorMsg swApp, "Failed: Stress constraint was not replaced with Factor Of Safety constraint.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2

        ' Create topology frequency constraint

        varModeShapes = Array(2, 4, 5)
        varComparators = Array(1, 1, 2)
        varFrequencyValues = Array("100", "200", "201 - 205")
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoFreqConstraintObj = CWTopologyStudyManagerObj.CreateFrequencyConstraint(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create frequency constraint.": GoTo LastLine
        sFreqConstraintName = CWTopoFreqConstraintObj.GetName

        Set CWTopoFreqConstraintObj = CWTopologyStudyManagerObj.GetFrequencyConstraint(sFreqConstraintName, ErrorCodeObj)
        CWTopoFreqConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoFreqConstraintObj.SetName(sFreqConstraintName)
        CWTopoFreqConstraintObj.SetModeTrackingFlag2 0
        ErrorCodeObj = CWTopoFreqConstraintObj.SetFrequencyData((varModeShapes), (varComparators), (varFrequencyValues))
        CWTopoFreqConstraintObj.ClearFrequencyData
        ErrorCodeObj = CWTopoFreqConstraintObj.SetFrequencyData((varModeShapes), (varComparators), (varFrequencyValues))
        CWTopoFreqConstraintObj.SetName sFreqConstraintNameForVerif
        sObjName = CWTopoFreqConstraintObj.GetName()
        If sObjName <> sFreqConstraintNameForVerif Then ErrorMsg swApp, "Frequency constraint: Failed to get name.": GoTo LastLine
        ErrorCodeObj = CWTopoFreqConstraintObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.ClearSelection2 True
        Part.GraphicsRedraw2

        boolstatus = Part.Extension.SelectByRay(0.135, 0.01, 0, -0.499999999999997, -0.707106781186554, -0.499999999999995, 1.19476403492439E-03, 3, True, 0, 0)
        boolstatus = Part.Extension.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 0, Nothing, 0)
        Set DispatchObjSelVertexForConstraint_Displacement_constraint_2 = Part.SelectionManager.GetSelectedObject6(1, -1)
        DispArray = Array(DispatchObjSelVertexForConstraint_Displacement_constraint_2)
        Set DispatchObjSelCoordSysForConstraint_Displacement_constraint_2 = Part.SelectionManager.GetSelectedObject6(2, -1)

        ' Create second topology displacement constraint

        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.CreateDisplacementConstraint(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create displacement constraint.": GoTo LastLine
        sDisplacementConstraintName = CWTopoDisplacementConstraintObj.GetName

        Set CWTopoDisplacementConstraintObj = CWTopologyStudyManagerObj.GetDisplacementConstraint(sDisplacementConstraintName, ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to get displacement constraint.": GoTo LastLine
        CWTopoDisplacementConstraintObj.BeginEdit
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComponent(5)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set component.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetComparator(0)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set comparator.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValuationPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set valuation preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetValue(1.2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set value.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetLocationPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set location preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetVertices((DispArray))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set vertex.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystemPreference(1)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set coordinate system preference.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.SetCoordinateSystem(DispatchObjSelCoordSysForConstraint_Displacement_constraint_2)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to set coordinate system.": GoTo LastLine
        ErrorCodeObj = CWTopoDisplacementConstraintObj.EndEdit()
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to end edit.": GoTo LastLine
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Create topology preserved region

        Part.ClearSelection2 True
        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(0.152000000000072, 2.36311904768058E-02, -4.88232552103796E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 2, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.155833684385215, 2.27465262312307E-02, -3.90000000001578E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 2, True, 0, 0)
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoPreservedRegionObj = CWTopologyStudyManagerObj.CreatePreservedRegionControl(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create preserved region control.": GoTo LastLine
        CWTopoPreservedRegionObj.BeginEdit
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        DispArrayForPreservedRegion = Array(DispatchObj1, DispatchObj2)
        ErrorCodeObj = CWTopoPreservedRegionObj.SelectFaces((DispArrayForPreservedRegion))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed: CWTopoPreservedRegionObj faces could not be selected": GoTo LastLine
        CWTopoPreservedRegionObj.SetIncludeRegionDepth2 True
        CWTopoPreservedRegionObj.SetAreaDepth 1
        CWTopoPreservedRegionObj.SetAreaDepthUnit 0
        ErrorCodeObj = CWTopoPreservedRegionObj.EndEdit()

        sManufacControlName = CWTopoPreservedRegionObj.GetName
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Edit preserved region control area depth and units

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(0.152000000000072, 2.36311904768058E-02, -4.88232552103796E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 2, True, 0, 0)
        boolstatus = Part.Extension.SelectByRay(0.155833684385215, 2.27465262312307E-02, -3.90000000001578E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 2, True, 0, 0)
        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoPreservedRegionObj = CWTopologyStudyManagerObj.GetPreservedRegionControl(sManufacControlName, ErrorCodeObj)
        CWTopoPreservedRegionObj.BeginEdit
        Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        DispArrayForPreservedRegion = Array(DispatchObj1, DispatchObj2)
        ErrorCodeObj = CWTopoPreservedRegionObj.SelectFaces((DispArrayForPreservedRegion))
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed: CWTopoPreservedRegionObj faces could not be selected": GoTo LastLine
        CWTopoPreservedRegionObj.SetName (sManufacControlName)
        CWTopoPreservedRegionObj.SetIncludeRegionDepth2 True
        CWTopoPreservedRegionObj.SetAreaDepth 0.002
        CWTopoPreservedRegionObj.SetAreaDepthUnit 2
        ErrorCodeObj = CWTopoPreservedRegionObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Create topology thickness control

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoThicknessControlObj = CWTopologyStudyManagerObj.CreateThicknessControl(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create thickness control.": GoTo LastLine
        CWTopoThicknessControlObj.BeginEdit
        CWTopoThicknessControlObj.SetIncludeMinMemberThickness True
        CWTopoThicknessControlObj.SetMinimumMemberThickness 5.99766617291857
        CWTopoThicknessControlObj.SetMinimumMemberThicknessUnit 0
        CWTopoThicknessControlObj.SetIncludeMaxMemberThickness2 True
        CWTopoThicknessControlObj.SetMaxMemberThickness 10.710118165926
        CWTopoThicknessControlObj.SetMaxMemberThicknessUnit 0
        ErrorCodeObj = CWTopoThicknessControlObj.EndEdit()

        sManufacControlName = CWTopoThicknessControlObj.GetName
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2

        ' Edit thickness control to include maximum member thickness

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoThicknessControlObj = CWTopologyStudyManagerObj.GetThicknessControl(sManufacControlName, ErrorCodeObj)
        CWTopoThicknessControlObj.BeginEdit
        CWTopoThicknessControlObj.SetName sManufacControlName
        CWTopoThicknessControlObj.SetIncludeMinMemberThickness2 False
        CWTopoThicknessControlObj.SetIncludeMaxMemberThickness2 True
        CWTopoThicknessControlObj.SetMaxMemberThickness 1.5
        CWTopoThicknessControlObj.SetMaxMemberThicknessUnit 1
        ErrorCodeObj = CWTopoThicknessControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2

        ' Create topology de-mold control with a mid-plane direction

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByID2("Plane7", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDemoldControlObj = CWTopologyStudyManagerObj.CreateDemoldControl(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create De-mold control.": GoTo LastLine
        CWTopoDemoldControlObj.BeginEdit
        Set sDispObjPlane = Part.SelectionManager.GetSelectedObject6(1, -1)
        CWTopoDemoldControlObj.SelectDemoldDirection 0
        CWTopoDemoldControlObj.SetAutoDetermineCentralMidPlane2 False
        CWTopoDemoldControlObj.SelectPlaneForDirection sDispObjPlane
        ErrorCodeObj = CWTopoDemoldControlObj.EndEdit()

        sManufacControlName = CWTopoDemoldControlObj.GetName

        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()
        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Edit de-mold control to automatically determine central mid plane direction

        Part.GraphicsRedraw2
        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByID2("Plane7", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

        Part.GraphicsRedraw2
        boolstatus = Part.DeSelectByID("Plane7", "PLANE", 0, 0, 0)

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByRay(0.155546878794837, 9.87797571485771E-03, -3.89175812866256E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 1, True, 0, 0)

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDemoldControlObj = CWTopologyStudyManagerObj.GetDemoldControl(sManufacControlName, ErrorCodeObj)
        CWTopoDemoldControlObj.BeginEdit
        Set sDispObjEdge = Part.SelectionManager.GetSelectedObject6(1, -1)
        CWTopoDemoldControlObj.SetName sManufacControlName
        CWTopoDemoldControlObj.SelectDemoldDirection 0
        CWTopoDemoldControlObj.SetAutoDetermineCentralMidPlane2 True
        CWTopoDemoldControlObj.SelectEdgeForPullDirection sDispObjEdge
        ErrorCodeObj = CWTopoDemoldControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Edit de-mold control to be pulling

        Part.GraphicsRedraw2
        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0.155546878794837, 9.87797571485771E-03, -3.89175812866256E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 1, True, 0, 0)

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDemoldControlObj = CWTopologyStudyManagerObj.GetDemoldControl(sManufacControlName, ErrorCodeObj)
        CWTopoDemoldControlObj.BeginEdit
        Set sDispObjEdge = Part.SelectionManager.GetSelectedObject6(1, -1)
        CWTopoDemoldControlObj.SelectDemoldDirection 1
        CWTopoDemoldControlObj.SelectEdgeForPullDirection sDispObjEdge
        CWTopoDemoldControlObj.SetReverseDirection2 False
        ErrorCodeObj = CWTopoDemoldControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Edit de-mold control to be stamping

        Part.GraphicsRedraw2
        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByRay(0.155546878794837, 9.87797571485771E-03, -3.89175812866256E-02, 0.389180293740867, -0.51558974627672, -0.763351761966972, 8.18084299275831E-04, 1, True, 0, 0)

        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoDemoldControlObj = CWTopologyStudyManagerObj.GetDemoldControl(sManufacControlName, ErrorCodeObj)
        CWTopoDemoldControlObj.BeginEdit
        Set sDispObjEdge = Part.SelectionManager.GetSelectedObject6(1, -1)
        CWTopoDemoldControlObj.SelectDemoldDirection 2
        CWTopoDemoldControlObj.SelectEdgeForPullDirection sDispObjEdge
        CWTopoDemoldControlObj.SetReverseDirection2 True
        ErrorCodeObj = CWTopoDemoldControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.GraphicsRedraw2
        Part.ClearSelection2 True

        ' Define topology one-half symmetry control

        Part.GraphicsRedraw2
        boolstatus = Part.Extension.SelectByID2("Plane7", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoSymmetryControlObj = CWTopologyStudyManagerObj.CreateSymmetryControl(ErrorCodeObj)
        If ErrorCodeObj <> 0 Then ErrorMsg swApp, "Failed to create symmetry control.": GoTo LastLine
        CWTopoSymmetryControlObj.BeginEdit
        Set sDispObjPlane1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        CWTopoSymmetryControlObj.SelectSymmetryType 0
        CWTopoSymmetryControlObj.SelectFirstSymmetryPlane sDispObjPlane1
        ErrorCodeObj = CWTopoSymmetryControlObj.EndEdit()

        sManufacControlName = CWTopoSymmetryControlObj.GetName
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Define topology one-quarter symmetry control

        Part.GraphicsRedraw2
        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByID2("Plane7", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Plane5", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoSymmetryControlObj = CWTopologyStudyManagerObj.GetSymmetryControl("Symmetry control 1", ErrorCodeObj)
        CWTopoSymmetryControlObj.BeginEdit
        Set sDispObjPlane1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set sDispObjPlane2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        CWTopoSymmetryControlObj.SelectSymmetryType 1
        CWTopoSymmetryControlObj.SelectFirstSymmetryPlane sDispObjPlane1
        CWTopoSymmetryControlObj.SelectSecondSymmetryPlane sDispObjPlane2
        CWTopoSymmetryControlObj.SetName sManufacControlName
        ErrorCodeObj = CWTopoSymmetryControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        ' Define topology one-eighth symmetry control

        Part.GraphicsRedraw2
        Part.ClearSelection2 True
        boolstatus = Part.Extension.SelectByID2("Plane7", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Plane5", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Plane4", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        Part.GraphicsRedraw2
        CWTopologyStudyManagerObj.BeginEdit
        Set CWTopoSymmetryControlObj = CWTopologyStudyManagerObj.GetSymmetryControl(sManufacControlName, ErrorCodeObj)
        CWTopoSymmetryControlObj.BeginEdit
        Set sDispObjPlane1 = Part.SelectionManager.GetSelectedObject6(1, -1)
        Set sDispObjPlane2 = Part.SelectionManager.GetSelectedObject6(2, -1)
        Set sDispObjPlane3 = Part.SelectionManager.GetSelectedObject6(3, -1)
        CWTopoSymmetryControlObj.SelectSymmetryType 2
        CWTopoSymmetryControlObj.SelectFirstSymmetryPlane sDispObjPlane1
        CWTopoSymmetryControlObj.SelectSecondSymmetryPlane sDispObjPlane2
        CWTopoSymmetryControlObj.SelectThirdSymmetryPlane sDispObjPlane3
        ErrorCodeObj = CWTopoSymmetryControlObj.EndEdit()
        ErrorCodeObj = CWTopologyStudyManagerObj.EndEdit()

        Part.ClearSelection2 True
        Part.GraphicsRedraw2

LastLine:
     End Sub

Sub ErrorMsg(swApp As SldWorks.SldWorks, Message As String)
     swApp.SendMsgToUser2 Message, 0, 0
     swApp.RecordLine "'*** WARNING - General"
     swApp.RecordLine "'*** " & Message
     swApp.RecordLine ""
End Sub
```
