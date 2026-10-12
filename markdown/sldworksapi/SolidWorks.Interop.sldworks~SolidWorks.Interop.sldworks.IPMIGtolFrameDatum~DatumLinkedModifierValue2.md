---
title: "DatumLinkedModifierValue2 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinkedModifierValue2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue2.html"
---

# DatumLinkedModifierValue2 Property (IPMIGtolFrameDatum)

Gets the value of the modifier of the second linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinkedModifierValue2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.Double

instance.DatumLinkedModifierValue2 = value

value = instance.DatumLinkedModifierValue2
```

### C#

```csharp
System.double DatumLinkedModifierValue2 {get; set;}
```

### C++/CLI

```cpp
property System.double DatumLinkedModifierValue2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the [second linked datum modifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier2.html)

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinkedModifierValue2](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinkedModifierValue2.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
