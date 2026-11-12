---
title: "ICamFollowerMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ICamFollowerMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.html"
---

# ICamFollowerMateFeatureData Interface

Allows access to a cam-follower mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICamFollowerMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ICamFollowerMateFeatureData
```

### C#

```csharp
public interface ICamFollowerMateFeatureData
```

### C++/CLI

```cpp
public interface class ICamFollowerMateFeatureData
```

## VBA Syntax

See [CamFollowerMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~CamFollowerMateFeatureData.html).

## Examples

'VBA

'******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\Cam-Follower.sldasm**.
' 2. Delete **CamMateCoincident1** from the Mates folder in the FeatureManager design tree.
' 3. Run the macro.
' 4. Inspect the Mates folder in the FeatureManager design tree.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean

Option Explicit

Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByRay(-2.29201081452857E-03, 7.61655216381314E-02, 9.81125242168446E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 2.88013169157359E-03, 2, True, 1, 0)
boolstatus = Part.Extension.SelectByRay(0, 0.0762, 0, -0.577381545199981, -0.577287712085548, -0.577381545199979, 2.88013169157359E-03, 3, True, 8, 0)

' Create CamFollowerMateFeatureData
Dim MateData As SldWorks.CamFollowerMateFeatureData
Set MateData = Part.**CreateMateData**(9)

' Set the Entities To Mate
Dim FirstEntityToMate As Object
Dim SecondEntityToMate As Object
Set FirstEntityToMate = Part.SelectionManager.GetSelectedObject6(1, -1)
MateData.**EntitiesToMate**(0) = FirstEntityToMate
Set SecondEntityToMate = Part.SelectionManager.GetSelectedObject6(2, -1)
MateData.**EntitiesToMate**(1) = SecondEntityToMate

' Set the Mate Alignment
MateData.MateAlignment = 2

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Examples

[Create a Cam-Follower Mate (C#)](Create_Cam_Follower_Mate_Example_CSharp.htm)

## Remarks

A cam-follower mate:

- Allows you to mate a cylinder, plane, or point on a cam-follower part to the tangent faces of a cam part.
- Appears in the FeatureManager design tree as either CamMateCoincident or CamMateTangent.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a cam-follower mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ICamFollowerMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData~EntitiesToMate.html) for each EntityType or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1 for the cam face and Mark = 8 for the cam-follower face or vertex.
3. Specify other properties of the CamFollowerMateFeatureData object.

To edit a cam-follower mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a CamFollowerMateFeatureData object.
3. Modify the CamFollowerMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this cam-follower mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[CamFollowerMateFeatureData](SWObjectModel.pdf#CamFollowerMateFeatureData)

## See Also

[ICamFollowerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
