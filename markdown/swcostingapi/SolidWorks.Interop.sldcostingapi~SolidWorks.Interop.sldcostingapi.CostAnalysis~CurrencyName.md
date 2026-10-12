---
title: "CurrencyName Property (CostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysis"
member: "CurrencyName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis~CurrencyName.html"
---

# CurrencyName Property (CostAnalysis)

Gets the name of the currency from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysis
Dim value As System.String

value = instance.CurrencyName
```

### C#

```csharp
System.string CurrencyName {get;}
```

### C++/CLI

```cpp
property System.String^ CurrencyName {
   System.String^ get();
}
```

### Property Value

Name of currency

## VBA Syntax

See [CostAnalysis::CurrencyName](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~CurrencyName.html).

## Remarks

Examples of names of currencies are:

- **United States Dollars**
- **Euros**
- **British Pounds**
- etc.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis.html)
[CostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysis_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
