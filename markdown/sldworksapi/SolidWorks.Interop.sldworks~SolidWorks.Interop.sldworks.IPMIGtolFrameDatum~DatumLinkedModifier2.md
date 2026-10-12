---
title: "DatumLinkedModifier2 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinkedModifier2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier2.html"
---

# DatumLinkedModifier2 Property (IPMIGtolFrameDatum)

Gets the modifier of the second linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinkedModifier2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.Integer

instance.DatumLinkedModifier2 = value

value = instance.DatumLinkedModifier2
```

### C#

```csharp
System.int DatumLinkedModifier2 {get; set;}
```

### C++/CLI

```cpp
property System.int DatumLinkedModifier2 {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Second linked datum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked2.html) material modifier as defined in [swMaterialModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html)

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinkedModifier2](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinkedModifier2.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIGtolFrameDatum::DatumLinkedModifierValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue2.html) to get this linked datum's modifier value, if one exists.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
