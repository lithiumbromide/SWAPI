---
title: "Supplement Property (ISwDMDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAngleBetweenDimTol"
member: "Supplement"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol~Supplement.html"
---

# Supplement Property (ISwDMDimXpertAngleBetweenDimTol)

Gets whether to evaluate the supplement angle for this DimXpert angle-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Supplement As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAngleBetweenDimTol
Dim value As System.Boolean

value = instance.Supplement
```

### C#

```csharp
System.bool Supplement {get;}
```

### C++/CLI

```cpp
property System.bool Supplement {
   System.bool get();
}
```

### Property Value

True to evaluate the supplement angle; false to not

## VBA Syntax

See [SwDMDimXpertAngleBetweenDimTol::Supplement](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAngleBetweenDimTol~Supplement.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol.html)
[ISwDMDimXpertAngleBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
