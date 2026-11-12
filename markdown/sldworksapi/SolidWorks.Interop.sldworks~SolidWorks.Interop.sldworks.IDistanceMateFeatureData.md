---
title: "IDistanceMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html"
---

# IDistanceMateFeatureData Interface

Allows access to a distance mate or a limit distance mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDistanceMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
```

### C#

```csharp
public interface IDistanceMateFeatureData
```

### C++/CLI

```cpp
public interface class IDistanceMateFeatureData
```

## VBA Syntax

See [DistanceMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData.html).

## Examples

[Create and Edit Limit Distance Mate (VBA)](Create_Limit_Distance_Mate_Example_VB.htm)
[Create and Edit Limit Distance Mate (C#)](Create_Limit_Distance_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

A distance mate places selected items at a specified distance. A limit distance mate is an advanced mate that allows components to move within a range of distances. Use [IDistanceMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.html) to determine whether this is a limit distance mate.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create either a distance mate or a limit distance mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IDistanceMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify other properties of the DistanceMateFeatureData object.

To edit a distance mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a DistanceMateFeatureData object.
3. Modify the DistanceMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a distance mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[DistanceMateFeatureData](SWObjectModel.pdf#DistanceMateFeatureData)

## See Also

[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
