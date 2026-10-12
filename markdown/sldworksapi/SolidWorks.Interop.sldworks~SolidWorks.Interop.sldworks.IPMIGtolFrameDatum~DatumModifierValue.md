---
title: "DatumModifierValue Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumModifierValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumModifierValue.html"
---

# DatumModifierValue Property (IPMIGtolFrameDatum)

Gets the value of the material modifier of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumModifierValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.Double

instance.DatumModifierValue = value

value = instance.DatumModifierValue
```

### C#

```csharp
System.double DatumModifierValue {get; set;}
```

### C++/CLI

```cpp
property System.double DatumModifierValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the [datum modifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumModifier.html)

## VBA Syntax

See [PMIGtolFrameDatum::DatumModifierValue](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumModifierValue.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
