---
title: "Inner Property (IDimXpertConeFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertConeFeature"
member: "Inner"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature~Inner.html"
---

# Inner Property (IDimXpertConeFeature)

Gets whether the DimXpert cone is a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertConeFeature
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

True if cone is a hole; false if a pin

## VBA Syntax

See [DimXpertConeFeature::Inner](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertConeFeature~Inner.html).

## Examples

[Get DimXpert Cone Feature Example (VBA)](Get_DimXpert_Cone_Feature_Example_VB.htm)
[Get DimXpert Cone Feature Example (VB.NET)](Get_DimXpert_Cone_Feature_Example_VBNET.htm)

## See Also

[IDimXpertConeFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature.html)
[IDimXpertConeFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertConeFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
