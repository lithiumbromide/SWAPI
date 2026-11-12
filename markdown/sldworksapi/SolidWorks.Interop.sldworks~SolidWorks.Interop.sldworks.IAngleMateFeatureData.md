---
title: "IAngleMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html"
---

# IAngleMateFeatureData Interface

Allows access to an angle mate or a limit angle mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAngleMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
```

### C#

```csharp
public interface IAngleMateFeatureData
```

### C++/CLI

```cpp
public interface class IAngleMateFeatureData
```

## VBA Syntax

See [AngleMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData.html).

## Examples

[Create and Edit Limit Angle Mate (VBA)](Create_Limit_Angle_Mate_Example_VB.htm)
[Create and Edit Limit Angle Mate (C#)](Create_Limit_Angle_Mate_Example_CSharp.htm)

## Remarks

An angle mate places selected items at a specified angle. A limit angle mate is an advanced mate that allows items to move within a range of angles. Use [IAngleMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate.html) to determine whether this is a limit angle mate.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create either an angle mate or a limit angle mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IAngleMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify [IAngleMateFeatureData::ReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~ReferenceEntity.html) or use IModelDocExtension::SelectByID2 to pre-select the reference entity using Mark = 67108864.
4. Specify other properties of the AngleMateFeatureData object.

To edit an angle mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to an AngleMateFeatureData object.
3. Modify the AngleMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this angle mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[AngleMateFeatureData](SWObjectModel.pdf#AngleMateFeatureData)

## See Also

[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
