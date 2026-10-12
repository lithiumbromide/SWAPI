---
title: "ICWLinkageRod Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html"
---

# ICWLinkageRod Interface

Allows access to a linkage rod connector. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWLinkageRod
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
```

### C#

```csharp
public interface ICWLinkageRod
```

### C++/CLI

```cpp
public interface class ICWLinkageRod
```

## VBA Syntax

See [CWLinkageRod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod.html).

## Examples

'VBA

'=====================================

'Preconditions:

1. Open `Public_Documents`**\SOLIDWORKS\SOLIDWORKS 2022\samples\Simulation Examples\mixedmesh-1.sldasm**.
2. In SOLIDWORKS, select **Tools > Add-ins > SOLIDWORKS Simulation**.
3. Ensure the specified material library exists.
4. Open an Immediate window.

'Postconditions:

'1. Creates a **Linkage rod-3**.
'2. Meshes the model.
'3. Runs an analysis.
'4. Gets the results.
'5. Gets the linkage rod connector forces.
'6. Inspect the Immediate window for linkage rod connector forces.

'==========================================

Dim SwApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim COSMOSWORKSObj As CosmosWorksLib.COSMOSWORKS
Dim CWAddinCallBackObj As CosmosWorksLib.CWAddinCallBack
Dim ActiveDocObj As CosmosWorksLib.CWModelDoc
Dim StudyManagerObj As CosmosWorksLib.CWStudyManager
Dim StudyObj As CosmosWorksLib.CWStudy
Dim Study As CosmosWorksLib.CWStudy
Dim LoadsAndRestraintsManagerObj As CosmosWorksLib.CWLoadsAndRestraintsManager
Dim cwLinkageRod As CosmosWorksLib.cwLinkageRod
Dim CWMesh As CosmosWorksLib.CWMesh
Dim CWResult As CosmosWorksLib.CWResults
Dim errCode As Long
Dim strMaterialLib As String
Dim el As Double
Dim tl As Double
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

Set SwApp = Application.SldWorks
Set Part = SwApp.**ActiveDoc**

Set CWAddinCallBackObj = SwApp.**GetAddInObject**("CosmosWorks.CosmosWorks")
If CWAddinCallBackObj Is Nothing Then ErrorMsg2 SwApp, "CWAddinCallBackObj object not found", True
Set COSMOSWORKSObj = CWAddinCallBackObj.COSMOSWORKS
If COSMOSWORKSObj Is Nothing Then ErrorMsg2 SwApp, "COSMOSWORKSObj object not found", True

'Set material Library
strMaterialLib = SwApp.**GetExecutablePath** & "\lang\english\sldmaterials\solidworks materials.sldmat"

'Get active document
Set ActiveDocObj = COSMOSWORKSObj.**ActiveDoc**()
If ActiveDocObj Is Nothing Then ErrorMsg2 SwApp, "No Active Document", True 'Get the study

'Activate the study
Set StudyManagerObj = ActiveDocObj.**StudyManager**()
If StudyManagerObj Is Nothing Then ErrorMsg2 SwApp, "StudyManagerObj object not there", True

StudyManagerObj.**ActiveStudy** = 0
Set Study = StudyManagerObj.**GetStudy**(0)
If Study Is Nothing Then ErrorMsg2 SwApp, "Study not created", True

'Select vertexes for End 1 and 2 of the linkage rod connector
boolstatus = Part.Extension.SelectByRay(-0.231298527539886, 0.166575928167274, 0.458852915453974, -0.577381545199981, -0.577287712085548, -0.577381545199979, 3.6575436673129E-03, 3, True, 0, 0)
boolstatus = Part.Extension.SelectByRay(4.88947738114092E-02, 0.414776469003414, 0.458852915453974, -0.577381545199981, -0.577287712085548, -0.577381545199979, 3.6575436673129E-03, 3, True, 0, 0)

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

Set cwLinkageRod = LoadsAndRestraintsManagerObj.**AddLinkageRod**((DispArray), (DispArray2), 0, errCode)
If errCode <> 0 Then ErrorMsg2 SwApp, "Linkage Rod creation failed", True

Set cwLinkageRod = LoadsAndRestraintsManagerObj.**GetLinkageRod**("Linkage rod-3", errCode)

'Start editing the linkage rod
cwLinkageRod.**BeginEdit**

'Set the joint type of End 1 and End 2
cwLinkageRod.**SetJointTypeAtEnd1** 0
cwLinkageRod.**SetJointTypeAtEnd2** 0

'Set the hollow circular cross-section parameters
Dim SectionParamsArray As Variant
SectionParamsArray = Array(0.005, 0.0005)
cwLinkageRod.**SetSectionParams** 1, (SectionParamsArray)

'Set the material
cwLinkageRod.**MaterialSource** = 1
cwLinkageRod.**SetLibraryMaterial** strMaterialLib, "Alloy Steel"
cwLinkageRod.**IncludeMass** = False

'Stop editing
errCode = cwLinkageRod.**EndEdit**()
If errCode <> 0 Then ErrorMsg2 SwApp, "Linkage rod connector failed editing", True

Part.ClearSelection2 True

'Mesh
Set CWMesh = StudyObj.**Mesh**
If CWMesh Is Nothing Then ErrorMsg2 SwApp, "No mesh object", False
CWMesh.**Quality** = 1
CWMesh.**MesherType** = 0
Call CWMesh.**GetDefaultElementSizeAndTolerance**(0, el, tl)
errCode = StudyObj.**CreateMesh**(0, el, tl)
If errCode <> 0 Then ErrorMsg2 SwApp, "Mesh failed", True

'Run analysis
errCode = StudyObj.**RunAnalysis**
If errCode <> 0 Then ErrorMsg2 SwApp, "Analysis failed", True

Part.GraphicsRedraw2

'Get results
Set CWResult = StudyObj.**Results**
If CWResult Is Nothing Then ErrorMsg2 SwApp, "No results", False

'Get linkage rod connector forces
Dim Forc As Variant
Forc = CWResult.**GetConnectorForces2**(1, "Linkage rod-3", 0, errCode)

Dim i As Integer
For i = 0 To 10
Debug.Print i & " : " & Forc(i)
Next i

If errCode <> 0 Then ErrorMsg2 SwApp, "No connector forces", True

End Sub

Function ErrorMsg2(SwApp As Object, Message As String, EndTest As Boolean)
SwApp.SendMsgToUser2 Message, 0, 0
SwApp.RecordLine "'*** WARNING - General"
SwApp.RecordLine "'*** " & Message
SwApp.RecordLine ""
'If EndTest Then
'End
'End If
End Function

## Remarks

This interface is only available with SOLIDWORKS Simulation Professional and Premium licenses.

For more information about linkage rod connectors, see the **SOLIDWORKS user-interface help > Simulation > Loads and Restraints > Connectors** topics.

## Accessors

[ICWLoadsAndRestraintsManager::AddLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddLinkageRod.html)

[ICWLoadsAndRestraintsManager::GetLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLinkageRod.html)

## See Also

[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
