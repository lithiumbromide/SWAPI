---
title: "ChamferDistance Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "ChamferDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ChamferDistance.html"
---

# ChamferDistance Property (IEndCapFeatureData)

Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ChamferDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Double

instance.ChamferDistance = value

value = instance.ChamferDistance
```

### C#

```csharp
System.double ChamferDistance {get; set;}
```

### C++/CLI

```cpp
property System.double ChamferDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Chamfer distance if [IEndCapFeatureData::UseChamferCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~UseChamferCorners.html) is true; fillet radius if IEndCapFeatureData::UseChamferCorners is false

## VBA Syntax

See [EndCapFeatureData::ChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~ChamferDistance.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## Remarks

This property is valid only if [IEndCapFeatureData::UseCornerTreatment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~UseCornerTreatment.html) is true.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
