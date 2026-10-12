---
title: "Reattach Method (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "Reattach"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~Reattach.html"
---

# Reattach Method (IDatumOrigin)

Attaches the datum origin to a different entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function Reattach() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As System.Boolean

value = instance.Reattach()
```

### C#

```csharp
System.bool Reattach()
```

### C++/CLI

```cpp
System.bool Reattach();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the datum origin is attached to a different entity, false if not

## VBA Syntax

See [DatumOrigin::Reattach](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~Reattach.html).

## Remarks

This method:

- Lets you manipulate the datum origin. It attaches the datum origin to the currently selected entity.
- Expects that only one entity (vertex, edge, or sketch point) is selected. That selected entity must be in the same view as the original entity to which the datum origin was attached.

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
