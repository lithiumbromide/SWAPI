---
title: "TolValue Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "TolValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.html"
---

# TolValue Property (IPMIGtolBoxData)

Gets the tolerance value in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Double

instance.TolValue = value

value = instance.TolValue
```

### C#

```csharp
System.double TolValue {get; set;}
```

### C++/CLI

```cpp
property System.double TolValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance value

## VBA Syntax

See [PMIGtolBoxData::TolValue](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~TolValue.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.html)
[IPMIGtolBoxData::TolerancePerUnitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitType.html)
[IPMIGtolBoxData::TolerancePerUnitValue1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.html)
[IPMIGtolBoxData::TolerancePerUnitValue2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
