---
title: "IProjectionCurveFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html"
---

# IProjectionCurveFeatureData Interface

Allows access to a projection curve feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IProjectionCurveFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
```

### C#

```csharp
public interface IProjectionCurveFeatureData
```

### C++/CLI

```cpp
public interface class IProjectionCurveFeatureData
```

## VBA Syntax

See [ProjectionCurveFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData.html).

## Examples

[Get Projected Curve (VBA)](Get_Projected_Curve_Example_VB.htm)

## Remarks

To create a projection curve feature:

1. Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the necessary entities using the following Marks:

  - target faces on which to project a sketch = 1
  - sketch to project = 2
  - target sketch on which to project a sketch = 4
  - projection direction entity = 8
2. Call IFeatureManager::CreateDefinition(swFmRefCurve) to access this interface.
3. Set non-entity properties on this interface.
4. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create the projection curve feature.

See the SOLIDWORKS Help for more information about projection curve features.

## Accessors

[IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) and [IFeature::IGetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetDefinition.html)

[IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

## Access Diagram

[ProjectionCurveFeatureData](SWObjectModel.pdf#ProjectionCurveFeatureData)

## See Also

[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
