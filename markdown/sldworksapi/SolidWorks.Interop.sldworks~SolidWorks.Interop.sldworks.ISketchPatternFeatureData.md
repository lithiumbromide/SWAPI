---
title: "ISketchPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html"
---

# ISketchPatternFeatureData Interface

Allows access to a sketch-driven pattern feature in a part.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISketchPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
```

### C#

```csharp
public interface ISketchPatternFeatureData
```

### C++/CLI

```cpp
public interface class ISketchPatternFeatureData
```

## VBA Syntax

See [SketchPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData.html).

## Examples

[Get Properties of Sketch Pattern Feature (VBA)](Get_Properties_of_Sketch-Pattern_Feature_Example_VB.htm)
[Get Properties of Sketch Pattern Feature (VB.NET)](Get_Properties_of_Sketch-Pattern_Feature_Example_VBNET.htm)
[Get Properties of Sketch Pattern Feature (C#)](Get_Properties_of_Sketch-Pattern_Feature_Example_CSharp.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities needed to create the circular pattern feature.

To select the required entities, use these selection Marks:

- features = 4
- points = 32
- sketches = 64
- faces = 128
- bodies = 256

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create a sketch-driven pattern.

For more information, see the **Sketch Driven Patterns** topic in the SOLIDWORKS Help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[SketchPatternFeatureData](SWObjectModel.pdf#SketchPatternFeatureData)

## See Also

[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
