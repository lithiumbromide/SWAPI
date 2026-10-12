---
title: "DefaultMachiningOperationTool Property (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "DefaultMachiningOperationTool"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~DefaultMachiningOperationTool.html"
---

# DefaultMachiningOperationTool Property (ITemplateOverrides)

Gets or sets the tool for the default machining operation for machined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultMachiningOperationTool As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
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

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
