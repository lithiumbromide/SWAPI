---
title: "LinkToKFactor Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "LinkToKFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LinkToKFactor.html"
---

# LinkToKFactor Property (ISMNormalCutFeatureData2)

Gets or sets whether to link to a K-Factor when adjusting the offset plane of this Normal Cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToKFactor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Boolean

instance.LinkToKFactor = value

value = instance.LinkToKFactor
```

### C#

```csharp
System.bool LinkToKFactor {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToKFactor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link to a K-Factor, false to not

## VBA Syntax

See [SMNormalCutFeatureData2::LinkToKFactor](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~LinkToKFactor.html).

## Remarks

This property is valid only if:

- [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.html) is set to [swNormalCutParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane

- and -

- [ISMNormalCutFeatureData2::OffsetPlaneReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OffsetPlaneReference.html) is set.

If this property is set to true, then [ISMNormalCutFeatureData2::LayerAdjustmentValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LayerAdjustmentValue.html) is automatically set to 0.5.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
