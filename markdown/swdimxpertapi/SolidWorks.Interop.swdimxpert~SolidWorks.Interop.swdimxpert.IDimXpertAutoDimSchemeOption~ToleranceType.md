---
title: "ToleranceType Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "ToleranceType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~ToleranceType.html"
---

# ToleranceType Property (IDimXpertAutoDimSchemeOption)

Gets and sets the type of tolerance to dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Integer

instance.ToleranceType = value

value = instance.ToleranceType
```

### C#

```csharp
System.int ToleranceType {get; set;}
```

### C++/CLI

```cpp
property System.int ToleranceType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of tolerance as defined in [swDimXpertAutoDimSchemeToleranceType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertAutoDimSchemeToleranceType_e.html); default is swDimXpertAutoDimSchemeToleranceType_PlusMinus

## VBA Syntax

See [DimXpertAutoDimSchemeOption::ToleranceType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~ToleranceType.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
