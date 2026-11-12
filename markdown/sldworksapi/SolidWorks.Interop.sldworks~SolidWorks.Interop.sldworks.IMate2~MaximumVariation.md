---
title: "MaximumVariation Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "MaximumVariation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.html"
---

# MaximumVariation Property (IMate2)

Gets the maximum variation, in meters or radians, for the dimension of this distance or angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MaximumVariation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Double

value = instance.MaximumVariation
```

### C#

```csharp
System.double MaximumVariation {get;}
```

### C++/CLI

```cpp
property System.double MaximumVariation {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum variation for the dimension of this mate

## VBA Syntax

See [Mate2::MaximumVariation](ms-its:sldworksapivb6.chm::/sldworks~Mate2~MaximumVariation.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)

## Remarks

This property is valid only for [IMate2::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~Type.html):

- swMateType_e.swMateANGLE

- or -

- swMateType_e.swMateDISTANCE

For distance and angle mates:

`Maximum_variation` = `maximum_value` - `dimension_value`

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::DisplayDimension2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.html)
[IMate2::MinimumVariation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
