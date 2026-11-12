---
title: "ICircularPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html"
---

# ICircularPatternFeatureData Interface

Allows access to a circular pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICircularPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
```

### C#

```csharp
public interface ICircularPatternFeatureData
```

### C++/CLI

```cpp
public interface class ICircularPatternFeatureData
```

## VBA Syntax

See [CircularPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData.html).

## Examples

[Get Transform for Each Circular Pattern Instance (C#)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm)
[Get Transform for Each Circular Pattern Instance (VB.NET)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm)
[Get Transform for Each Circular Pattern Instance (VBA)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm)
[Create Bidirectional Circular Pattern Feature (C#)](Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm)
[Create Bidirectional Circular Pattern Feature (VB.NET)](Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm)
[Create Bidirectional Circular Pattern Feature (VBA)](Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the circular pattern feature.

| If... | Use... |
| --- | --- |
| Using IModelDocExtension::SelectByID2 to select entities | 1 to mark the direction axis 4 to mark the features to pattern 256 to mark the bodies to pattern 134217728 to mark the structure systems to pattern |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the circular pattern feature.

After creating the circular pattern feature, you can:

- [vary the spacing of pattern instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.html) and dimensions by implementing [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html).

- [change the structure system to pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~StructureSystemToPatternArray.html).

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[CircularPatternFeatureData](SWObjectModel.pdf#CircularPatternFeatureData)

## See Also

[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
