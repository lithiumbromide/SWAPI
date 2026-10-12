---
title: "IGetSecondaryDatums Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "IGetSecondaryDatums"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetSecondaryDatums.html"
---

# IGetSecondaryDatums Method (ISwDMDimXpertGeometricTolerance)

Gets all of the secondary datums in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSecondaryDatums( _
   ByVal Count As System.Integer _
) As swDmDimXpertDatum
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim Count As System.Integer
Dim value As swDmDimXpertDatum

value = instance.IGetSecondaryDatums(Count)
```

### C#

```csharp
swDmDimXpertDatum IGetSecondaryDatums(
   System.int Count
)
```

### C++/CLI

```cpp
swDmDimXpertDatum^ IGetSecondaryDatums(
   System.int Count
)
```

### Parameters

- `Count`: Number of secondary datums

### Return Value

in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertDatum](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDatum.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertGeometricTolerance::GetSecondaryDatumCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetSecondaryDatumCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimXpertGeometricTolerance::GetSecondaryDatums Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetSecondaryDatums.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
