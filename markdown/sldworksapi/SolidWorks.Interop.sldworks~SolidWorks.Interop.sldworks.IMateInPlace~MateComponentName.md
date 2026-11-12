---
title: "MateComponentName Property (IMateInPlace)"
project: "SOLIDWORKS API Help"
interface: "IMateInPlace"
member: "MateComponentName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateComponentName.html"
---

# MateComponentName Property (IMateInPlace)

Gets the name of the specified component for this **Inplace** mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MateComponentName( _
   ByVal NIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.String

value = instance.MateComponentName(NIndex)
```

### C#

```csharp
System.string MateComponentName(
   System.int NIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ MateComponentName {
   System.String^ get(System.int NIndex);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NIndex`: 0-based index associated with the specified component

### Property Value

Name of the specified component

## VBA Syntax

See [MateInPlace::MateComponentName](ms-its:sldworksapivb6.chm::/sldworks~MateInPlace~MateComponentName.html).

## Examples

[Get Component Names and Types for Inplace MAte (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (VBA)](Get_Mates_Example_VB.htm)

## See Also

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.html)
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
