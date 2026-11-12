---
title: "GetTemplateCount Method (CostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "CostManager"
member: "GetTemplateCount"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager~GetTemplateCount.html"
---

# GetTemplateCount Method (CostManager)

Gets the number of Costing templates available for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateCount( _
   ByVal CostingType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostManager
Dim CostingType As System.Integer
Dim value As System.Integer

value = instance.GetTemplateCount(CostingType)
```

### C#

```csharp
System.int GetTemplateCount(
   System.int CostingType
)
```

### C++/CLI

```cpp
System.int GetTemplateCount(
   System.int CostingType
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)

### Return Value

Number of Costing templates available for CostingType

## VBA Syntax

See [CostManager::GetTemplateCount](swcostingapivb6.chm::/SldCostingAPI~CostManager~GetTemplateCount.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager.html)
[CostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostManager_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
