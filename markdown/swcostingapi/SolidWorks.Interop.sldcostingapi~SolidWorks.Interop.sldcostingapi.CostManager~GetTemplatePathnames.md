---
title: "GetTemplatePathnames Method (CostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "CostManager"
member: "GetTemplatePathnames"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager~GetTemplatePathnames.html"
---

# GetTemplatePathnames Method (CostManager)

Gets the paths and filenames of the Costing templates available for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplatePathnames( _
   ByVal CostingType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostManager
Dim CostingType As System.Integer
Dim value As System.Object

value = instance.GetTemplatePathnames(CostingType)
```

### C#

```csharp
System.object GetTemplatePathnames(
   System.int CostingType
)
```

### C++/CLI

```cpp
System.Object^ GetTemplatePathnames(
   System.int CostingType
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)

### Return Value

Array of strings of the paths and filenames of the Costing templates available for CostingType

## VBA Syntax

See [CostManager::GetTemplatePathnames](swcostingapivb6.chm::/SldCostingAPI~CostManager~GetTemplatePathnames.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager.html)
[CostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
