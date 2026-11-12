---
title: "ScopeAllFeature Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "ScopeAllFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~ScopeAllFeature.html"
---

# ScopeAllFeature Property (IDimXpertAutoDimSchemeOption)

Gets and sets whether to dimension all features.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScopeAllFeature As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Boolean

instance.ScopeAllFeature = value

value = instance.ScopeAllFeature
```

### C#

```csharp
System.bool ScopeAllFeature {get; set;}
```

### C++/CLI

```cpp
property System.bool ScopeAllFeature {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to dimension all features (default), false to dimension only selected features

## VBA Syntax

See [DimXpertAutoDimSchemeOption::ScopeAllFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~ScopeAllFeature.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## Remarks

If this API is set to false, then you can only dimension manually selected features whose selection marks are greater than 50.

If this API is set to true, then [IDimXpertAutoDimSchemeOption::FeatureFilters](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~FeatureFilters.html) is in force.

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
