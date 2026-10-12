---
title: "StructuralMemberStockType Property (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "StructuralMemberStockType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~StructuralMemberStockType.html"
---

# StructuralMemberStockType Property (CostingDefaults)

Gets or sets the default type of structural member stock cost method for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property StructuralMemberStockType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim value As System.Integer

instance.StructuralMemberStockType = value

value = instance.StructuralMemberStockType
```

### C#

```csharp
System.int StructuralMemberStockType {get; set;}
```

### C++/CLI

```cpp
property System.int StructuralMemberStockType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default type of structural member stock cost method as defined in [swcStructuralStockCostType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcStructuralStockCostType_e.html)

## VBA Syntax

See [CostDefaults::StructuralMemberStockType](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~StructuralMemberStockType.html).

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
