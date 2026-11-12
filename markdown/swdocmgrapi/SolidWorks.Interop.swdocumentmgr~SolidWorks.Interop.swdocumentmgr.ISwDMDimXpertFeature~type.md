---
title: "type Property (ISwDMDimXpertFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertFeature"
member: "type"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~type.html"
---

# type Property (ISwDMDimXpertFeature)

Gets the type of this DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property type As swDmDimXpertFeatureType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertFeature
Dim value As swDmDimXpertFeatureType_e

value = instance.type
```

### C#

```csharp
swDmDimXpertFeatureType_e type {get;}
```

### C++/CLI

```cpp
property swDmDimXpertFeatureType_e type {
   swDmDimXpertFeatureType_e get();
}
```

### Property Value

Type of feature as defined in [swDmDimXpertFeatureType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertFeatureType_e.html)

## VBA Syntax

See [SwDMDimXpertFeature::type](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertFeature~type.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
