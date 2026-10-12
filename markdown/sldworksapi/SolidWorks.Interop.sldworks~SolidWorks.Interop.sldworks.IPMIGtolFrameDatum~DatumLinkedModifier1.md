---
title: "DatumLinkedModifier1 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinkedModifier1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier1.html"
---

# DatumLinkedModifier1 Property (IPMIGtolFrameDatum)

Gets the modifier of the first linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinkedModifier1 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.Integer

instance.DatumLinkedModifier1 = value

value = instance.DatumLinkedModifier1
```

### C#

```csharp
System.int DatumLinkedModifier1 {get; set;}
```

### C++/CLI

```cpp
property System.int DatumLinkedModifier1 {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[First linked datum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked1.html) material modifier as defined in [swMaterialModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html)

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinkedModifier1](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinkedModifier1.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIGtolFrameDatum::DatumLinkedModifierValue1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue1.html) to get this linked datum's modifier value, if one exists.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
