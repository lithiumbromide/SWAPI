---
title: "LotSize Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "LotSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~LotSize.html"
---

# LotSize Property (ICostAnalysis)

Gets or sets the quantity of parts to produce per batch for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property LotSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Integer

instance.LotSize = value

value = instance.LotSize
```

### C#

```csharp
System.int LotSize {get; set;}
```

### C++/CLI

```cpp
property System.int LotSize {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Quantity of parts to produce per batch

## VBA Syntax

See [CostAnalysis::LotSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~LotSize.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::TotalQuantity Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~TotalQuantity.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
