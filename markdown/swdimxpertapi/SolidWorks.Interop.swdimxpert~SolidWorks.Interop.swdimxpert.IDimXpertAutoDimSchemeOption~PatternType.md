---
title: "PatternType Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "PatternType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~PatternType.html"
---

# PatternType Property (IDimXpertAutoDimSchemeOption)

Gets and sets the type of pattern to dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Integer

instance.PatternType = value

value = instance.PatternType
```

### C#

```csharp
System.int PatternType {get; set;}
```

### C++/CLI

```cpp
property System.int PatternType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Pattern type as defined in [swDimXpertAutoDimSchemePatternType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertAutoDimSchemePatternType_e.html); default is swDimXpertAudoDimSchemePatternType_Linear

## VBA Syntax

See [DimXpertAutoDimSchemeOption::PatternType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~PatternType.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
