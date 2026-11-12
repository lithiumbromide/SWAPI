---
title: "ReferenceFeature Property (ISwDMDimXpertCounterBoreDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCounterBoreDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (ISwDMDimXpertCounterBoreDimTol)

Gets the DimXpert reference feature for this DimXpert counterbore dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCounterBoreDimTol
Dim value As SwDMDimXpertFeature

value = instance.ReferenceFeature
```

### C#

```csharp
SwDMDimXpertFeature ReferenceFeature {get;}
```

### C++/CLI

```cpp
property SwDMDimXpertFeature^ ReferenceFeature {
   SwDMDimXpertFeature^ get();
}
```

### Property Value

[ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

## VBA Syntax

See [SwDMDimXpertCounterBoreDimTol::ReferenceFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCounterBoreDimTol~ReferenceFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCounterBoreDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol.html)
[ISwDMDimXpertCounterBoreDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
