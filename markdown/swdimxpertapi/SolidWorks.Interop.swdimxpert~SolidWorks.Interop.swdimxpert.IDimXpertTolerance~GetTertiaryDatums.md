---
title: "GetTertiaryDatums Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "GetTertiaryDatums"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatums.html"
---

# GetTertiaryDatums Method (IDimXpertTolerance)

Gets all of the tertiary datums in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTertiaryDatums() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Object

value = instance.GetTertiaryDatums()
```

### C#

```csharp
System.object GetTertiaryDatums()
```

### C++/CLI

```cpp
System.Object^ GetTertiaryDatums();
```

### Return Value

Array of [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html)s

## VBA Syntax

See [DimXpertTolerance::GetTertiaryDatums](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~GetTertiaryDatums.html).

## Remarks

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::GetTertiaryDatumModifiers](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatumModifiers.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
