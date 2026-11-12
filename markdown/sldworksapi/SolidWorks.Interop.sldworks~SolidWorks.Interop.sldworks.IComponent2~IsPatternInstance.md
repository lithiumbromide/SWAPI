---
title: "IsPatternInstance Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsPatternInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsPatternInstance.html"
---

# IsPatternInstance Method (IComponent2)

Gets whether the component is a member of a pattern instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsPatternInstance() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsPatternInstance()
```

### C#

```csharp
System.bool IsPatternInstance()
```

### C++/CLI

```cpp
System.bool IsPatternInstance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the component is a member of pattern instance, false if not

## VBA Syntax

See [Component2::IsPatternInstance](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsPatternInstance.html).

## Remarks

True if the component is a member of pattern instance, false if not

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
