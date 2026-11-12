---
title: "GetFeatures Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetFeatures.html"
---

# GetFeatures Method (IDimXpertPart)

Gets all of the DimXpert features in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As System.Object

value = instance.GetFeatures()
```

### C#

```csharp
System.object GetFeatures()
```

### C++/CLI

```cpp
System.Object^ GetFeatures();
```

### Return Value

Array of [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)s

## VBA Syntax

See [DimXpertPart::GetFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetFeatures.html).

## Examples

[Get DimXpert Feature (VBA)](Get_DimXpert_Feature_Example_VB.htm)
[Get DimXpert Feature (VB.NET)](Get_DimXpert_Feature_Example_VBNET.htm)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
