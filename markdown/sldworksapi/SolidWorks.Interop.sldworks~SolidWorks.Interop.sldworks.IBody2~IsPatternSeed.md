---
title: "IsPatternSeed Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsPatternSeed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsPatternSeed.html"
---

# IsPatternSeed Method (IBody2)

Gets whether this body is the seed of a patterned body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsPatternSeed( _
   ByVal BodyDispIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim BodyDispIn As System.Object
Dim value As System.Boolean

value = instance.IsPatternSeed(BodyDispIn)
```

### C#

```csharp
System.bool IsPatternSeed(
   System.object BodyDispIn
)
```

### C++/CLI

```cpp
System.bool IsPatternSeed(
   System.Object^ BodyDispIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyDispIn`: Patterned body

### Return Value

True if this body is the seed of the patterned body, false if not

## VBA Syntax

See [Body2::IsPatternSeed](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsPatternSeed.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
