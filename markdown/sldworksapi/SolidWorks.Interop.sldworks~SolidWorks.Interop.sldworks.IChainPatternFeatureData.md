---
title: "IChainPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html"
---

# IChainPatternFeatureData Interface

Allows access to a chain component pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IChainPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
```

### C#

```csharp
public interface IChainPatternFeatureData
```

### C++/CLI

```cpp
public interface class IChainPatternFeatureData
```

## VBA Syntax

See [ChainPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData.html).

## Examples

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

## Remarks

This interface supports the following chain component patterns:

- distance
- distance linkage
- connected linkage

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to populate the chain component pattern.

| Entity to select | Corresponding Chain Pattern PropertyManager control | Selection mark | Number of selections |
| --- | --- | --- | --- |
| 2D or 3D sketch containing an open or closed loop, Sketch line , or Model edge | Path | 2 | 1 for all types of chain patterns |
| Assembly component | Chain Group 1 Component to Pattern | 1 | 1 for all types of chain patterns |
| Cylindrical face , Circular or linear edge, Sketch point , Vertex , or Reference axis | Chain Group 1 Path Link 1 | 256 | 1 for all types of chain patterns |
| Cylindrical face, Circular or linear edge, Sketch point, Vertex, or Reference axis | Chain Group 1 Path Link 2 | 512 | 1 for distance linkage or connected linkage None for distance |
| Component plane or planar face | Chain Group 1 Path Alignment Plane | 16384 | 1 for all types of chain patterns |
| Assembly component | Chain Group 2 Component to Pattern | 2048 | 1 for connected linkage None for distance or linkage distance |
| Cylindrical face, Circular or linear edge, Sketch point, Vertex, or Reference axis | Chain Group 2 Path Link 1 | 4096 | 1 for connected linkage None for distance or linkage distance |
| Cylindrical face, Circular or linear edge, Sketch point, Vertex, or Reference axis | Chain Group 2 Path Link 2 | 8192 | 1 for connected linkage None for distance or linkage distance |
| Component plane or planar face | Group 2 Path Alignment Plane | 32768 | 1 for connected linkage None for distance or linkage distance |
| Assembly plane | Face normal alignment | 1024 | 1 if the chain path is a sketch line None for all other types of paths |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the chain component pattern feature.

## Accessors

[IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[ChainPatternFeatureData](SWObjectModel.pdf#ChainPatternFeatureData)

## See Also

[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
