---
title: "BlankSize Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "BlankSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~BlankSize.html"
---

# BlankSize Property (ICostAnalysisMachining)

Gets or sets the size of the blank for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlankSize As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
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

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::IBlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IBlankSize.html)
[ICostAnalysisMachining::GetMinimumBlankSize Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMinimumBlankSize.html)
[ICostAnalysisMachining::IGetMinimumBlankSize Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMinimumBlankSize.html)
[ICostAnalysisMachining::GetBlankDimensionCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetBlankDimensionCount.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
