---
title: "Blind Property (ISwDMDimXpertCompoundHoleFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundHoleFeature"
member: "Blind"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~Blind.html"
---

# Blind Property (ISwDMDimXpertCompoundHoleFeature)

Gets whether this DimXpert compound hole is blind or through all.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Blind As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundHoleFeature
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

True if the compound hole is blind; false if through all

## VBA Syntax

See [SwDMDimXpertCompoundHoleFeature::Blind](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundHoleFeature~Blind.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.html)
[ISwDMDimXpertCompoundHoleFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
