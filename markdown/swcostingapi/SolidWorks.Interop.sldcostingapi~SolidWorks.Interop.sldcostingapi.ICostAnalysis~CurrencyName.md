---
title: "CurrencyName Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "CurrencyName"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyName.html"
---

# CurrencyName Property (ICostAnalysis)

Gets the name of the currency from the Costing template for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrencyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
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

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Examples of names of currencies are:

- **United States Dollars**
- **Euros**
- **British Pounds**
- etc.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::CurrencyCode Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencyCode.html)
[ICostAnalysis::CurrencySeparator Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~CurrencySeparator.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
