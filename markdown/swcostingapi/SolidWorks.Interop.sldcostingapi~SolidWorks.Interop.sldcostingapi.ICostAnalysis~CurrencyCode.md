---
title: "CurrencyCode Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "CurrencyCode"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyCode.html"
---

# CurrencyCode Property (ICostAnalysis)

Gets the 3-letter currency code from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencyCode As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

Examples of 3-letter currency codes are:

- **USD** for United States Dollars
- **EUR** for Euros
- **GBP** for British Pounds
- etc.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::CurrencyName Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyName.html)
[ICostAnalysis::CurrencySeparator Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencySeparator.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
