---
title: "Angle Property (ISwDMDimXpertChamferFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertChamferFeature"
member: "Angle"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature~Angle.html"
---

# Angle Property (ISwDMDimXpertChamferFeature)

Gets the angle of this DimXpert chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertChamferFeature
Dim value As System.Double

value = instance.Angle
```

### C#

```csharp
System.double Angle {get;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
}
```

### Property Value

Angle of the chamfer in radians

## VBA Syntax

See [SwDMDimXpertChamferFeature::Angle](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertChamferFeature~Angle.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.html)
[ISwDMDimXpertChamferFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
