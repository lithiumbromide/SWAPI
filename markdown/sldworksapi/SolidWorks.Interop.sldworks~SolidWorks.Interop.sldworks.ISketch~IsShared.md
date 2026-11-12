---
title: "IsShared Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IsShared"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsShared.html"
---

# IsShared Method (ISketch)

Gets whether this sketch is used by more than one feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsShared() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.IsShared()
```

### C#

```csharp
System.bool IsShared()
```

### C++/CLI

```cpp
System.bool IsShared();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this sketch is used by more than one feature, false if not

## VBA Syntax

See [Sketch::IsShared](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IsShared.html).

## Examples

[Determine If Sketch Is Shared (VBA)](Determine_if_Sketch_is_Shared_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
