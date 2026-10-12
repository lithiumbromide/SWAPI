---
title: "IComponentReload2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IComponentReload2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IComponentReload2.html"
---

# IComponentReload2 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::ReplaceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ReplaceComponents.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IComponentReload2( _
   ByVal Component As Component, _
   ByVal ReadOnly As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Component As Component
Dim ReadOnly As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer

value = instance.IComponentReload2(Component, ReadOnly, Options)
```

### C#

```csharp
System.int IComponentReload2(
   Component Component,
   System.bool ReadOnly,
   System.int Options
)
```

### C++/CLI

```cpp
System.int IComponentReload2(
   Component^ Component,
   System.bool ReadOnly,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`:
- `ReadOnly`:
- `Options`:

## VBA Syntax

See [AssemblyDoc::IComponentReload2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IComponentReload2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
