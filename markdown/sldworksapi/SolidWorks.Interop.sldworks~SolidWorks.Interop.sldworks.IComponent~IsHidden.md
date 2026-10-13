---
title: "IsHidden Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "IsHidden"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~IsHidden.html"
---

# IsHidden Method (IComponent)

Obsolete. Superseded by [IComponent2::IsHidden](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IsHidden.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHidden( _
   ByVal ConsiderSuppressed As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim ConsiderSuppressed As System.Boolean
Dim value As System.Boolean

value = instance.IsHidden(ConsiderSuppressed)
```

### C#

```csharp
System.bool IsHidden(
   System.bool ConsiderSuppressed
)
```

### C++/CLI

```cpp
System.bool IsHidden(
   System.bool ConsiderSuppressed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConsiderSuppressed`:

## VBA Syntax

See [Component::IsHidden](ms-its:sldworksapivb6.chm::/sldworks~Component~IsHidden.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
