---
title: "GetBottomBlends Method (IDimXpertExtrudeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertExtrudeFeature"
member: "GetBottomBlends"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature~GetBottomBlends.html"
---

# GetBottomBlends Method (IDimXpertExtrudeFeature)

Gets the bottom blend DimXpert feature for this DimXpert extrude.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomBlends() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertExtrudeFeature
Dim value As DimXpertFeature

value = instance.GetBottomBlends()
```

### C#

```csharp
DimXpertFeature GetBottomBlends()
```

### C++/CLI

```cpp
DimXpertFeature^ GetBottomBlends();
```

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertExtrudeFeature::GetBottomBlends](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertExtrudeFeature~GetBottomBlends.html).

## Examples

[Get DimXpert Extrude Feature Example (VBA)](Get_DimXpert_Extrude_Feature_Example_VB.htm)
[Get DimXpert Extrude Feature Example (VB.NET)](Get_DimXpert_Extrude_Feature_Example_VBNET.htm)

## Remarks

The bottom blend is typically an [IDimXpertFilletFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFilletFeature.html).

## See Also

[IDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature.html)
[IDimXpertExtrudeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
