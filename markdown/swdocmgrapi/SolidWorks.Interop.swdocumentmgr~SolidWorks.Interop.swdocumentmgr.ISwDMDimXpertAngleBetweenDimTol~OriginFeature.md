---
title: "OriginFeature Property (ISwDMDimXpertAngleBetweenDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAngleBetweenDimTol"
member: "OriginFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol~OriginFeature.html"
---

# OriginFeature Property (ISwDMDimXpertAngleBetweenDimTol)

Gets the DimXpert feature of origin for this DimXpert angle-between dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OriginFeature As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAngleBetweenDimTol
Dim value As SwDMDimXpertFeature

value = instance.OriginFeature
```

### C#

```csharp
SwDMDimXpertFeature OriginFeature {get;}
```

### C++/CLI

```cpp
property SwDMDimXpertFeature^ OriginFeature {
   SwDMDimXpertFeature^ get();
}
```

### Property Value

[ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

## VBA Syntax

See [SwDMDimXpertAngleBetweenDimTol::OriginFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAngleBetweenDimTol~OriginFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol.html)
[ISwDMDimXpertAngleBetweenDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
