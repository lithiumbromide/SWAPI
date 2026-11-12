---
title: "Add Bearing Connector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Bearing_Connector_Example_CSharp.htm"
---

# Add Bearing Connector Example (C#)

This example shows how to add a bearing connector for a shaft and its housing.

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

// ====================================================

// Preconditions:

// 1. Contact SOLIDWORKS API Support to obtain the assembly and components that work with this macro.

// 2. Open **QAA_01_Cylindrical Bearing.sldasm** in SOLIDWORKS.

// 3. Load the Simulation add-in in SOLIDWORKS.

// 4. Add the SOLIDWORKS Simulation interop assembly as a reference to the .NET macro.

// 5 (Optional) Uncomment code to get connector forces.

// 6. Open an Immediate/Output window.

//

// Postconditions:

// 1. Activates and gets the **Static 5_Rigid** study.

// 2. Creates **Bearing Connector-2** and modifies its properties.

// 3. Meshes the model.

// 4. Analyzes the study.

// 5. Inspect the Immediate/Output window and the Simulation study tree.

// ======================================================

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows;

using System.Windows.Forms;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using SolidWorks.Interop.cosworks;

namespace AddBearingConnector_CSharp

{

public partial class SolidWorksMacro

{

private ModelDoc2 Part;

private ModelView myModelView;

private bool boolstatus;

private int longstatus;

private int longwarnings;

public void Main()

{

CosmosWorks COSMOSWORKSObj;

CwAddincallback CWAddinCallBackObj;

CWModelDoc ActiveDocObj;

CWStudyManager StudyManagerObj;

CWMesh CWMesh;

CWResults CWResult;

CWLoadsAndRestraintsManager LoadsAndRestraintsManagerObj;

int errCode;

double el;

double tl;

double Tol1;

double Connector_Force;

// Set Part = SwApp.OpenDoc6("QAA_01_Cylindrical Bearing.SLDASM", swDocASSEMBLY, 192, "", longstatus, longwarnings)

// If Part Is Nothing Then ErrorMsg2 SwApp, "Failed to open:QAA_01_Cylindrical Bearing.SLDASM", True

// SwApp.ActivateDoc2 "QAA_01_Cylindrical Bearing.SLDASM", False, longstatus

Part = (ModelDoc2)swApp.ActiveDoc;

CWAddinCallBackObj = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");

if (CWAddinCallBackObj == null)

ErrorMsg2(swApp, "CWAddinCallBackObj object not found", true);

COSMOSWORKSObj = CWAddinCallBackObj.CosmosWorks;

if (COSMOSWORKSObj == null)

ErrorMsg2(swApp, "COSMOSWORKSObj object not found", true);

myModelView = (ModelView)Part.ActiveView;

myModelView.FrameLeft = 0;

myModelView.FrameTop = 0;

myModelView.FrameState = (int)swWindowState_e.swWindowMaximized;

myModelView.FrameState = (int)swWindowState_e.swWindowMaximized;

ActiveDocObj = COSMOSWORKSObj.ActiveDoc;

if (ActiveDocObj == null)

ErrorMsg2(swApp, "No Active Document", true);

StudyManagerObj = ActiveDocObj.StudyManager;

if (StudyManagerObj == null)

ErrorMsg2(swApp, "StudyManagerObj object not there", true);

StudyManagerObj.ActiveStudy = 1;

CWStudy StudyObj;

StudyObj = StudyManagerObj.GetStudy(1);

if (StudyObj == null)

ErrorMsg2(swApp, "Study not created", true);

Part.GraphicsRedraw2();

Part.ViewZoomTo2(0.0539264773386334, 0.0194101535368661, 0.159999999986677, 0.0933821942296391, -0.0238032506770925, 0.159999999986677);

Part.GraphicsRedraw2();

Part.GraphicsRedraw2();

boolstatus = Part.Extension.SelectByRay(-0.0430154869025614, -0.0023147631828806, 0.00869723354912821, -0.851450358677067, -0.352944394561843, -0.387895012930133, 0.000163979435633325, 2, true, 0, 0);

Part.GraphicsRedraw2();

Part.GraphicsRedraw2();

Part.GraphicsRedraw2();

Part.GraphicsRedraw2();

boolstatus = Part.Extension.SelectByRay(-0.0445748406675648, -0.00987194045754336, 0.00485229755915384, -0.851450358677067, -0.352944394561843, -0.387895012930133, 0.000163979435633325, 2, true, 0, 0);

Part.GraphicsRedraw2();

Part.GraphicsRedraw2();

LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager;

object DispatchShaftObj;

SelectionMgr swSelMgr;

swSelMgr = (SelectionMgr)Part.SelectionManager;

DispatchShaftObj = swSelMgr.GetSelectedObject6(1, -1);

object DispatchHousingObj;

DispatchHousingObj = swSelMgr.GetSelectedObject6(2, -1);

ICWBearingConnector CWBearingConnector;

CWBearingConnector = LoadsAndRestraintsManagerObj.**AddBearingConnector**(DispatchShaftObj, DispatchHousingObj, out errCode);

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector creation failed", true);

if (CWBearingConnector == null)

ErrorMsg2(swApp, "Bearing connector creation failed", true);

errCode = CWBearingConnector.**PerformAdvanceValidations**();

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector PerformAdvanceValidations failed", true);

CWBearingConnector = LoadsAndRestraintsManagerObj.**GetBearingConnector**("Bearing Connector-6", out errCode);

if (CWBearingConnector == null)

ErrorMsg2(swApp, "GetBearingConnector failed", true);

CWBearingConnector.**BeginEdit**();

CWBearingConnector.**ConnectionType** = (int)swsBearingConnectionType_e.swsSpringConnType;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector ConnectionType failed", true);

CWBearingConnector.**UnitType** = (int)swsUnit_e.swsUnitSI;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector UnitType failed", true);

CWBearingConnector.**StiffnessType** = (int)swsBearingStiffnessType_e.swsBearingStiffnessRigid;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector StiffnessType failed", true);

CWBearingConnector.**AxialStiffnessValue** = 0;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector AxialStiffnessValue failed", true);

CWBearingConnector.**LateralStiffnessValue** = 0;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector LateralStiffnessValue failed", true);

CWBearingConnector.**TiltStiffnessValue** = 0;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector TiltStiffnessValue failed", true);

CWBearingConnector.**StabilizeShaftRotation** = false;

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector StabilizeShaftRotation failed", true);

errCode = CWBearingConnector.**EndEdit**();

if (errCode != 0)

ErrorMsg2(swApp, "Bearing connector EndEdit failed", true);

Part.ClearSelection2(true);

CWMesh = StudyObj.Mesh;

if (CWMesh == null)

ErrorMsg2(swApp, "No Mesh Object", false);

CWMesh.Quality = 1;

CWMesh.MesherType = 0;

CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);

errCode = StudyObj.CreateMesh(0, el, tl);

if (errCode != 0)

ErrorMsg2(swApp, "Mesh failed", true);

errCode = StudyObj.RunAnalysis();

if (errCode != 0)

ErrorMsg2(swApp, "Analysis failed", true);

Part.GraphicsRedraw2();

CWResult = StudyObj.Results;

if (CWResult == null)

ErrorMsg2(swApp, "No Result Object", false);

//Get Connector results

//Dim Forc As Variant;

//Forc = CWResult.GetConnectorForces2(1, "Bearing connector-2", 0, errCode);

//Connector_Force = -528.28; //Expected axial force(comp = 7)

//Tol1 = 0.1;

//Dim i As Integer;

//For i = 0 To 10

// Debug.Print (i + " : " + Forc(i));

// SwApp.RecordLine ("' * *******Bearing connector Force " + i + " : " + Forc(i) + " * *******");

//Next i

//If errCode <> 0 Then ErrorMsg2( SwApp, "No connector force", false);

//Connector force comparision

//If ((Forc(7)) = nan) Then

// ErrorMsg2 (SwApp, "Forc(7) is not calculated ", false);

//End If

//If ((Forc(7)) < 0.95 * Connector_Force) Or ((Forc(7)) > 1.05 * Connector_Force) Then

// ErrorMsg2 (SwApp, "O/p Force % error = " + (((Forc(7) - Connector_Force) / Connector_Force) * 100), false);

//End If

}

public void ErrorMsg2(SldWorks SwApp, string Message, bool EndTest)

{

SwApp.SendMsgToUser2(Message, 0, 0);

SwApp.RecordLine("'*** WARNING - General");

SwApp.RecordLine("'*** " + Message);

SwApp.RecordLine("");

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
