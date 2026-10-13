---
title: "BlankSize Property (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "BlankSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~BlankSize.html"
---

# BlankSize Property (CostAnalysisMachining)

Gets or sets the size of the blank for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankSize As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim value As System.Object

instance.BlankSize = value

value = instance.BlankSize
```

### C#

```csharp
System.object BlankSize {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BlankSize {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

The material determines the size of the array:

| Material | Array |
| --- | --- |
| Block | 3 doubles for the X, Y, and Z coordinates |
| Cylinder | 2 doubles for the diameter and length |
| Plate | 2 doubles for the length and width |

This property does not support setting:

- block or cylinder material when size is calculated by [ICostAnalysisMachining::Margins](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~Margins.html).

- plate material. [Thickness](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentPlateThickness.html) is a property of the [material](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterial.html).

## VBA Syntax

See [CostAnalysisMachining::BlankSize](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~BlankSize.html).

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
