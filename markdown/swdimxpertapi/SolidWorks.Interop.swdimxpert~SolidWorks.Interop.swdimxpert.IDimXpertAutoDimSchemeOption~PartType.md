---
title: "PartType Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "PartType"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~PartType.html"
---

# PartType Property (IDimXpertAutoDimSchemeOption)

Gets and sets the type of part to dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Integer

instance.PartType = value

value = instance.PartType
```

### C#

```csharp
System.int PartType {get; set;}
```

### C++/CLI

```cpp
property System.int PartType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Part type as defined in [swDimXpertAutoDimSchemePartType_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertAutoDimSchemePartType_e.html); default is swDimXpertAutoDimSchemePartType_Prismatic

## VBA Syntax

See [DimXpertAutoDimSchemeOption::PartType](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~PartType.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
