---
title: "Feature Property (ISwDMDimXpertAnnotation)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAnnotation"
member: "Feature"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~Feature.html"
---

# Feature Property (ISwDMDimXpertAnnotation)

Gets the DimXpert feature to which this DimXpert annotation is applied.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Feature As SwDMDimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAnnotation
Dim value As SwDMDimXpertFeature

value = instance.Feature
```

### C#

```csharp
SwDMDimXpertFeature Feature {get;}
```

### C++/CLI

```cpp
property SwDMDimXpertFeature^ Feature {
   SwDMDimXpertFeature^ get();
}
```

### Property Value

[ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

## VBA Syntax

See [SwDMDimXpertAnnotation::Feature](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAnnotation~Feature.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
