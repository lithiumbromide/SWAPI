---
title: "MateEntityType Property (IMateInPlace)"
project: "SOLIDWORKS API Help"
interface: "IMateInPlace"
member: "MateEntityType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntityType.html"
---

# MateEntityType Property (IMateInPlace)

Gets the type of entity in this Inplace mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MateEntityType( _
   ByVal NIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.Integer

value = instance.MateEntityType(NIndex)
```

### C#

```csharp
System.int MateEntityType(
   System.int NIndex
) {get;}
```

### C++/CLI

```cpp
property System.int MateEntityType {
   System.int get(System.int NIndex);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NIndex`: 0-based index associated with this entity

### Property Value

Type of entity as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [MateInPlace::MateEntityType](ms-its:sldworksapivb6.chm::/sldworks~MateInPlace~MateEntityType.html).

## Examples

[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (VBA)](Get_Mates_Example_VB.htm)

## Remarks

To get the name of the entity, call [IMateInPlace::MateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateInPlace~MateEntity.html).

## See Also

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.html)
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
