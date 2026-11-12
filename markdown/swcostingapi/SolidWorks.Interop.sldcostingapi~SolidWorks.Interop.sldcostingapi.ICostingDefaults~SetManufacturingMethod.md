---
title: "SetManufacturingMethod Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "SetManufacturingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetManufacturingMethod.html"
---

# SetManufacturingMethod Method (ICostingDefaults)

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
Dim instance As ICostingDefaults
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

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetManufacturingMethod Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetManufacturingMethod.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
