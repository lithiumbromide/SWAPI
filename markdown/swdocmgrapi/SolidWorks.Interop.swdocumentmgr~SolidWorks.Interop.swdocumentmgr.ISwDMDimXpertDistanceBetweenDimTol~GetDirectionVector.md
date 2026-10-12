---
title: "GetDirectionVector Method (ISwDMDimXpertDistanceBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDistanceBetweenDimTol"
member: "GetDirectionVector"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetDirectionVector.html"
---

# GetDirectionVector Method (ISwDMDimXpertDistanceBetweenDimTol)

Gets the direction vector for this DimXpert distance-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDistanceBetweenDimTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetDirectionVector(I, J, K)
```

### C#

```csharp
System.bool GetDirectionVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetDirectionVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`: i component of direction vector
- `J`: j component of direction vector
- `K`: k component of direction vector

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertDistanceBetweenDimTol::GetDirectionVector](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDistanceBetweenDimTol~GetDirectionVector.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.html)
[ISwDMDimXpertDistanceBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
