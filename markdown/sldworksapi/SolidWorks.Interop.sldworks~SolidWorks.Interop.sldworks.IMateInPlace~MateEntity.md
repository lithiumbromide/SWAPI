---
title: "MateEntity Property (IMateInPlace)"
project: "SOLIDWORKS API Help"
interface: "IMateInPlace"
member: "MateEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntity.html"
---

# MateEntity Property (IMateInPlace)

Gets the name of the mated entity associated with the specified index for this Inplace mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MateEntity( _
   ByVal NIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.Object

value = instance.MateEntity(NIndex)
```

### C#

```csharp
System.object MateEntity(
   System.int NIndex
) {get;}
```

### C++/CLI

```cpp
property System.Object^ MateEntity {
   System.Object^ get(System.int NIndex);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NIndex`: 0-based index associated with this entity

### Property Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [MateInPlace::MateEntity](ms-its:sldworksapivb6.chm::/sldworks~MateInPlace~MateEntity.html).

## Remarks

To get the type of entity returned by this method, call [IMateInPlace::MateEntityType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateInPlace~MateEntityType.html) .

## See Also

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.html)
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
