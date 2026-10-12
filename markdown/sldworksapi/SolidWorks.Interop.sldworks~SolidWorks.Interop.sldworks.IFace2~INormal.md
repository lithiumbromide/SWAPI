---
title: "INormal Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "INormal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~INormal.html"
---

# INormal Property (IFace2)

Gets the unit normal vector for any planar face.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property INormal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Double

instance.INormal = value

value = instance.INormal
```

### C#

```csharp
System.double INormal {get; set;}
```

### C++/CLI

```cpp
property System.double INormal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to an array of 3 doubles (i,j,k)

## VBA Syntax

See [Face2::INormal](ms-its:sldworksapivb6.chm::/sldworks~Face2~INormal.html).

## Remarks

This property is read-only.

If the face is not a planar face, then this property returns 0,0,0.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::Normal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
