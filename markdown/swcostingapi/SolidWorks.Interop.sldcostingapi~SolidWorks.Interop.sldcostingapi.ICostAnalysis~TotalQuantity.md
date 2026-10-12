---
title: "TotalQuantity Property (ICostAnalysis)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis"
member: "TotalQuantity"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~TotalQuantity.html"
---

# TotalQuantity Property (ICostAnalysis)

Gets or sets the total quantity of parts to produce for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalQuantity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis
Dim value As System.Integer

instance.TotalQuantity = value

value = instance.TotalQuantity
```

### C#

```csharp
System.int TotalQuantity {get; set;}
```

### C++/CLI

```cpp
property System.int TotalQuantity {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Total quantity of parts to produce

## VBA Syntax

See [CostAnalysis::TotalQuantity](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis~TotalQuantity.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysies (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysis Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis.html)
[ICostAnalysis Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis_members.html)
[ICostAnalysis::LotSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis~LotSize.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
