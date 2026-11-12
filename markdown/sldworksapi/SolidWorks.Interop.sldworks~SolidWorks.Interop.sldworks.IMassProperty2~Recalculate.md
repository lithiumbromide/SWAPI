---
title: "Recalculate Method (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "Recalculate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html"
---

# Recalculate Method (IMassProperty2)

Recalculates the mass properties of the selectied bodies/components.

## Syntax

### Visual Basic (Declaration)

```vb
Function Recalculate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Boolean

value = instance.Recalculate()
```

### C#

```csharp
System.bool Recalculate()
```

### C++/CLI

```cpp
System.bool Recalculate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if recalculation is successful, false if not

## VBA Syntax

See [MassProperty2::Recalculate](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~Recalculate.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

Call this method after overriding mass properties (center of mass, mass, moments of inertia, principal axes orientation, or principal moments of inertia) or resetting [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html).

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
