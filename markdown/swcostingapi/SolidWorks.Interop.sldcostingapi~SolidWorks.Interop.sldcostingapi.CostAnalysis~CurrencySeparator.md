---
title: "CurrencySeparator Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "CurrencySeparator"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~CurrencySeparator.html"
---

# CurrencySeparator Property (CostAnalysis)

Gets the delimiter for the currency from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencySeparator As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.String

value = instance.CurrencySeparator
```

### C#

```csharp
System.string CurrencySeparator {get;}
```

### C++/CLI

```cpp
property System.String^ CurrencySeparator {
   System.String^ get();
}
```

### Property Value

Delimiter for the currency:

- **Period** (e.g., 1.00)
  - or -
- **Comma** (e.g., 1, 00)

## VBA Syntax

See [CostAnalysis::CurrencySeparator](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~CurrencySeparator.html).

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
