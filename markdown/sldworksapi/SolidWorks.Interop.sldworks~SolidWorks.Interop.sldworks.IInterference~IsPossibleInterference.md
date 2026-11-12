---
title: "IsPossibleInterference Property (IInterference)"
project: "SOLIDWORKS API Help"
interface: "IInterference"
member: "IsPossibleInterference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IsPossibleInterference.html"
---

# IsPossibleInterference Property (IInterference)

Gets whether this interference is a possible interference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsPossibleInterference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInterference
Dim value As System.Boolean

value = instance.IsPossibleInterference
```

### C#

```csharp
System.bool IsPossibleInterference {get;}
```

### C++/CLI

```cpp
property System.bool IsPossibleInterference {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this is a possible interference, false if not

## VBA Syntax

See [Interference::IsPossibleInterference](ms-its:sldworksapivb6.chm::/sldworks~Interference~IsPossibleInterference.html).

## See Also

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
