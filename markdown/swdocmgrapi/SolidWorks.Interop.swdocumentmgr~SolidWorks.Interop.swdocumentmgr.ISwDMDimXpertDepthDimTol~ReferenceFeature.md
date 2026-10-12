---
title: "ReferenceFeature Property (ISwDMDimXpertDepthDimTol)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertDepthDimTol"
member: "ReferenceFeature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol~ReferenceFeature.html"
---

# ReferenceFeature Property (ISwDMDimXpertDepthDimTol)

Gets the DimXpert reference feature for this DimXpert depth dimension tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceFeature As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertDepthDimTol
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

See [SwDMDimXpertDepthDimTol::ReferenceFeature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertDepthDimTol~ReferenceFeature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertDepthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol.html)
[ISwDMDimXpertDepthDimTol Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
