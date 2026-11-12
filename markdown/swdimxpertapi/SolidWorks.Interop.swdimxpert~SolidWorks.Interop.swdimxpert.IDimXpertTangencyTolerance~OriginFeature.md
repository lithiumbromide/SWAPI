---
title: "OriginFeature Property (IDimXpertTangencyTolerance)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertTangencyTolerance"
member: "OriginFeature"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTangencyTolerance~OriginFeature.html"
---

# OriginFeature Property (IDimXpertTangencyTolerance)

Gets the DimXpert feature of origin for this DimXpert tangency tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OriginFeature As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertTangencyTolerance
Dim value As DimXpertFeature

value = instance.OriginFeature
```

### C#

```csharp
DimXpertFeature OriginFeature {get;}
```

### C++/CLI

```cpp
property DimXpertFeature^ OriginFeature {
   DimXpertFeature^ get();
}
```

### Property Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertTangencyTolerance::OriginFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertTangencyTolerance~OriginFeature.html).

## Examples

[Get DimXpert Tolerance6 Example (VBA)](Get_DimXpert_Tolerance6_Example_VB.htm)
[Get DimXpert Tolerance6 Example (VB.NET)](Get_DimXpert_Tolerance6_Example_VBNET.htm)
[Get DimXpert Features and Annotations in a Model Example (C#)](Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm)

## See Also

[IDimXpertTangencyTolerance Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTangencyTolerance.html)
[IDimXpertTangencyTolerance Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertTangencyTolerance_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
