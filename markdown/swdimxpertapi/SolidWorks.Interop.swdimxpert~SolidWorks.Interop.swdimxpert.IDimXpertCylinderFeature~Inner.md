---
title: "Inner Property (IDimXpertCylinderFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCylinderFeature"
member: "Inner"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature~Inner.html"
---

# Inner Property (IDimXpertCylinderFeature)

Gets whether this DimXpert cylinder is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCylinderFeature
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

True if cylinder is a hole; false if a pin

## VBA Syntax

See [DimXpertCylinderFeature::Inner](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCylinderFeature~Inner.html).

## See Also

[IDimXpertCylinderFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature.html)
[IDimXpertCylinderFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCylinderFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
