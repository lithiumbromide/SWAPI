---
title: "GetNominalPoint Method (ISwDMDimXpertIntersectPointFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertIntersectPointFeature"
member: "GetNominalPoint"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalPoint.html"
---

# GetNominalPoint Method (ISwDMDimXpertIntersectPointFeature)

Gets the coordinates of this DimXpert intersect point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertIntersectPointFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.GetNominalPoint(X, Y, Z)
```

### C#

```csharp
System.bool GetNominalPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.bool GetNominalPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the intersect point
- `Y`: y coordinate of the intersect point
- `Z`: z coordinate of the intersect point

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertIntersectPointFeature::GetNominalPoint](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertIntersectPointFeature~GetNominalPoint.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.html)
[ISwDMDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
