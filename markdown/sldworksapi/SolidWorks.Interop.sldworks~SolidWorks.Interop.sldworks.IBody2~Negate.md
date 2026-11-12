---
title: "Negate Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Negate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Negate.html"
---

# Negate Method (IBody2)

Reverses the direction (i.e., orientation) of the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function Negate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.Negate()
```

### C#

```csharp
System.bool Negate()
```

### C++/CLI

```cpp
System.bool Negate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the direction of the body is reversed, false if not

## VBA Syntax

See [Body2::Negate](ms-its:sldworksapivb6.chm::/sldworks~Body2~Negate.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14
