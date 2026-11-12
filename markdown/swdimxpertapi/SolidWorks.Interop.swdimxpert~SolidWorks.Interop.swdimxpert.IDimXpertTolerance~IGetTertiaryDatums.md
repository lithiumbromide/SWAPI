---
title: "IGetTertiaryDatums Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "IGetTertiaryDatums"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~IGetTertiaryDatums.html"
---

# IGetTertiaryDatums Method (IDimXpertTolerance)

Gets all of the tertiary datums in this DimXpert tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTertiaryDatums( _
   ByVal Count As System.Integer _
) As DimXpertDatum
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim Count As System.Integer
Dim value As DimXpertDatum

value = instance.IGetTertiaryDatums(Count)
```

### C#

```csharp
DimXpertDatum IGetTertiaryDatums(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertDatum^ IGetTertiaryDatums(
   System.int Count
)
```

### Parameters

- `Count`: Number of tertiary datums

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertTolerance::GetTertiaryDatumCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetTertiaryDatumCount.html) to get the value for the Count parameter.

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::IGetTertiaryDatumModifiers](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~IGetTertiaryDatumModifiers.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
