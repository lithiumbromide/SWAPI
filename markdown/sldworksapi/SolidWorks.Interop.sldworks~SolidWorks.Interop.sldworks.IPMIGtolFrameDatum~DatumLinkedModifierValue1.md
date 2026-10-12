---
title: "DatumLinkedModifierValue1 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinkedModifierValue1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue1.html"
---

# DatumLinkedModifierValue1 Property (IPMIGtolFrameDatum)

Gets the value of the modifier of the first linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinkedModifierValue1 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.Double

instance.DatumLinkedModifierValue1 = value

value = instance.DatumLinkedModifierValue1
```

### C#

```csharp
System.double DatumLinkedModifierValue1 {get; set;}
```

### C++/CLI

```cpp
property System.double DatumLinkedModifierValue1 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the [first linked datum modifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier1.html)

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinkedModifierValue1](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinkedModifierValue1.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
