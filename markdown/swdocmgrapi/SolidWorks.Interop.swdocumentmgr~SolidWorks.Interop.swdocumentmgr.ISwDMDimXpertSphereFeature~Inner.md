---
title: "Inner Property (ISwDMDimXpertSphereFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertSphereFeature"
member: "Inner"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature~Inner.html"
---

# Inner Property (ISwDMDimXpertSphereFeature)

Gets whether this DimXpert sphere is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertSphereFeature
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

True if the sphere is a hole; false if it's a pin

## VBA Syntax

See [SwDMDimXpertSphereFeature::Inner](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertSphereFeature~Inner.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.html)
[ISwDMDimXpertSphereFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
