---
title: "ISwDMDimXpertFeature Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFeature"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.html"
---

# ISwDMDimXpertFeature Interface

Allows you to access general information about DimXpert features and sub-features.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFeature
```

### C#

```csharp
public interface ISwDMDimXpertFeature
```

### C++/CLI

```cpp
public interface class ISwDMDimXpertFeature
```

## VBA Syntax

See [SwDMDimXpertFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertFeature.html).

## Examples

[Get DimXpert Sphere and Datum (VB.NET)](Get_DimXpert_Sphere_and_Datum_Example_VBNET.htm)
[Get DimXpert Sphere and Datum (C#)](Get_DimXpert_Sphere_and_Datum_Example_CSharp.htm)

## Remarks

This interface is the base class for several more specific DimXpert feature interfaces (see the **See Also** section). Use the [ISwDMDimXpertFeature::type](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature~type.html) property to find out which specific feature interface is needed to acquire more information for a given DimXpert feature.

## Accessors

[ISwDMDimXpertAngleBetweenDimTol::OriginFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol~OriginFeature.html)

[ISwDMDimXpertAnnotation::Feature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~Feature.html)

[ISwDMDimXpertBestFitPlaneFeature::GetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~GetSubFeatures.html) and [ISwDMDimXpertBestFitPlaneFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~IGetSubFeatures.html)

[ISwDMDimXpertCompositeDistanceBetweenDimTol::GetFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetFeature.html), [ISwDMDimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html), [ISwDMDimXpertCompositeDistanceBetweenDimTol::GetOriginFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetOriginFeature.html)

[ISwDMDimXpertCompoundClosedSlot3DFeature::GetBottomFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetBottomFeature.html) and [ISwDMDimXpertCompoundClosedSlot3DFeature::GetEndFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.html)

[ISwDMDimXpertCompoundHoleFeature::GetBottomFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetBottomFeature.html), [ISwDMDimXpertCompoundHoleFeature::GetReferenceFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetReferenceFeature.html), [ISwDMDimXpertCompoundHoleFeature::GetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatures.html), [ISwDMDimXpertCompoundHoleFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~IGetSubFeatures.html)

[ISwDMDimXpertCompoundNotchFeature::GetBottomFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetBottomFeature.html), [ISwDMDimXpertCompoundNotchFeature::GetEndFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetEndFeature.html), [ISwDMDimXpertCompoundNotchFeature::GetOpenSideReferenceFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetOpenSideReferenceFeature.html), [ISwDMDimXpertCompoundNotchFeature::GetTopReferenceFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetTopReferenceFeature.html)

[ISwDMDimXpertCounterBoreDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol~ReferenceFeature.html)

[ISwDMDimXpertCounterSinkAngleDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol~ReferenceFeature.html)

[ISwDMDimXpertCounterSinkDiameterDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkDiameterDimTol~ReferenceFeature.html)

[ISwDMDimXpertDepthDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol~ReferenceFeature.html)

[ISwDMDimXpertDistanceBetweenDimTol::GetFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetFeature.html) and [ISwDMDimXpertDistanceBetweenDimTol::GetOriginFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetOriginFeature.html)

[ISwDMDimXpertExtrudeFeature::GetBottomBlends](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetBottomBlends.html), [ISwDMDimXpertExtrudeFeature::GetTopBlends](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetTopBlends.html), [ISwDMDimXpertExtrudeFeature::GetBottomFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetBottomFeature.html), [ISwDMDimXpertExtrudeFeature::GetReferenceFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetReferenceFeature.html), [ISwDMDimXpertExtrudeFeature::GetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatures.html), [ISwDMDimXpertExtrudeFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~IGetSubFeatures.html)

[ISwDMDimXpertIntersectCircleFeature::GetIntersectFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetIntersectFeature.html) and [ISwDMDimXpertIntersectCircleFeature::GetPlaneFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetPlaneFeature.html)

[ISwDMDimXpertIntersectLineFeature::GetPlaneFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetPlaneFeatures.html)

[ISwDMDimXpertIntersectPlaneFeature::GetFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature~GetFeatures.html)

[ISwDMDimXpertIntersectPointFeature::GetFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetFeatures.html)

[ISwDMDimXpertPart::GetFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatures.html) and [ISwDMDimXpertPart::IGetFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetFeatures.html)

[ISwDMDimXpertPatternFeature::GetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatures.html) and [ISwDMDimXpertPatternFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~IGetSubFeatures.html)

[ISwDMDimXpertTangencyTolerance::GetOriginFeature property](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol~GetOriginFeature.html)

SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetFeatures.html

## See Also

[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMDimXpertBestFitPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature.html)
[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.html)
[ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.html)
[ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.html)
[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.html)
[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.html)
[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.html)
[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.html)
[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.html)
[ISwDMDimXpertFilletFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.html)
[ISwDMDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature.html)
[ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.html)
[ISwDMDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature.html)
[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.html)
[ISwDMDimXpertPatternFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature.html)
[ISwDMDimXpertPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.html)
[ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.html)
[ISwDMDimXpertSurfaceFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSurfaceFeature.html)
