---
title: "ICWCable Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html"
---

# ICWCable Interface

Allows access to a cable connector.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWCable
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
```

### C#

```csharp
public interface ICWCable
```

### C++/CLI

```cpp
public interface class ICWCable
```

## VBA Syntax

See [CWCable](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable.html).

## Examples

'VBA

'This example demonstrates how to create a cable connector.

'===========================================================

'Preconditions:

'1. Open an assembly with three parts that you will connect with two cables.

'2. Create a static study that has requisite loads and fixtures and uses the Intel Direct Sparse Solver.

'3. Modify SelectByRay parameters in the code below to select edges/faces on each set of two parts to connect.

'4. Ensure the material library exists.

'5. Open an Immediate window.

'

'Postconditions:

'1. Gets the study.

'2. Creates two cable connectors (both with diameter 0.02 m, safe axial strength 2400 N/m^2, and Alloy Steel)

' between the two sets of parts selected in step 3 of the preconditions.

'3. Meshes the study.

'4. Runs the analysis.

'5. Gets the results.

'6. Gets connector results/force.

'7. Compares connector forces.
'==============================================================

Option Explicit

Sub main()

Dim SwApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim COSMOSWORKSObj As CosmosWorksLib.COSMOSWORKS

Dim CWAddinCallBackObj As CosmosWorksLib.CWAddinCallBack

Dim StudyObj As CosmosWorksLib.CWStudy

Dim CWCable As CosmostWorksLib.CWCable

Dim CWCable2 As CosmostWorksLib.CWCable

Dim CWMesh As CosmosWorksLib.CWMesh

Dim CWResult As CosmosWorksLib.CWResults

Dim boolstatus As Boolean

Dim errCode As Long

Dim longstatus As Long, longwarnings As Long

Dim myModelView As SldWorks.ModelView

Dim ActiveDocObj As CosmosWorksLib.CWModelDoc

Dim StudyManagerObj As CosmosWorksLib.CWStudyManager

Dim LoadsAndRestraintsManagerObj As CosmosWorksLib.CWLoadsAndRestraintsManager

Dim el As Double, tl As Double, Tol1 As Double, Connector_Force1 As Double, Connector_Force2 As Double

Dim strMaterialLib As String

Set SwApp = Application.SldWorks

Set Part = SwApp.**ActiveDoc**

'Addin Callback

Set CWAddinCallBackObj = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")

If CWAddinCallBackObj Is Nothing Then ErrorMsg2 SwApp, "CWAddinCallBackObj object not found", True

Set COSMOSWORKSObj = CWAddinCallBackObj.COSMOSWORKS

If COSMOSWORKSObj Is Nothing Then ErrorMsg2 SwApp, "COSMOSWORKSObj object not found", True

'Set material Library

strMaterialLib = "e:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat"

Set myModelView = Part.ActiveView

myModelView.FrameLeft = 0

myModelView.FrameTop = 0

Set myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

Set myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

'Get active document

Set ActiveDocObj = COSMOSWORKSObj.ActiveDoc()

If ActiveDocObj Is Nothing Then ErrorMsg2 SwApp, "No Active Document", True

'Activate the study

Set StudyManagerObj = ActiveDocObj.StudyManager()

If StudyManagerObj Is Nothing Then ErrorMsg2 SwApp, "StudyManagerObj object not there", True

StudyManagerObj.ActiveStudy = 0

Set StudyObj = StudyManagerObj.GetStudy(0)

If StudyObj Is Nothing Then ErrorMsg2 SwApp, "Study not created", True

' Select the first pair of items to connect by cable; select faces only for solid bodies; select edges for shells

boolstatus = Part.Extension.**SelectByRay**(0.921920271769864, 1.16713776277859, 1.33177419666754, -0.34176252876859, -0.236529471640091, 0.909534047177652, 8.42662241140337E-04, 2, True, 0, 0)

boolstatus = Part.Extension.**SelectByRay**(0.645679844298542, 0.837284425334389, 1.33287586529872, -0.34176252876859, -0.236529471640091, 0.909534047177652, 6.82790794058472E-04, 2, True, 0, 0)

' Redraw

Part.GraphicsRedraw2

Dim StudyObj As Object

Set StudyObj = StudyManagerObj.GetStudy(0)

Set LoadsAndRestraintsManagerObj = StudyObj.**LoadsAndRestraintsManager**()

Dim DispatchObj1 As Object

Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)

Dim DispatchObj2 As Object

Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)

Dim DispArray As Variant

DispArray = Array(DispatchObj1)

Dim DispArray2 As Variant

DispArray2 = Array(DispatchObj2)

Set CWCable = LoadsAndRestraintsManagerObj.**AddCable**((DispArray), (DispArray2), 0, errCode)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 creation failed", True

Set CWCable = LoadsAndRestraintsManagerObj.**GetCable**("Cable-2", errCode)

CWCable.**BeginEdit**

errCode = CWCable.**SetFlipOffsetDirAtEnd1**(0)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 SetFlipOffsetDirAtEnd1 failed", True

errCode = CWCable.**SetOffsetAtEnd1**(0.01)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 SetOffsetAtEnd1 failed", True

errCode = CWCable.**SetFlipOffsetDirAtEnd2**(0)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 SetFlipOffsetDirAtEnd2 failed", True

errCode = CWCable.**SetOffsetAtEnd2**(0.01)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 SetOffsetAtEnd2 failed", True

errCode = CWCable.**SetCableParams**(0.02, 2400, 0#)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 SetCableParams failed", True

CWCable.**MaterialSource** = 1

CWCable.**SetLibraryMaterial** strMaterialLib, "Alloy Steel"

errCode = CWCable.**EndEdit**()

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-2 EndEdit failed", True

' Select the second pair of items to connect by cable; select faces only for solid bodies; select edges for shells

boolstatus = Part.Extension.**SelectByRay**(0.373018956619831, 1.17464121526402, 1.33263008238066, -0.34176252876859, -0.236529471640091, 0.909534047177652, 9.80012553162479E-04, 2, True, 0, 0)

boolstatus = Part.Extension.**SelectByRay**(0.644518640365447, 0.841241138500749, 1.33311291616565, -0.34176252876859, -0.236529471640091, 0.909534047177652, 1.69346169186476E-03, 2, True, 0, 0)

Part.GraphicsRedraw2

Set StudyObj = StudyManagerObj.GetStudy(0)

Set LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

Set DispatchObj1 = Part.SelectionManager.GetSelectedObject6(1, -1)

Set DispatchObj2 = Part.SelectionManager.GetSelectedObject6(2, -1)

DispArray = Array(DispatchObj1)

DispArray2 = Array(DispatchObj2)

Set CWCable2 = LoadsAndRestraintsManagerObj.**AddCable**((DispArray), (DispArray2), 0, errCode)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 creation failed", True

Set CWCable2 = LoadsAndRestraintsManagerObj.**GetCable**("Cable-3", errCode)

CWCable2.BeginEdit

errCode = CWCable2.**SetFlipOffsetDirAtEnd1**(0)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 SetFlipOffsetDirAtEnd1 failed", True

errCode = CWCable2.**SetOffsetAtEnd1**(0.01)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 SetOffsetAtEnd1 failed", True

errCode = CWCable2.**SetFlipOffsetDirAtEnd2**(0)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 SetFlipOffsetDirAtEnd2 failed", True

errCode = CWCable2.**SetOffsetAtEnd2**(0.01)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 SetOffsetAtEnd2 failed", True

errCode = CWCable2.**SetCableParams**(0.02, 2400, 0#)

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 SetCableParams failed", True

CWCable2.**MaterialSource** = 1

CWCable2.**SetLibraryMaterial** strMaterialLib, "Alloy Steel"

errCode = CWCable2.**EndEdit**()

If errCode <> 0 Then ErrorMsg2 SwApp, "Cable-3 EndEdit failed", True

Part.ClearSelection2 True

'Mesh

Set CWMesh = StudyObj.**Mesh**

If CWMesh Is Nothing Then ErrorMsg2 SwApp, "No Mesh Object", False

CWMesh.Quality = 1

CWMesh.MesherType = 0 '2 'BCB

Call CWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)

errCode = StudyObj.CreateMesh(0, el, tl)

If errCode <> 0 Then ErrorMsg2 SwApp, "Mesh failed", True

'Run Analysis

errCode = StudyObj.**RunAnalysis**

If errCode <> 0 Then ErrorMsg2 SwApp, "Analysis failed", True

Part.GraphicsRedraw2

'Get results

Set CWResult = StudyObj.**Results**

If CWResult Is Nothing Then ErrorMsg2 SwApp, "No Result Object", False

'Get connector results/Force

Dim Force1, Force2 As Variant

Force1 = CWResult.**GetConnectorForces2**(1, "Cable-2", 0, errCode)

Force2 = CWResult.**GetConnectorForces2**(1, "Cable-3", 0, errCode)

Connector_Force1 = 1380 'Expected axial force (comp = 7)

Connector_Force2 = 1390 'Expected axial force (comp = 7)

Tol1 = 0.1

Dim i As Integer

For i = 0 To 10

Debug.Print i & " : " & Force1(i)

SwApp.RecordLine "'******** Cable-2 Force " & i & " : " & Force1(i) & " ********"

Next i

If errCode <> 0 Then ErrorMsg2 SwApp, "No connector force", True

If ((Force1(7)) < 0.95 * Connector_Force1) Or ((Force1(7)) > 1.05 * Connector_Force1) Then

ErrorMsg2 SwApp, "O/p Force % error = " & (((Force1(7) - Connector_Force1) / Connector_Force1) * 100), False

End If

For i = 0 To 10

Debug.Print i & " : " & Force2(i)

SwApp.RecordLine "'******** Cable-3 Force " & i & " : " & Force2(i) & " ********"

Next i

If errCode <> 0 Then ErrorMsg2 SwApp, "No connector force", True

If ((Force2(7)) < 0.95 * Connector_Force2) Or ((Force2(7)) > 1.05 * Connector_Force2) Then

ErrorMsg2 SwApp, "O/p Force % error = " & (((Force2(7) - Connector_Force2) / Connector_Force2) * 100), False

End If

End Sub

Function ErrorMsg2(SwApp As Object, Message As String, EndTest As Boolean)

SwApp.SendMsgToUser2 Message, 0, 0

SwApp.RecordLine "'*** WARNING - General"

SwApp.RecordLine "'*** " & Message

SwApp.RecordLine ""

End Function

## Accessors

[ICWLoadAndRestraintsManager::AddCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddCable.html)

[ICWLoadAndRestraintsManager::GetCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetCable.html)

## See Also

[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
