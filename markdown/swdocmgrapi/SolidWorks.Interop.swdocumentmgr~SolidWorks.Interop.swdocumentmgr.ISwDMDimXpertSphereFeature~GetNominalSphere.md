---
title: "GetNominalSphere Method (ISwDMDimXpertSphereFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertSphereFeature"
member: "GetNominalSphere"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature~GetNominalSphere.html"
---

# GetNominalSphere Method (ISwDMDimXpertSphereFeature)

Gets the origin coordinates and radius of this DimXpert sphere.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalSphere( _
   ByRef R As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertSphereFeature
Dim R As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.GetNominalSphere(R, X, Y, Z)
```

### C#

```csharp
System.bool GetNominalSphere(
   out System.double R,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.bool GetNominalSphere(
   [Out] System.double R,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `R`: Radius of the sphere
- `X`: x coordinate of the sphere origin
- `Y`: y coordinate of the sphere origin
- `Z`: z coordinate of the sphere origin

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertSphereFeature::GetNominalSphere](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertSphereFeature~GetNominalSphere.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.html)
[ISwDMDimXpertSphereFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
