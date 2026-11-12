---
title: "DatumLinked1 Property (IPMIGtolFrameDatum)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolFrameDatum"
member: "DatumLinked1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked1.html"
---

# DatumLinked1 Property (IPMIGtolFrameDatum)

Gets the first linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLinked1 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolFrameDatum
Dim value As System.String

instance.DatumLinked1 = value

value = instance.DatumLinked1
```

### C#

```csharp
System.string DatumLinked1 {get; set;}
```

### C++/CLI

```cpp
property System.String^ DatumLinked1 {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

First linked datum

## VBA Syntax

See [PMIGtolFrameDatum::DatumLinked1](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolFrameDatum~DatumLinked1.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.html)
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
