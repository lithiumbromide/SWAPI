---
title: "LayerAdjustmentValue Property (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "LayerAdjustmentValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LayerAdjustmentValue.html"
---

# LayerAdjustmentValue Property (ISMNormalCutFeatureData2)

Gets or sets the offset plane adjustment value.

## Syntax

### Visual Basic (Declaration)

```vb
Property LayerAdjustmentValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim value As System.Double

instance.LayerAdjustmentValue = value

value = instance.LayerAdjustmentValue
```

### C#

```csharp
System.double LayerAdjustmentValue {get; set;}
```

### C++/CLI

```cpp
property System.double LayerAdjustmentValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= offset <= 1.0

## VBA Syntax

See [SMNormalCutFeatureData2::LayerAdjustmentValue](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~LayerAdjustmentValue.html).

## Remarks

This property is valid only if [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.html) is set to [swNormalCutParameters_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane.

If [ISMNormalCutFeatureData2::LinkToKFactor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LinkToKFactor.html) is set to true, this property is automatically set to 0.5.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
