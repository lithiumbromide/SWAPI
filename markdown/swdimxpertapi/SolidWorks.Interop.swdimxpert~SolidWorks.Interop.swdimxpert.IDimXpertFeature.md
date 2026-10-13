---
title: "IDimXpertFeature Interface"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: ""
kind: "interface"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html"
---

# IDimXpertFeature Interface

Allows you to access DimXpert features and sub-features on the DimXpertManager tab of the Management Panel.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
```

### C#

```csharp
public interface IDimXpertFeature
```

### C++/CLI

```cpp
public interface class IDimXpertFeature
```

## VBA Syntax

See [DimXpertFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)
[Get DimXpert Features and Annotations Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

This interface is the base class for several more specific DimXpert feature interfaces (see the **See Also** section below). Use the [IDimXpertFeature::Type](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~Type.html) property to find out which specific feature interface is needed to acquire more information for a given DimXpert feature.

Note that some features, such as swDimXpertFeatureType_e.swDimXpertFeature_Surface, do not have more specific interfaces. Those particular features are completely defined by the IDimXpertFeature interface.

## Accessors

[IAnnotation::GetDimXpertFeature](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetDimXpertFeature.html)

[IDimXpertAngleBetweenDimTol::OriginFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAngleBetweenDimTol~OriginFeature.html)

[IDimxpertAnnotation::Feature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~Feature.html)

[IDimXpertBestfitPlaneFeature::GetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertBestfitPlaneFeature~GetSubFeatures.html) and [IDimXpertBestfitPlaneFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertBestfitPlaneFeature~IGetSubFeatures.html)

[IDimXpertCompositeDistanceBetweenDimTol::GetFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetFeature.html), [IDimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.html), [IDimXpertCompositeDistanceBetweenDimTol::GetOriginFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompositeDistanceBetweenDimTol~GetOriginFeature.html)

[IDimXpertCompoundClosedSlot3DFeature::GetBottomFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetBottomFeature.html) and [IDimXpertCompoundClosedSlot3DFeature::GetEndFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetEndFeatures.html)

[IDimXpertCompoundHoleFeature::GetBottomFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetBottomFeature.html), [IDimXpertCompoundHoleFeature::GetReferenceFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetReferenceFeature.html), [IDimXpertCompoundHoleFeature::GetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundHoleFeature~GetSubFeatures.html), [IDimXpertCompoundHoleFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundHoleFeature~IGetSubFeatures.html)

[IDimXpertCompoundNotchFeature::GetBottomFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetBottomFeature.html), [IDimXpertCompoundNotchFeature::GetEndFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetEndFeature.html), [IDimXpertCompoundNotchFeature::GetOpenSideReferenceFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetOpenSideReferenceFeature.html), [IDimXpertCompoundNotchFeature::GetTopReferenceFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetTopReferenceFeature.html)

[IDimXpertCounterBoreDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCounterBoreDimTol~ReferenceFeature.html)

[IDimXpertCounterSinkAngleDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCounterSinkAngleDimTol~ReferenceFeature.html)

[IDimXpertCounterSinkDiameterDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertCounterSinkDiameterDimTol~ReferenceFeature.html)

[IDimXpertDepthDimTol::ReferenceFeature property](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDepthDimTol~ReferenceFeature.html)

[IDimXpertDistanceBetweenDimTol::GetFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol~GetFeature.html) and [IDimXpertDistanceBetweenDimTol::GetOriginFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDistanceBetweenDimTol~GetOriginFeature.html)

[IDimXpertExtrudeFeature::GetBottomBlends](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetBottomBlends.html), [IDimXpertExtrudeFeature::GetTopBlends](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetTopBlends.html), [IDimXpertExtrudeFeature::GetBottomFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetBottomFeature.html), [IDimXpertExtrudeFeature::GetReferenceFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetReferenceFeature.html), [IDimXpertExtrudeFeature::GetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~GetSubFeatures.html), [IDimXpertExtrudeFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertExtrudeFeature~IGetSubFeatures.html)

[IDimXpertFeature::GetAppliedFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetAppliedFeatures.html) and [IDimXpertFeature::IGetAppliedFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~IGetAppliedFeatures.html)

[IDimXpertIntersectPlaneFeature::GetFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertIntersectPlaneFeature~GetFeatures.html)

[IDimXpertIntersectPointFeature::GetFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertIntersectPointFeature~GetFeatures.html)

[IDimXpertPart::GetFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetFeatures.html) and [IDimXpertPart::IGetFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~IGetFeatures.html)

[IDimXpertPart::GetFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetFeature.html)

[IDimXpertPatternFeature::GetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPatternFeature~GetSubFeatures.html) and [IDimXpertPatternFeature::IGetSubFeatures](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPatternFeature~IGetSubFeatures.html)

[IDimXpertTangencyTolerance::OriginFeature property](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTangencyTolerance~OriginFeature.html)

[IFeature::GetSpecificFeature2](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## See Also

[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
[IDimXpertBestfitPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertBestfitPlaneFeature.html)
[IDimXpertChamferFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertChamferFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundHoleFeature.html)
[IDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature.html)
[IDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature.html)
[IDimXpertConeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature.html)
[IDimXpertCylinderFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature.html)
[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertFilletFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature.html)
[IDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectCircleFeature.html)
[IDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectLineFeature.html)
[IDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPlaneFeature.html)
[IDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertIntersectPointFeature.html)
[IDimXpertPatternFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPatternFeature.html)
[IDimXpertPlaneFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPlaneFeature.html)
[IDimXpertSphereFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature.html)
