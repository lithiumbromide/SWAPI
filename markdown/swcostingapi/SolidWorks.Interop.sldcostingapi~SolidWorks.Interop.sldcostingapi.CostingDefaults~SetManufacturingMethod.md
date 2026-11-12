---
title: "SetManufacturingMethod Method (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "SetManufacturingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~SetManufacturingMethod.html"
---

# SetManufacturingMethod Method (CostingDefaults)

Sets the default manufacturing method for the specified type of body for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetManufacturingMethod( _
   ByVal BodyType As System.Integer, _
   ByVal DefaultMethod As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim BodyType As System.Integer
Dim DefaultMethod As System.Integer

instance.SetManufacturingMethod(BodyType, DefaultMethod)
```

### C#

```csharp
void SetManufacturingMethod(
   System.int BodyType,
   System.int DefaultMethod
)
```

### C++/CLI

```cpp
void SetManufacturingMethod(
   System.int BodyType,
   System.int DefaultMethod
)
```

### Parameters

- `BodyType`: Body type as defined in [swcBodyType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcBodyType_e.html)
- `DefaultMethod`: Default manufacturing method for BodyType as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

## VBA Syntax

See [CostDefaults::SetManufacturingMethod](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~SetManufacturingMethod.html).

## Remarks

Changes made to default settings are saved to the registry and are applied in the next and subsequent Costing sessions.

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
