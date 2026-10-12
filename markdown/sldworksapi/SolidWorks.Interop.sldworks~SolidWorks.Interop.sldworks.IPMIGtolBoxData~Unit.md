---
title: "Unit Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "Unit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.html"
---

# Unit Property (IPMIGtolBoxData)

Gets the units of tolerance for this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Units of tolerance as defined in [swPMIUnit_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIUnit_e.html)

## VBA Syntax

See [PMIGtolBoxData::Unit](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~Unit.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::TolerancePerUnitValue1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.html)
**IPMIGtolBoxData::TolerancePerUnitValue1Precision Property ()**
[IPMIGtolBoxData::TolerancePerUnitValue2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.html)
**IPMIGtolBoxData::TolerancePerUnitValue2Precision Property ()**
[IPMIGtolBoxData::TolValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.html)
**IPMIGtolBoxData::TolValuePrecision Property ()**
[IPMIGtolBoxData::GetTolTypeValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues.html)
**IPMIGtolBoxData::GetTolTypeValuesPrecision Method ()**

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
