---
title: "Inner Property (ISwDMDimXpertCylinderFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCylinderFeature"
member: "Inner"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature~Inner.html"
---

# Inner Property (ISwDMDimXpertCylinderFeature)

Gets whether this DimXpert cylinder is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCylinderFeature
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

True if the cylinder is a hole; false if it's a pin

## VBA Syntax

See [SwDMDimXpertCylinderFeature::Inner](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCylinderFeature~Inner.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.html)
[ISwDMDimXpertCylinderFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
