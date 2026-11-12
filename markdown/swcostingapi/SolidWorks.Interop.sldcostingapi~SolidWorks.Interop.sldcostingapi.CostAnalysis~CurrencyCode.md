---
title: "CurrencyCode Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "CurrencyCode"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~CurrencyCode.html"
---

# CurrencyCode Property (CostAnalysis)

Gets the 3-letter currency code from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencyCode As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.String

value = instance.CurrencyCode
```

### C#

```csharp
System.string CurrencyCode {get;}
```

### C++/CLI

```cpp
property System.String^ CurrencyCode {
   System.String^ get();
}
```

### Property Value

3-letter currency code

## VBA Syntax

See [CostAnalysis::CurrencyCode](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~CurrencyCode.html).

## Remarks

Examples of 3-letter currency codes are:

- **USD** for United States Dollars
- **EUR** for Euros
- **GBP** for British Pounds
- etc.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
