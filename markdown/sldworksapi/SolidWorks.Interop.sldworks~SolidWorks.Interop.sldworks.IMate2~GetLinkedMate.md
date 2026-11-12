---
title: "GetLinkedMate Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "GetLinkedMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetLinkedMate.html"
---

# GetLinkedMate Method (IMate2)

Gets the linked mate of this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkedMate() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Object

value = instance.GetLinkedMate()
```

### C#

```csharp
System.object GetLinkedMate()
```

### C++/CLI

```cpp
System.Object^ GetLinkedMate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [Mate2::GetLinkedMate](ms-its:sldworksapivb6.chm::/sldworks~Mate2~GetLinkedMate.html).

## Remarks

This mate and its linked mate are siblings in a Hole Set, which is defined as two concentric mates between the same two components.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
