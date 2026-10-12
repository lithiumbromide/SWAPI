---
title: "IMargins Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "IMargins"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IMargins.html"
---

# IMargins Property (ICostAnalysisMachining)

Gets or sets the margins for the [stock type](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentStockType.html) for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property IMargins( _
   ByVal NumDimensions As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim NumDimensions As System.Integer
Dim value As System.Double

instance.IMargins(NumDimensions) = value

value = instance.IMargins(NumDimensions)
```

### C#

```csharp
System.double IMargins(
   System.int NumDimensions
) {get; set;}
```

### C++/CLI

```cpp
property System.double IMargins {
   System.double get(System.int NumDimensions);
   void set (System.int NumDimensions, System.double value);
}
```

### Parameters

- `NumDimensions`: Number of dimensions for the stock type

### Property Value

- in-process, unmanaged C++: Pointer to an array of doubles of the available margins (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this property, call [ICostAnalysisMachining::GetMarginDimensionCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetMarginDimensionCount.html) to get the NumMargins value.

The material determines the size of the array:

| Material | Array |
| --- | --- |
| Block | 6 doubles for the -X, +X, -Y, +Y, -Z, and +Z ICostAnalysisMachining::SpecificSizeEnabled must bet set to true to specify block dimensions to add to the tightest fitting stock faces. |
| Cylinder | 3 doubles for the -D, -L, and +L |
| Plate | 4 doubles, all 0, for the -W, +W, -L, and +L |

This property does not support setting margins:

- for plate material
  - or -
- when a [custom size](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~IBlankSize.html) is defined.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::Margins Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~Margins.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
