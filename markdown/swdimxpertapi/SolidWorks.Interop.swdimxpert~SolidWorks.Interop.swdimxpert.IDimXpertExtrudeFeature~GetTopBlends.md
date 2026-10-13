---
title: "GetTopBlends Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "GetTopBlends"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~GetTopBlends.html"
---

# GetTopBlends Method (IDimXpertExtrudeFeature)

Gets the top blend DimXpert feature for this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTopBlends() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
Dim value As DimXpertFeature

value = instance.GetTopBlends()
```

### C#

```csharp
DimXpertFeature GetTopBlends()
```

### C++/CLI

```cpp
DimXpertFeature^ GetTopBlends();
```

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertExtrudeFeature::GetTopBlends](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~GetTopBlends.html).

## Remarks

The top blend is typically an [IDimXpertFilletFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFilletFeature.html).

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
