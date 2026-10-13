---
title: "GetNominalBottomPlane Method (ISwDMDimXpertCompoundClosedSlot3dFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundClosedSlot3dFeature"
member: "GetNominalBottomPlane"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetNominalBottomPlane.html"
---

# GetNominalBottomPlane Method (ISwDMDimXpertCompoundClosedSlot3dFeature)

Gets the coordinates and vector for the reference plane at the bottom of this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalBottomPlane( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundClosedSlot3dFeature
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalBottomPlane(X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalBottomPlane(
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetNominalBottomPlane(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `X`: x coordinate of the bottom plane
- `Y`: y coordinate of the bottom plane
- `Z`: z coordinate of the bottom plane
- `I`: i component of the direction vector of the bottom plane
- `J`: j component of the direction vector of the bottom plane
- `K`: k component of the direction vector of the bottom plane

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundClosedSlot3dFeature::GetNominalBottomPlane](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundClosedSlot3dFeature~GetNominalBottomPlane.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.html)
[ISwDMDimXpertCompoundClosedSlot3dFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
