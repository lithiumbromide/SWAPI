---
title: "Select Method (IComponent)"
project: "SOLIDWORKS API Help"
interface: "IComponent"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~Select.html"
---

# Select Method (IComponent)

Obsolete. Superseded by [IComponent2::Select3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Select3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.Select(AppendFlag)
```

### C#

```csharp
System.bool Select(
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`:

## VBA Syntax

See [Component::Select](ms-its:sldworksapivb6.chm::/sldworks~Component~Select.html).

## See Also

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.html)
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.html)
