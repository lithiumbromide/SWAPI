---
title: "GetMaterialClass Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "GetMaterialClass"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialClass.html"
---

# GetMaterialClass Method (ICostingDefaults)

Gets the name of the default material class for the specified manufacturing method for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialClass( _
   ByVal MethodType As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim MethodType As System.Integer
Dim value As System.String

value = instance.GetMaterialClass(MethodType)
```

### C#

```csharp
System.string GetMaterialClass(
   System.int MethodType
)
```

### C++/CLI

```cpp
System.String^ GetMaterialClass(
   System.int MethodType
)
```

### Parameters

- `MethodType`: Manufacturing method as defined in [swcMethodType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcMethodType_e.html)

### Return Value

Name of the default material class for MethodType

## VBA Syntax

See [CostDefaults::GetMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~GetMaterialClass.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetMaterialName.html)
[ICostingDefaults::SetMaterialClass Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialClass.html)
[ICostingDefaults::SetMaterialName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetMaterialName.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
