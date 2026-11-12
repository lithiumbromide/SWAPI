---
title: "Blind Property (ISwDMDimXpertExtrudeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertExtrudeFeature"
member: "Blind"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~Blind.html"
---

# Blind Property (ISwDMDimXpertExtrudeFeature)

Gets whether this DimXpert extrude is blind or through all.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Blind As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertExtrudeFeature
Dim value As System.Boolean

value = instance.Blind
```

### C#

```csharp
System.bool Blind {get;}
```

### C++/CLI

```cpp
property System.bool Blind {
   System.bool get();
}
```

### Property Value

True if the extrude is blind; false if through all

## VBA Syntax

See [SwDMDimXpertExtrudeFeature::Blind](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertExtrudeFeature~Blind.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.html)
[ISwDMDimXpertExtrudeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
