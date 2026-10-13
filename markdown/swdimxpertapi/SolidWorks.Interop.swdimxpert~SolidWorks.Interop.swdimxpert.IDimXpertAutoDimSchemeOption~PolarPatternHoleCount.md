---
title: "PolarPatternHoleCount Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "PolarPatternHoleCount"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~PolarPatternHoleCount.html"
---

# PolarPatternHoleCount Property (IDimXpertAutoDimSchemeOption)

Gets and sets the number of holes to dimension in the polar pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property PolarPatternHoleCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Integer

instance.PolarPatternHoleCount = value

value = instance.PolarPatternHoleCount
```

### C#

```csharp
System.int PolarPatternHoleCount {get; set;}
```

### C++/CLI

```cpp
property System.int PolarPatternHoleCount {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of holes to dimension in the polar pattern; default is 5

## VBA Syntax

See [DimXpertAutoDimSchemeOption::PolarPatternHoleCount](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~PolarPatternHoleCount.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
