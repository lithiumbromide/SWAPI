---
title: "GetManufacturingMethod Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "GetManufacturingMethod"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetManufacturingMethod.html"
---

# GetManufacturingMethod Method (ICostingDefaults)

Gets the default manufacturing method for the specified type of body for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetManufacturingMethod( _
   ByVal BodyType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim BodyType As System.Integer
Dim value As System.Integer

value = instance.GetManufacturingMethod(BodyType)
```

### C#

```csharp
System.int GetManufacturingMethod(
   System.int BodyType
)
```

### C++/CLI

```cpp
System.int GetManufacturingMethod(
   System.int BodyType
)
```

### Parameters

- `BodyType`: Body type as defined in [swcBodyType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcBodyType_e.html)

### Return Value

Default manufacturing method for BodyType as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

## VBA Syntax

See [CostDefaults::GetManufacturingMethod](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~GetManufacturingMethod.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::SetManufacturingMethod Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetManufacturingMethod.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
