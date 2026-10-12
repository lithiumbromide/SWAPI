---
title: "GetMateEntityCount Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetMateEntityCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMateEntityCount.html"
---

# GetMateEntityCount Method (IMate2)

Gets the number of entities for this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMateEntityCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
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

Number of entities for this mate

## VBA Syntax

See [Mate2::GetMateEntityCount](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetMateEntityCount.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)

## Remarks

Call this method before calling [IMate2::MateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~MateEntity.html) to get the number of entities in the mate.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
