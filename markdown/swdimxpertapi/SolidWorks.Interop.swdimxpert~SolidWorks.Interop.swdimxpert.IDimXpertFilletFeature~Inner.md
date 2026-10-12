---
title: "Inner Property (IDimXpertFilletFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFilletFeature"
member: "Inner"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature~Inner.html"
---

# Inner Property (IDimXpertFilletFeature)

Gets whether this DimXpert fillet is for a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFilletFeature
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

True if fillet is for a hole; false if for a pin

## VBA Syntax

See [DimXpertFilletFeature::Inner](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFilletFeature~Inner.html).

## See Also

[IDimXpertFilletFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature.html)
[IDimXpertFilletFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFilletFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
