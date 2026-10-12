---
title: "IGetTertiaryDatums Method (ISwDMDimXpertGeometricTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertGeometricTolerance"
member: "IGetTertiaryDatums"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~IGetTertiaryDatums.html"
---

# IGetTertiaryDatums Method (ISwDMDimXpertGeometricTolerance)

Gets all of the tertiary datums in this DimXpert geometric tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTertiaryDatums( _
   ByVal Count As System.Integer _
) As swDmDimXpertDatum
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertGeometricTolerance
Dim Count As System.Integer
Dim value As swDmDimXpertDatum

value = instance.IGetTertiaryDatums(Count)
```

### C#

```csharp
swDmDimXpertDatum IGetTertiaryDatums(
   System.int Count
)
```

### C++/CLI

```cpp
swDmDimXpertDatum^ IGetTertiaryDatums(
   System.int Count
)
```

### Parameters

- `Count`: Number of tertiary datums

### Return Value

in-process, unmanaged C++: Pointer to an array of [ISwDMDimXpertDatum](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertDatum.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Use [ISwDMDimXpertGeometricTolerance::GetTertiaryDatumCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatumCount.html) to populate the Count argument.

## See Also

[ISwDMDimXpertGeometricTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.html)
[ISwDMDimXpertGeometricTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance_members.html)
[ISwDMDimXpertGeometricTolerance::GetTertiaryDatums Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance~GetTertiaryDatums.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
