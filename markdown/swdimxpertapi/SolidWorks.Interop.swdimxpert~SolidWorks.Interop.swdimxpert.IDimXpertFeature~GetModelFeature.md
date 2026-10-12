---
title: "GetModelFeature Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "GetModelFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~GetModelFeature.html"
---

# GetModelFeature Method (IDimXpertFeature)

Gets the SOLIDWORKS model feature corresponding to this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As System.Object

value = instance.GetModelFeature()
```

### C#

```csharp
System.object GetModelFeature()
```

### C++/CLI

```cpp
System.Object^ GetModelFeature();
```

### Return Value

[IFeature](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [DimXpertFeature::GetModelFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~GetModelFeature.html).

## Examples

[Get DimXpert Feature Example (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature Example (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
