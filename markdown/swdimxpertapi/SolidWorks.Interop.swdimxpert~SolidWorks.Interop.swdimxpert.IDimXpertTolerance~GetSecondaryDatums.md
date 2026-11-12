---
title: "GetSecondaryDatums Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "GetSecondaryDatums"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~GetSecondaryDatums.html"
---

# GetSecondaryDatums Method (IDimXpertTolerance)

Gets all of the secondary datums in this DimXpert geometric tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSecondaryDatums() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim value As System.Object

value = instance.GetSecondaryDatums()
```

### C#

```csharp
System.object GetSecondaryDatums()
```

### C++/CLI

```cpp
System.Object^ GetSecondaryDatums();
```

### Return Value

Array of [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html)s

## VBA Syntax

See [DimXpertTolerance::GetSecondaryDatums](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTolerance~GetSecondaryDatums.html).

## Remarks

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::GetSecondaryDatumModifiers](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetSecondaryDatumModifiers.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
