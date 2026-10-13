---
title: "CurrencySeparator Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "CurrencySeparator"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencySeparator.html"
---

# CurrencySeparator Property (ICostAnalysis)

Gets the delimiter for the currency from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencySeparator As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::CurrencyCode Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyCode.html)
[ICostAnalysis::CurrencyName Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyName.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
