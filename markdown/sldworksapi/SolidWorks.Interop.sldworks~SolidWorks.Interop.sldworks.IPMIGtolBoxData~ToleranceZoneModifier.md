---
title: "ToleranceZoneModifier Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "ToleranceZoneModifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~ToleranceZoneModifier.html"
---

# ToleranceZoneModifier Property (IPMIGtolBoxData)

Gets the tolerance zone modifier in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceZoneModifier As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Integer

instance.ToleranceZoneModifier = value

value = instance.ToleranceZoneModifier
```

### C#

```csharp
System.int ToleranceZoneModifier {get; set;}
```

### C++/CLI

```cpp
property System.int ToleranceZoneModifier {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance zone modifier as defined in [swToleranceZoneModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToleranceZoneModifier_e.html)

## VBA Syntax

See [PMIGtolBoxData::ToleranceZoneModifier](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~ToleranceZoneModifier.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
