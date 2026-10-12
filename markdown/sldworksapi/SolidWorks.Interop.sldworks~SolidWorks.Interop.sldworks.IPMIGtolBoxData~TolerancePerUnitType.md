---
title: "TolerancePerUnitType Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "TolerancePerUnitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitType.html"
---

# TolerancePerUnitType Property (IPMIGtolBoxData)

Gets the tolerance per unit area type in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolerancePerUnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Integer

instance.TolerancePerUnitType = value

value = instance.TolerancePerUnitType
```

### C#

```csharp
System.int TolerancePerUnitType {get; set;}
```

### C++/CLI

```cpp
property System.int TolerancePerUnitType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance per unit area type as defined in [swPMITolPerUnitAreaType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMITolPerUnitAreaType_e.html)

## VBA Syntax

See [PMIGtolBoxData::TolerancePerUnitType](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~TolerancePerUnitType.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This property is valid only if [IPMIFrameData::GeometricCharacteristic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic.html) returns [swGeometricCharacteristic_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html):

- swGeometricCharacteristic_Flatness
- swGeometricCharacteristic_Straightness

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::TolerancePerUnitValue1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.html)
**IPMIGtolBoxData::TolerancePerUnitValue1Precision Property ()**
[IPMIGtolBoxData::TolerancePerUnitValue2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.html)
**IPMIGtolBoxData::TolerancePerUnitValue2Precision Property ()**
[IPMIGtolBoxData::TolValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.html)
**IPMIGtolBoxData::TolValuePrecision Property ()**

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
