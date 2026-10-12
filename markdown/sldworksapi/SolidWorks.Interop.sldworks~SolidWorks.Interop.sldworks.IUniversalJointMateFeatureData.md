---
title: "IUniversalJointMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IUniversalJointMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html"
---

# IUniversalJointMateFeatureData Interface

Allows access to a universal joint mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IUniversalJointMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IUniversalJointMateFeatureData
```

### C#

```csharp
public interface IUniversalJointMateFeatureData
```

### C++/CLI

```cpp
public interface class IUniversalJointMateFeatureData
```

## VBA Syntax

See [UniversalJointMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~UniversalJointMateFeatureData.html).

## Examples

'VBA
' ******************************************************************************
' 1. Open `public_documents`**\samples\tutorial\api\MechanicalMates\Universal Joint.sldasm**.
' 2. Run the macro.
' 3. Inspect the Mates folder of the FeatureManager design tree.
' ******************************************************************************
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Option Explicit

Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

boolstatus = Part.Extension.SelectByRay(1.88633351534122E-02, 2.88569103901466E-02, 5.46569039595397E-02, -0.879159305813743, -0.399683188478405, -0.259484611969252, 7.73012265648448E-04, 2, True, 1, 0)
boolstatus = Part.Extension.SelectByRay(1.86671108039604E-02, 7.47386637118552E-02, 4.19001939717987E-02, -0.879159305813743, -0.399683188478405, -0.259484611969252, 7.73012265648448E-04, 2, True, 1, 0)

' Create UniversalJointMateFeatureData
Dim MateData As SldWorks.UniversalJointMateFeatureData
Set MateData = Part.**CreateMateData**(19)

' Set the Entities To Mate
Dim EntitiesToMate(1) As Object
Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
Dim EntitiesToMateVar As Variant
EntitiesToMateVar = EntitiesToMate
MateData.**EntitiesToMate** = (EntitiesToMateVar)

' Set the Mate DefineJointPoint
MateData.**DefineJointPoint** = False

' Create the mate
Dim MateFeature As SldWorks.Feature
Set MateFeature = Part.**CreateMate**(MateData)
Part.ClearSelection2 True
Part.EditRebuild3

End Sub

## Remarks

A universal joint (U-joint) mate consists of two components where the rotation of one component (the output shaft) about its axis is driven by the rotation of another component (the input shaft) about its axis. An example would be the U-joint between the transmission and the rear drive axle of an automobile.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a universal joint mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IUniversalJointMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Set [IUniversalJointMateFeatureData::DefineJointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint.html) to true and specify [IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.html) or use IModelDocExtension::SelectByID2 to pre-select the joint point using Mark = 16384.
4. Specify other properties of the UniversalJointMateFeatureData object as required.

To edit a universal joint mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a UniversalJointMateFeatureData object.
3. Modify the UniversalJointMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this universal joint mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[UniversalJointMateFeatureData](SWObjectModel.pdf#UniversalJointMateFeatureData)

## See Also

[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
