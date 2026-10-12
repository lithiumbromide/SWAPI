---
title: "AngleType Property (ISwDMDimXpertChamferFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertChamferFeature"
member: "AngleType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~AngleType.html"
---

# AngleType Property (ISwDMDimXpertChamferFeature)

Gets the type of chamfer angle for this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AngleType As swDmDimXpertChamferAngleType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertChamferFeature
Dim value As swDmDimXpertChamferAngleType_e

value = instance.AngleType
```

### C#

```csharp
swDmDimXpertChamferAngleType_e AngleType {get;}
```

### C++/CLI

```cpp
property swDmDimXpertChamferAngleType_e AngleType {
   swDmDimXpertChamferAngleType_e get();
}
```

### Property Value

Type of chamfer angle as defined in [swDmDimXpertChamferAngleType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertChamferAngleType_e.html)

## VBA Syntax

See [SwDMDimXpertChamferFeature::AngleType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertChamferFeature~AngleType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.html)
[ISwDMDimXpertChamferFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
