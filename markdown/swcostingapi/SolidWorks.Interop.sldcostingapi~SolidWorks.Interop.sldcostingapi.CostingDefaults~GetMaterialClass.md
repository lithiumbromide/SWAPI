---
title: "GetMaterialClass Method (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "GetMaterialClass"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~GetMaterialClass.html"
---

# GetMaterialClass Method (CostingDefaults)

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
Dim instance As CostingDefaults
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

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
