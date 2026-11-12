---
title: "GetDirectionVector Method (ISwDMDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAngleBetweenDimTol"
member: "GetDirectionVector"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol~GetDirectionVector.html"
---

# GetDirectionVector Method (ISwDMDimXpertAngleBetweenDimTol)

Gets the direction vector for computing the angle of this DimXpert angle-between dimension tolerance.

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
Dim instance As ISwDMDimXpertAngleBetweenDimTol
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

See [SwDMDimXpertAngleBetweenDimTol::GetDirectionVector](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAngleBetweenDimTol~GetDirectionVector.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol.html)
[ISwDMDimXpertAngleBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
