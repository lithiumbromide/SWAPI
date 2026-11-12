---
title: "DisplayDimension2 Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "DisplayDimension2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.html"
---

# DisplayDimension2 Property (IMate2)

Gets the specified display dimension for this mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DisplayDimension2( _
   ByVal Index As System.Integer _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Index As System.Integer
Dim value As DisplayDimension

value = instance.DisplayDimension2(Index)
```

### C#

```csharp
DisplayDimension DisplayDimension2(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property DisplayDimension^ DisplayDimension2 {
   DisplayDimension^ get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Number indicating which mate's display dimension to get (see **Remarks**)

### Property Value

[Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) for the specified mate

## VBA Syntax

See [Mate2::DisplayDimension2](ms-its:sldworksapivb6.chm::/sldworks~Mate2~DisplayDimension2.html).

## Examples

[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)
[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)

## Remarks

This property returns the first display dimension for all types of mates and the second display dimension for gear mates only.

A gear mate has two feature dimensions whose values form the gear ratio. All other mates return NULL/Nothing for the second display dimension.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::MaximumVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.html)
[IMate2::MinimumVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
