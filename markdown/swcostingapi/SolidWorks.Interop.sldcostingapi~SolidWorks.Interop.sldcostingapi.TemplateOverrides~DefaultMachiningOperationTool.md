---
title: "DefaultMachiningOperationTool Property (TemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "TemplateOverrides"
member: "DefaultMachiningOperationTool"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides~DefaultMachiningOperationTool.html"
---

# DefaultMachiningOperationTool Property (TemplateOverrides)

Gets or sets the tool for the default machining operation for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultMachiningOperationTool As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As TemplateOverrides
Dim value As System.Integer

instance.DefaultMachiningOperationTool = value

value = instance.DefaultMachiningOperationTool
```

### C#

```csharp
System.int DefaultMachiningOperationTool {get; set;}
```

### C++/CLI

```cpp
property System.int DefaultMachiningOperationTool {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Tool for the default machining operation as defined in [swcDefaultMachiningTool_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcDefaultMachiningTool_e.html)

## VBA Syntax

See [TemplateOverrides::DefaultMachiningOperationTool](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~DefaultMachiningOperationTool.html).

## Remarks

Setting this property is only applied if:

- [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is either swcMethodType_e.swcMethodType_Machining or swcMethodType_e.swcMethodType_MachinedPlate.
- [ITemplateOverrides::VolumeFeatureCalculationType](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~VolumeFeatureCalculationType.html) is swcVolumeFeatureCalculationType_e.swcVolumeFeatureCalculationType_MachiningOperation.

## See Also

[TemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides.html)
[TemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.TemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
