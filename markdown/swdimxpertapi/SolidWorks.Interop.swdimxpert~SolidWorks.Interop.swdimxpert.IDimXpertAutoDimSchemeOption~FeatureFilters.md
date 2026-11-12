---
title: "FeatureFilters Property (IDimXpertAutoDimSchemeOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAutoDimSchemeOption"
member: "FeatureFilters"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~FeatureFilters.html"
---

# FeatureFilters Property (IDimXpertAutoDimSchemeOption)

Gets and sets a feature filter [bitmask](sldworksapiprogguide.chm::/OVERVIEW/Bitmasks.htm) for the Auto Dimension Scheme.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureFilters As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAutoDimSchemeOption
Dim value As System.Integer

instance.FeatureFilters = value

value = instance.FeatureFilters
```

### C#

```csharp
System.int FeatureFilters {get; set;}
```

### C++/CLI

```cpp
property System.int FeatureFilters {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

[Bitmask](sldworksapiprogguide.chm::/OVERVIEW/Bitmasks.htm) of values as defined in [swDimXpertFeatureFilters_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertFeatureFilters_e.html); default is all features or 8191

## VBA Syntax

See [DimXpertAutoDimSchemeOption::FeatureFilters](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAutoDimSchemeOption~FeatureFilters.html).

## Examples

[Auto Dimension Scheme Example (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme Example (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme Example (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## Remarks

This API is in force only when [IDimXpertAutoDimSchemeOption::ScopeAllFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAutoDimSchemeOption~ScopeAllFeature.html) is set to true.

## See Also

[IDimXpertAutoDimSchemeOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)
[IDimXpertAutoDimSchemeOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAutoDimSchemeOption_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
