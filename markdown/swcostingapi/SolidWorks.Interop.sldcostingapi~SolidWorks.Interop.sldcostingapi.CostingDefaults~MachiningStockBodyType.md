---
title: "MachiningStockBodyType Property (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "MachiningStockBodyType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~MachiningStockBodyType.html"
---

# MachiningStockBodyType Property (CostingDefaults)

Gets or sets the default machining stock body type for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property MachiningStockBodyType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim value As System.Integer

instance.MachiningStockBodyType = value

value = instance.MachiningStockBodyType
```

### C#

```csharp
System.int MachiningStockBodyType {get; set;}
```

### C++/CLI

```cpp
property System.int MachiningStockBodyType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default machining stock body type as defined in [swcStockType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcStockType_e.html)

## VBA Syntax

See [CostDefaults::MachiningStockBodyType](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~MachiningStockBodyType.html).

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
