---
title: "SetMaterialName Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "SetMaterialName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialName.html"
---

# SetMaterialName Method (ICostingDefaults)

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
Dim instance As ICostingDefaults
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

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialName.html)
[ICostingDefaults::GetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialClass.html)
[ICostingDefaults::SetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
