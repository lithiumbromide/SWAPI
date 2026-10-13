---
title: "Inner Property (IDimXpertSphereFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertSphereFeature"
member: "Inner"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature~Inner.html"
---

# Inner Property (IDimXpertSphereFeature)

Gets whether the sphere is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertSphereFeature
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

True if sphere is a hole; false if a pin

## VBA Syntax

See [DimXpertSphereFeature::Inner](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertSphereFeature~Inner.html).

## Examples

[Get DimXpert Sphere Feature Example (VBA)](Get_DimXpert_Sphere_Feature_Example_VB.htm)
[Get DimXpert Sphere Feature Example (VB.NET)](Get_DimXpert_Sphere_Feature_Example_VBNET.htm)

## See Also

[IDimXpertSphereFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature.html)
[IDimXpertSphereFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertSphereFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
