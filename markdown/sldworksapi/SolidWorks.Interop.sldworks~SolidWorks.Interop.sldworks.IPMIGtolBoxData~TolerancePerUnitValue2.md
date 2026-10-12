---
title: "TolerancePerUnitValue2 Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "TolerancePerUnitValue2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.html"
---

# TolerancePerUnitValue2 Property (IPMIGtolBoxData)

Gets the tolerance 2 per unit area in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolerancePerUnitValue2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Double

instance.TolerancePerUnitValue2 = value

value = instance.TolerancePerUnitValue2
```

### C#

```csharp
System.double TolerancePerUnitValue2 {get; set;}
```

### C++/CLI

```cpp
property System.double TolerancePerUnitValue2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance 2 per unit area

## VBA Syntax

See [PMIGtolBoxData::TolerancePerUnitValue2](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~TolerancePerUnitValue2.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This property is valid only if:

- [IPMIFrameData::GeometricCharacteristic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic.html) returns [swGeometricCharacteristic_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html)

  - swGeometricCharacteristic_Flatness
  - swGeometricCharacteristic_Straightness
- [IPMIGtolBoxData::TolerancePerUnitType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitType.html) returns [swPMITolPerUnitAreaType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMITolPerUnitAreaType_e.html).swPMITolPerUnitType_Rectangular.

If IPMIGtolBoxData::TolerancePerUnitType returns swPMITolPerUnitAreaType_e.swPMITolPerUnitType_Rectangular, use this property and [IPMIGtolBoxData::TolerancePerUnitValue1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.html) to calculate the unit area value. Then divide [IPMIGtolBoxData::TolValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.html) by the unit area value to get the tolerance per unit area value.

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
