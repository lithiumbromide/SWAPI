---
title: "GetUpperAndLowerLimit Method (ISwDMDimXpertDimensionTolerance)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDimensionTolerance"
member: "GetUpperAndLowerLimit"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance~GetUpperAndLowerLimit.html"
---

# GetUpperAndLowerLimit Method (ISwDMDimXpertDimensionTolerance)

Gets the upper and lower tolerance limits for this DimXpert dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUpperAndLowerLimit( _
   ByRef Upper As System.Double, _
   ByRef Lower As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDimensionTolerance
Dim Upper As System.Double
Dim Lower As System.Double
Dim value As System.Boolean

value = instance.GetUpperAndLowerLimit(Upper, Lower)
```

### C#

```csharp
System.bool GetUpperAndLowerLimit(
   out System.double Upper,
   out System.double Lower
)
```

### C++/CLI

```cpp
System.bool GetUpperAndLowerLimit(
   [Out] System.double Upper,
   [Out] System.double Lower
)
```

### Parameters

- `Upper`: Upper tolerance limit
- `Lower`: Lower tolerance limit

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertDimensionTolerance::GetUpperAndLowerLimit](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDimensionTolerance~GetUpperAndLowerLimit.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDimensionTolerance Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html)
[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
