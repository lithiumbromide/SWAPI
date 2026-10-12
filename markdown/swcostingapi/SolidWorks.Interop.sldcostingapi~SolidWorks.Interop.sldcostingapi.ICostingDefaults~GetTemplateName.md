---
title: "GetTemplateName Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "GetTemplateName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetTemplateName.html"
---

# GetTemplateName Method (ICostingDefaults)

Gets the path and file name of the default Costing template for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateName( _
   ByVal CostingType As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim CostingType As System.Integer
Dim value As System.String

value = instance.GetTemplateName(CostingType)
```

### C#

```csharp
System.string GetTemplateName(
   System.int CostingType
)
```

### C++/CLI

```cpp
System.String^ GetTemplateName(
   System.int CostingType
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcCostingType_e.html)

### Return Value

Path and file name of the default Costing template

## VBA Syntax

See [CostDefaults::GetTemplateName](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~GetTemplateName.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::SetTemplateName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetTemplateName.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
