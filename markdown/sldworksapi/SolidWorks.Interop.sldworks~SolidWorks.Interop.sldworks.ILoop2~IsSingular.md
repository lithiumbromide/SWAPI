---
title: "IsSingular Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IsSingular"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsSingular.html"
---

# IsSingular Method (ILoop2)

Gets whether this loop is singular.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSingular() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Boolean

value = instance.IsSingular()
```

### C#

```csharp
System.bool IsSingular()
```

### C++/CLI

```cpp
System.bool IsSingular();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the loop is singular, false if not

## VBA Syntax

See [Loop2::IsSingular](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IsSingular.html).

## Examples

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Loops (VBA)](Get_Loops_Example_VB.htm)

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
