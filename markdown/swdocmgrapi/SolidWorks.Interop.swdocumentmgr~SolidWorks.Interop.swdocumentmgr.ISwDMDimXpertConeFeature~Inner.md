---
title: "Inner Property (ISwDMDimXpertConeFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertConeFeature"
member: "Inner"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~Inner.html"
---

# Inner Property (ISwDMDimXpertConeFeature)

Gets whether this DimXpert cone is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertConeFeature
Dim value As System.Boolean

value = instance.Inner
```

### C#

```csharp
System.bool Inner {get;}
```

### C++/CLI

```cpp
property System.bool Inner {
   System.bool get();
}
```

### Property Value

True if the cone is a hole; false if it's a pin

## VBA Syntax

See [SwDMDimXpertConeFeature::Inner](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertConeFeature~Inner.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.html)
[ISwDMDimXpertConeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
