---
title: "GetMateEntityCount Method (IMateInPlace)"
project: "SOLIDWORKS API Help"
interface: "IMateInPlace"
member: "GetMateEntityCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~GetMateEntityCount.html"
---

# GetMateEntityCount Method (IMateInPlace)

Gets the number of Inplace mated entities in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMateEntityCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateInPlace
Dim value As System.Integer

value = instance.GetMateEntityCount()
```

### C#

```csharp
System.int GetMateEntityCount()
```

### C++/CLI

```cpp
System.int GetMateEntityCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of Inplace mated entities

## VBA Syntax

See [MateInPlace::GetMateEntityCount](ms-its:sldworksapivb6.chm::/sldworks~MateInPlace~GetMateEntityCount.html).

## Examples

[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (VBA)](Get_Mates_Example_VB.htm)

## See Also

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.html)
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
