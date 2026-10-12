---
title: "type Property (ISwDMDimXpertAnnotation)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertAnnotation"
member: "type"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.html"
---

# type Property (ISwDMDimXpertAnnotation)

Gets the type of this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property type As swDmDimXpertAnnotationType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertAnnotation
Dim value As swDmDimXpertAnnotationType_e

value = instance.type
```

### C#

```csharp
swDmDimXpertAnnotationType_e type {get;}
```

### C++/CLI

```cpp
property swDmDimXpertAnnotationType_e type {
   swDmDimXpertAnnotationType_e get();
}
```

### Property Value

Type of annotation as defined in [swDmDimXpertAnnotationType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertAnnotationType_e.html)

## VBA Syntax

See [SwDMDimXpertAnnotation::type](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertAnnotation~type.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertAnnotation Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html)
[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
