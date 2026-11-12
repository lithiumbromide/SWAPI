---
title: "Inner Property (IDimXpertCompoundWidthFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundWidthFeature"
member: "Inner"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature~Inner.html"
---

# Inner Property (IDimXpertCompoundWidthFeature)

Gets whether the width is for a hole or a pin.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Inner As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundWidthFeature
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

True if width is for a hole; false if for a pin

## VBA Syntax

See [DimXpertCompoundWidthFeature::Inner](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundWidthFeature~Inner.html).

## Examples

[Get and Set Size Dimension Example (C#)](Get_and_Set_Size_Dimension_Example_CSharp.htm)
[Get and Set Size Dimension Example (VB.NET)](Get_and_Set_Size_Dimension_Example_VBNET.htm)
[Get and Set Size Dimension Example (VBA)](Get_and_Set_Size_Dimension_Example_VB.htm)
[Get DimXpert Width And Best Fit Plane Features Example (VBA)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VB.htm)
[Get DimXpert Width And Best Fit Plane Features Example (VB.NET)](Get_DimXpert_Width_And_BestFitPlane_Features_Example_VBNET.htm)

## See Also

[IDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature.html)
[IDimXpertCompoundWidthFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundWidthFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
