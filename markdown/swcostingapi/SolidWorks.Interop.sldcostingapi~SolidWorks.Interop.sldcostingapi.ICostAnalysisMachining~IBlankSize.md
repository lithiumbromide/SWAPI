---
title: "IBlankSize Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "IBlankSize"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IBlankSize.html"
---

# IBlankSize Property (ICostAnalysisMachining)

Gets or sets the size of the blank for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property IBlankSize( _
   ByVal NumDimensions As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim NumDimensions As System.Integer
Dim value As System.Double

instance.IBlankSize(NumDimensions) = value

value = instance.IBlankSize(NumDimensions)
```

### C#

```csharp
System.double IBlankSize(
   System.int NumDimensions
) {get; set;}
```

### C++/CLI

```cpp
property System.double IBlankSize {
   System.double get(System.int NumDimensions);
   void set (System.int NumDimensions, System.double value);
}
```

### Parameters

- `NumDimensions`: Number of dimensions for the blank

### Property Value

- in-process, unmanaged C++: Pointer to an array of doubles of the size of the blank (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisMachining::GetBlankDimensionCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetBlankDimensionCount.html) to get the NumDimensions value.

The material determines the size of the array:

| Material | Array |
| --- | --- |
| Block | 3 doubles for the X, Y, and Z coordinates |
| Cylinder | 2 doubles for the diameter and length |
| Plate | 2 doubles for the length and width |

This property does not support setting:

- block or cylinder material when size is calculated by [ICostAnalysisMachining::IMargins](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~IMargins.html).
- plate material. [Thickness](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentPlateThickness.html) is a property of the [material](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterial.html).

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::BlankSize Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~BlankSize.html)
[ICostAnalysisMachining::GetMinimumBlankSize Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMinimumBlankSize.html)
[ICostAnalysisMachining::IGetMinimumBlankSize Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMinimumBlankSize.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
