---
title: "ICWBearingConnector Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html"
---

# ICWBearingConnector Interface

Allows access to a bearing connector. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWBearingConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector
```

### C#

```csharp
public interface ICWBearingConnector
```

### C++/CLI

```cpp
public interface class ICWBearingConnector
```

## VBA Syntax

See [CWBearingConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector.html).

## Examples

'VBA

'This example demonstrates how to create a bearing connector for a shaft and its housing. Contact API Support to obtain the assembly and components that work with this example.

'====================================================

'Preconditions:

'1. Obtain the relevant assembly and components from API Support and open the assembly in SOLIDWORKS.

'2. Load the SOLIDWORKS Simulation add-in.

'3. Add the SOLIDWORKS Simulation type library as a reference.

'4. (Optional) Uncomment code to compare connector forces.

'5. Open an Immediate window.

'

'Postconditions:

'1. Activates and gets the **Static 5_Rigid** study.

'2. Creates a bearing connector.

'3. Meshes the model.

'4. Analyzes the study.

'5. Gets the analysis results.

'6. Gets the connector results and forces.

'7. (Optional) Compares connector forces.

'8. Inspect the Immediate window and the Simulation study tree.

'======================================================

Dim SwApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim swAssembly As SldWorks.AssemblyDoc

Dim myModelView As SldWorks.ModelView

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

Dim COSMOSWORKSObj As CosmosWorksLib.COSMOSWORKS

Dim CWAddinCallBackObj As CosmosWorksLib.CWAddinCallBack

Dim ActiveDocObj As CosmosWorksLib.CWModelDoc

Dim StudyManagerObj As CosmosWorksLib.CWStudyManager

Dim CWMesh As CosmosWorksLib.CWMesh

Dim CWResult As CosmosWorksLib.CWResults

Dim LoadsAndRestraintsManagerObj As CosmosWorksLib.CWLoadsAndRestraintsManager

Dim errCode As Long

Dim motionStudyMgr As Object

Dim el As Double, tl As Double, Tol1 As Double, Connector_Force As Double

Set SwApp = Application.SldWorks

'Set Part = SwApp.OpenDoc6("QAA_01_Cylindrical Bearing.SLDASM", swDocASSEMBLY, 192, "", longstatus, longwarnings)

'If Part Is Nothing Then ErrorMsg2 SwApp, "Failed to open:QAA_01_Cylindrical Bearing.SLDASM", True

'Set swAssembly = Part

'SwApp.ActivateDoc2 "QAA_01_Cylindrical Bearing.SLDASM", False, longstatus

Set Part = SwApp.ActiveDoc

Set CWAddinCallBackObj = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")

If CWAddinCallBackObj Is Nothing Then ErrorMsg2 SwApp, "CWAddinCallBackObj object not found", True

Set COSMOSWORKSObj = CWAddinCallBackObj.COSMOSWORKS

If COSMOSWORKSObj Is Nothing Then ErrorMsg2 SwApp, "COSMOSWORKSObj object not found", True

Set myModelView = Part.ActiveView

myModelView.FrameLeft = 0

myModelView.FrameTop = 0

Set myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

Set myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

Set motionStudyMgr = Part.Extension.GetMotionStudyManager()

Set ActiveDocObj = COSMOSWORKSObj.ActiveDoc()

If ActiveDocObj Is Nothing Then ErrorMsg2 SwApp, "No Active Document", True 'Get the study

Set StudyManagerObj = ActiveDocObj.StudyManager()

If StudyManagerObj Is Nothing Then ErrorMsg2 SwApp, "StudyManagerObj object not there", True

StudyManagerObj.ActiveStudy = 1

Dim StudyObj As Object

Set StudyObj = StudyManagerObj.GetStudy(1)

If StudyObj Is Nothing Then ErrorMsg2 SwApp, "Study not created", True

Part.GraphicsRedraw2

Part.ViewZoomTo2 5.39264773386334E-02, 1.94101535368661E-02, 0.159999999986677, 9.33821942296391E-02, -2.38032506770925E-02, 0.159999999986677

Part.GraphicsRedraw2

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(-4.30154869025614E-02, -2.3147631828806E-03, 8.69723354912821E-03, -0.851450358677067, -0.352944394561843, -0.387895012930133, 1.63979435633325E-04, 2, True, 0, 0)

Part.GraphicsRedraw2

Part.GraphicsRedraw2

Part.GraphicsRedraw2

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(-4.45748406675648E-02, -9.87194045754336E-03, 4.85229755915384E-03, -0.851450358677067, -0.352944394561843, -0.387895012930133, 1.63979435633325E-04, 2, True, 0, 0)

Part.GraphicsRedraw2

Part.GraphicsRedraw2

Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

Dim DispatchShaftObj As Object

Set DispatchShaftObj = Part.SelectionManager.GetSelectedObject6(1, -1)

Dim DispatchHousingObj As Object

Set DispatchHousingObj = Part.SelectionManager.GetSelectedObject6(2, -1)

Dim CWBearingConnector As ICWBearingConnector

Set CWBearingConnector = LoadsAndRestraintsManagerObj.**AddBearingConnector**(DispatchShaftObj, DispatchHousingObj, errCode)

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector creation failed", True

If CWBearingConnector Is Nothing Then ErrorMsg2 SwApp, "Bearing connector creation failed", True

errCode = CWBearingConnector.**PerformAdvanceValidations**

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector PerformAdvanceValidations failed", True

Set CWBearingConnector = LoadsAndRestraintsManagerObj.**GetBearingConnector**("Bearing Connector-2", errCode)

If CWBearingConnector Is Nothing Then ErrorMsg2 SwApp, "GetBearingConnector failed", True

CWBearingConnector.**BeginEdit**

CWBearingConnector.**ConnectionType** = swsSpringConnType

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector ConnectionType failed", True

CWBearingConnector.**UnitType** = swsUnitSI

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector UnitType failed", True

CWBearingConnector.**StiffnessType** = swsBearingStiffnessRigid

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector StiffnessType failed", True

CWBearingConnector.**AxialStiffnessValue** = 0

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector AxialStiffnessValue failed", True

CWBearingConnector.**LateralStiffnessValue** = 0

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector LateralStiffnessValue failed", True

CWBearingConnector.**TiltStiffnessValue** = 0

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector TiltStiffnessValue failed", True

CWBearingConnector.**StabilizeShaftRotation** = False

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector StabilizeShaftRotation failed", True

errCode = CWBearingConnector.**EndEdit**()

If errCode <> 0 Then ErrorMsg2 SwApp, "Bearing connector EndEdit failed", True

Part.ClearSelection2 True

Set CWMesh = StudyObj.Mesh

If CWMesh Is Nothing Then ErrorMsg2 SwApp, "No Mesh Object", False

CWMesh.Quality = 1

CWMesh.MesherType = 0 '2 'BCB

Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)

errCode = StudyObj.CreateMesh(0, el, tl)

If errCode <> 0 Then ErrorMsg2 SwApp, "Mesh failed", True

errCode = StudyObj.RunAnalysis

If errCode <> 0 Then ErrorMsg2 SwApp, "Analysis failed", True

Part.GraphicsRedraw2

Set CWResult = StudyObj.Results

If CWResult Is Nothing Then ErrorMsg2 SwApp, "No Result Object", False

'Get Connector results/Force

'Dim Forc As Variant

'Forc = CWResult.GetConnectorForces2(1, "Bearing connector-2", 0, errCode)

'Connector_Force = -528.28 'Expected axial force (comp = 7)

'Tol1 = 0.1

'Dim i As Integer

'For i = 0 To 10

' Debug.Print i & " : " & Forc(i)

' SwApp.RecordLine "'******** Bearing connector Force " & i & " : " & Forc(i) & " ********"

'Next i

'If errCode <> 0 Then ErrorMsg2 SwApp, "No connector force", True

'Connector force comparision.

'If ((Forc(7)) = nan) Then

'ErrorMsg2 SwApp, "Forc(7) is not calculated ", False

'End If

'If ((Forc(7)) < 0.95 * Connector_Force) Or ((Forc(7)) > 1.05 * Connector_Force) Then

'ErrorMsg2 SwApp, "O/p Force % error = " & (((Forc(7) - Connector_Force) / Connector_Force) * 100), False

'End If

End Sub

Function ErrorMsg2(SwApp As Object, Message As String, EndTest As Boolean)

SwApp.SendMsgToUser2 Message, 0, 0

SwApp.RecordLine "'*** WARNING - General"

SwApp.RecordLine "'*** " & Message

SwApp.RecordLine ""

'If EndTest Then

'SwApp.ExitApp

'End

'End If

End Function

## Examples

[Add Bearing Connector (VB.NET)](Add_Bearing_Connector_Example_VBNET.htm)
[Add Bearing Connector (C#)](Add_Bearing_Connector_Example_CSharp.htm)

## Remarks

For more information about bearing connectors, see the **SOLIDWORKS user-interface help > Simulation > Loads and Restraints > Connectors > Bearing Connectors Between Parts** topics.

## Accessors

[ICWLoadsAndRestraintsManager::AddBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddBearingConnector.html)

[ICWLoadsAndRestraintsManager::GetBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetBearingConnector.html)

## See Also

[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
