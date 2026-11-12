---
title: "CurrentPlateThickness Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CurrentPlateThickness"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentPlateThickness.html"
---

# CurrentPlateThickness Property (ICostAnalysisMachining)

Gets or sets the thickness of the plate for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentPlateThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.Double

instance.CurrentPlateThickness = value

value = instance.CurrentPlateThickness
```

### C#

```csharp
System.double CurrentPlateThickness {get; set;}
```

### C++/CLI

```cpp
property System.double CurrentPlateThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness of the plate

## VBA Syntax

See [CostAnalysisMachining::CurrentPlateThickness.](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CurrentPlateThickness.html)

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
