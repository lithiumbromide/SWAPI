---
title: "GetPrimaryDatums Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "GetPrimaryDatums"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~GetPrimaryDatums.html"
---

# GetPrimaryDatums Method (IDimXpertTolerance)

Gets all of the primary datums in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrimaryDatums() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Object

value = instance.GetPrimaryDatums()
```

### C#

```csharp
System.object GetPrimaryDatums()
```

### C++/CLI

```cpp
System.Object^ GetPrimaryDatums();
```

### Return Value

Array of [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html)s

## VBA Syntax

See [DimXpertTolerance::GetPrimaryDatums](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~GetPrimaryDatums.html).

## Remarks

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::GetPrimaryDatumModifiers](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetPrimaryDatumModifiers.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
