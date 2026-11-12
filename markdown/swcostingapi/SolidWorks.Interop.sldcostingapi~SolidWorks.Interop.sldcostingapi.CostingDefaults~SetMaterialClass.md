---
title: "SetMaterialClass Method (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "SetMaterialClass"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~SetMaterialClass.html"
---

# SetMaterialClass Method (CostingDefaults)

Sets the name of the default material class for the specified manufacturing method for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialClass( _
   ByVal MethodType As System.Integer, _
   ByVal MaterialClass As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim MethodType As System.Integer
Dim MaterialClass As System.String

instance.SetMaterialClass(MethodType, MaterialClass)
```

### C#

```csharp
void SetMaterialClass(
   System.int MethodType,
   System.string MaterialClass
)
```

### C++/CLI

```cpp
void SetMaterialClass(
   System.int MethodType,
   System.String^ MaterialClass
)
```

### Parameters

- `MethodType`: Manufacturing method as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)
- `MaterialClass`: Name of default material class for MethodType

## VBA Syntax

See [CostDefaults::SetMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~SetMaterialClass.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## Remarks

Changes made to default settings are saved to the registry and are applied in the next and subsequent Costing sessions.

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
