---
title: "GetNominalCompoundWidth Method (ISwDMDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundWidthFeature"
member: "GetNominalCompoundWidth"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature~GetNominalCompoundWidth.html"
---

# GetNominalCompoundWidth Method (ISwDMDimXpertCompoundWidthFeature)

Gets the coordinates and vector for this DimXpert compound width.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNominalCompoundWidth( _
   ByRef width As System.Double, _
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
Dim instance As ISwDMDimXpertCompoundWidthFeature
Dim width As System.Double
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetNominalCompoundWidth(width, X, Y, Z, I, J, K)
```

### C#

```csharp
System.bool GetNominalCompoundWidth(
   out System.double width,
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
System.bool GetNominalCompoundWidth(
   [Out] System.double width,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `width`: Width of compound width
- `X`: x coordinate of compound width
- `Y`: y coordinate of compound width
- `Z`: z coordinate of compound width
- `I`: i component of the direction vector of compound width
- `J`: j component of the direction vector of compound width
- `K`: k component of the direction vector of compound width

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundWidthFeature::GetNominalCompoundWidth](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundWidthFeature~GetNominalCompoundWidth.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.html)
[ISwDMDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
