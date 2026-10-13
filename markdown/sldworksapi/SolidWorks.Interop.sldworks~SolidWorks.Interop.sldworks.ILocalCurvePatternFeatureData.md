---
title: "ILocalCurvePatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html"
---

# ILocalCurvePatternFeatureData Interface

Allows access to a curve-driven component pattern feature in an assembly.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILocalCurvePatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
```

### C#

```csharp
public interface ILocalCurvePatternFeatureData
```

### C++/CLI

```cpp
public interface class ILocalCurvePatternFeatureData
```

## VBA Syntax

See [LocalCurvePatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), you must pre-select the entities needed to create the curve-driven component pattern feature.

| To select ... | Use Mark=... |
| --- | --- |
| Components to pattern | 1 |
| Curve, edge, sketch, or sketch entity for Direction 1 | 2 |
| Curve, edge, sketch, or sketch entity for Direction 2 | 4 |
| Reference point (only needed if ILocalCurvePatternFeatureData::D1ReferencePoint is set to swLocalCurvePatternReferencePoint_e .swLocalCurvePatternSelectedPoint) | 32 |
| Face normal (face on which a 3D curve lies) | 64 |

After calling IFeatureManager::CreateDefinition, you can explicitly set other properties on the feature data object.

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the curve-driven component pattern feature.

For more information, see the **Assemblies > Basic Component Operations > Component Patterns > Curve Driven Component Pattern** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

IFeatureManager::CreateDefinition

## Access Diagram

[LocalCurvePatternFeatureData](SWObjectModel.pdf#LocalCurvePatternFeatureData)

## See Also

[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
