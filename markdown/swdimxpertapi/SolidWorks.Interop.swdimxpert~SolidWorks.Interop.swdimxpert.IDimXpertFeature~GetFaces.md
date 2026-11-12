---
title: "GetFaces Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "GetFaces"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~GetFaces.html"
---

# GetFaces Method (IDimXpertFeature)

Gets the SOLIDWORKS faces in this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As System.Object

value = instance.GetFaces()
```

### C#

```csharp
System.object GetFaces()
```

### C++/CLI

```cpp
System.Object^ GetFaces();
```

### Return Value

Array of [faces](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [DimXpertFeature::GetFaces](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~GetFaces.html).

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
