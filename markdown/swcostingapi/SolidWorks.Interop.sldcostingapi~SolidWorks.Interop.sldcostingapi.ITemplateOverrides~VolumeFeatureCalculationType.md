---
title: "VolumeFeatureCalculationType Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "VolumeFeatureCalculationType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~VolumeFeatureCalculationType.html"
---

# VolumeFeatureCalculationType Property (ITemplateOverrides)

Gets or sets the volume feature calculation option for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property VolumeFeatureCalculationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
Dim value As System.Integer

instance.VolumeFeatureCalculationType = value

value = instance.VolumeFeatureCalculationType
```

### C#

```csharp
System.int VolumeFeatureCalculationType {get; set;}
```

### C++/CLI

```cpp
property System.int VolumeFeatureCalculationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Volume feature calculation option as defined in [swcVolumeFeatureCalculationType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcVolumeFeatureCalculationType_e.html)

## VBA Syntax

See [TemplateOverrides::VolumeFeatureCalculationType](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~VolumeFeatureCalculationType.html).

## Remarks

Setting this property is only applied if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::DefaultMachiningOperationTool Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultMachiningOperationTool.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
