---
title: "SolidFill Property (IWeldBead)"
project: "SOLIDWORKS API Help"
interface: "IWeldBead"
member: "SolidFill"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~SolidFill.html"
---

# SolidFill Property (IWeldBead)

Gets or sets whether to fill the weld bead annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidFill As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldBead
Dim value As System.Boolean

instance.SolidFill = value

value = instance.SolidFill
```

### C#

```csharp
System.bool SolidFill {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidFill {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to fill the weld bead, false to not (see **Remarks**)

## VBA Syntax

See [WeldBead::SolidFill](ms-its:sldworksapivb6.chm::/sldworks~WeldBead~SolidFill.html).

## Examples

See the [IWeldBead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html) examples.

## Remarks

To get the triangular-shaped weld treatment, use the polygon-related [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) APIs, which provide you with the geometry information. See the example for more information.

## See Also

[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IWeldBead Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead_members.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
