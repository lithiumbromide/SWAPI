---
title: "ILocalSketchPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html"
---

# ILocalSketchPatternFeatureData Interface

Allows access to a sketch-driven component pattern feature in an assembly.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILocalSketchPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
```

### C#

```csharp
public interface ILocalSketchPatternFeatureData
```

### C++/CLI

```cpp
public interface class ILocalSketchPatternFeatureData
```

## VBA Syntax

See [LocalSketchPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData.html).

## Examples

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the sketch-driven component pattern feature.

| To select ... | Use a mark of... |
| --- | --- |
| Components to pattern | 1 |
| Sketch to define the pattern | 16 |
| Reference point as defined in swLocalSketchPatternReferencePoint_e | 32 |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the local sketch-driven pattern feature.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[LocalSketchPatternFeatureData](SWObjectModel.pdf#LocalSketchPatternFeatureData)

## See Also

[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
