---
title: "SetMaterialClass Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "SetMaterialClass"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialClass.html"
---

# SetMaterialClass Method (ICostingDefaults)

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
Dim instance As ICostingDefaults
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

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialClass.html)
[ICostingDefaults::GetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialName.html)
[ICostingDefaults::SetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialName.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
