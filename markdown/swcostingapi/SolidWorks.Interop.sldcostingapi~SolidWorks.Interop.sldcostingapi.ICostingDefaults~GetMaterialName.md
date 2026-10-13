---
title: "GetMaterialName Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "GetMaterialName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialName.html"
---

# GetMaterialName Method (ICostingDefaults)

Gets the name of the default material for the specified manufacturing method for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialName( _
   ByVal MethodType As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim MethodType As System.Integer
Dim value As System.String

value = instance.GetMaterialName(MethodType)
```

### C#

```csharp
System.string GetMaterialName(
   System.int MethodType
)
```

### C++/CLI

```cpp
System.String^ GetMaterialName(
   System.int MethodType
)
```

### Parameters

- `MethodType`: Manufacturing method as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

### Return Value

Name of the default material for MethodType

## VBA Syntax

See [CostDefaults::GetMaterialName](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~GetMaterialName.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialClass.html)
[ICostingDefaults::SetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialClass.html)
[ICostingDefaults::SetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialName.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
