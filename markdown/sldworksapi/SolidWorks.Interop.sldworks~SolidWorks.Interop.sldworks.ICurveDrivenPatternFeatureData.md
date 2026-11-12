---
title: "ICurveDrivenPatternFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html"
---

# ICurveDrivenPatternFeatureData Interface

Allows access to a curve-driven pattern feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICurveDrivenPatternFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
```

### C#

```csharp
public interface ICurveDrivenPatternFeatureData
```

### C++/CLI

```cpp
public interface class ICurveDrivenPatternFeatureData
```

## VBA Syntax

See [CurveDrivenPatternFeatureData](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html), you must pre-select the entities needed to create the curve-driven pattern feature.

| To select ... | Use Mark=... |
| --- | --- |
| Features to pattern | 4 |
| Direction 1 entity (2D/3D curve, edge, sketch, or sketch entity) | 1 |
| Direction 2 entity (2D/3D curve, edge, sketch, or sketch entity) | 2 |
| Face normal (face on which the Direction 1 3D curve lies); needed only when ICurveDrivenPatternFeatureData::D1AlignmentMethod is set to swCurveDrivenPatternAlignment_e .swCurvePatternTangentToCurve and Direction 1 is a 3D curve entity | 1024 |

After calling IFeatureManager::CreateDefinition, you can explicitly set other properties on the feature data object.

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) after initializing this feature data object in order to successfully create the curve-driven pattern feature.

For more information about curve-driven pattern features, see the **Parts and Features > Features > Patterns and Mirroring > Types of Patterns > Curve Driven Patterns and the Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html)

IFeatureManager::CreateDefinition

## Access Diagram

[CurveDrivenPatternFeatureData](SWObjectModel.pdf#CurveDrivenPatternFeatureData)

## See Also

[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
