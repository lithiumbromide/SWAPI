---
title: "DatumLinked2 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinked2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked2.html"
---

# DatumLinked2 Property (IPMIGtolFrameDatum)

Gets the second linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinked2 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.String

instance.DatumLinked2 = value

value = instance.DatumLinked2
```

### C#

```csharp
System.string DatumLinked2 {get; set;}
```

### C++/CLI

```cpp
property System.String^ DatumLinked2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second linked datum

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinked2](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinked2.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
