---
title: "Datum Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "Datum"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~Datum.html"
---

# Datum Property (IPMIGtolFrameDatum)

Gets the Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Datum As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.String

instance.Datum = value

value = instance.Datum
```

### C#

```csharp
System.string Datum {get; set;}
```

### C++/CLI

```cpp
property System.String^ Datum {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gtol frame datum

## VBA Syntax

See [PMIGtolFrameDatum::Datum](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~Datum.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

In the Geometric Tolerance Properties dialog, you can specify up to two datums linked to the Primary, Secondary, and Tertiary datums. Click the drop-down selector next to each datum field to pop up a linked datum dialog where you can specify the linked datums and their material modifiers.

This property gets the primary, secondary, or tertiary datum. Use [IPMIGtolFrameDatum::DatumLinked1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked1.html) and [IPMIGtolFrameDatum::DatumLinked2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked2.html) to get the datums linked to this datum.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
