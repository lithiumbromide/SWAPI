---
title: "IGetSecondaryDatums Method (IDimXpertTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTolerance"
member: "IGetSecondaryDatums"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance~IGetSecondaryDatums.html"
---

# IGetSecondaryDatums Method (IDimXpertTolerance)

Gets all of the secondary datums in this DimXpert tolerance annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSecondaryDatums( _
   ByVal Count As System.Integer _
) As DimXpertDatum
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTolerance
Dim Count As System.Integer
Dim value As DimXpertDatum

value = instance.IGetSecondaryDatums(Count)
```

### C#

```csharp
DimXpertDatum IGetSecondaryDatums(
   System.int Count
)
```

### C++/CLI

```cpp
DimXpertDatum^ IGetSecondaryDatums(
   System.int Count
)
```

### Parameters

- `Count`: Number of secondary datums

### Return Value

in-process, unmanaged C++: Pointer to an array of [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

See [In-process Methods](sldworksapiprogguide.chm::/Overview/In-process_Methods.htm) for details about this type of method.

Before calling this method, call [IDimXpertTolerance::GetSecondaryDatumCount](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~GetSecondaryDatumCount.html) to get the value for the Count parameter.

The members of the array returned by this method map to the members of the array returned by [IGetDimXpertTolerance::IGetSecondaryDatumModifiers](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance~IGetSecondaryDatumModifiers.html).

## See Also

[IDimXpertTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance.html)
[IDimXpertTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
