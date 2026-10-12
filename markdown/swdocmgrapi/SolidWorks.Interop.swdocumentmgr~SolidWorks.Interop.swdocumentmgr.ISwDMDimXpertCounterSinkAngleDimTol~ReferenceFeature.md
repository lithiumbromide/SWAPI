---
title: "ReferenceFeature Property (ISwDMDimXpertCounterSinkAngleDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCounterSinkAngleDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (ISwDMDimXpertCounterSinkAngleDimTol)

Gets the DimXpert reference feature for this DimXpert countersink angle dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCounterSinkAngleDimTol
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

See [SwDMDimXpertCounterSinkAngleDimTol::ReferenceFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCounterSinkAngleDimTol~ReferenceFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCounterSinkAngleDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol.html)
[ISwDMDimXpertCounterSinkAngleDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
