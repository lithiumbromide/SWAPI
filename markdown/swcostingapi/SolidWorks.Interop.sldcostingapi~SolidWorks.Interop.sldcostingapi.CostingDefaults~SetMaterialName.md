---
title: "SetMaterialName Method (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "SetMaterialName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~SetMaterialName.html"
---

# SetMaterialName Method (CostingDefaults)

Sets the name of the default material for the specified manufacturing method for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialName( _
   ByVal MethodType As System.Integer, _
   ByVal MaterialName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim MethodType As System.Integer
Dim MaterialName As System.String

instance.SetMaterialName(MethodType, MaterialName)
```

### C#

```csharp
void SetMaterialName(
   System.int MethodType,
   System.string MaterialName
)
```

### C++/CLI

```cpp
void SetMaterialName(
   System.int MethodType,
   System.String^ MaterialName
)
```

### Parameters

- `MethodType`: Manufacturing method as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)
- `MaterialName`: Name of default material for MethodType

## VBA Syntax

See [CostDefaults::SetMaterialName](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~SetMaterialName.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## Remarks

Changes made to default settings are saved to the registry and are applied in the next and subsequent Costing sessions.

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
