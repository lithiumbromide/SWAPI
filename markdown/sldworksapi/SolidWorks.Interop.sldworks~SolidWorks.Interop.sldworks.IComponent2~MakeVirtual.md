---
title: "MakeVirtual Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "MakeVirtual"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html"
---

# MakeVirtual Method (IComponent2)

Obsolete. by Superseded by [IComponent2::MakeVirtual2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeVirtual() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.MakeVirtual()
```

### C#

```csharp
System.bool MakeVirtual()
```

### C++/CLI

```cpp
System.bool MakeVirtual();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is saved in an assembly, false if not

## VBA Syntax

See [Component2::MakeVirtual](ms-its:sldworksapivb6.chm::/sldworks~Component2~MakeVirtual.html).

## Remarks

This method breaks the link to the external component file. Existing references are ignored, and the component is renamed.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
