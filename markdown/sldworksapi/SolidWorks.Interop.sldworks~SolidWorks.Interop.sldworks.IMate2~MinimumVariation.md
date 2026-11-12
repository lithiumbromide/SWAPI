---
title: "MinimumVariation Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "MinimumVariation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation.html"
---

# MinimumVariation Property (IMate2)

Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MinimumVariation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Double

value = instance.MinimumVariation
```

### C#

```csharp
System.double MinimumVariation {get;}
```

### C++/CLI

```cpp
property System.double MinimumVariation {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum variation for the dimension of this mate

## VBA Syntax

See [Mate2::MinimumVariation](ms-its:sldworksapivb6.chm::/sldworks~Mate2~MinimumVariation.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)

## Remarks

This property is valid only for [IMate2::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~Type.html):

- swMateType_e.swMateANGLE

- or -

- swMateType_e.swMateDISTANCE

For distance and angle mates:

`Minimum_variation` = `minimum_value - dimension_value`

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::DisplayDimension2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.html)
[IMate2::MaximumVariation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
