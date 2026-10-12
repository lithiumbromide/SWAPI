---
title: "IComponentReload3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IComponentReload3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IComponentReload3.html"
---

# IComponentReload3 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::ReplaceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ReplaceComponents.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IComponentReload3( _
   ByVal Component As Component2, _
   ByVal ReadOnly As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Component As Component2
Dim ReadOnly As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer

value = instance.IComponentReload3(Component, ReadOnly, Options)
```

### C#

```csharp
System.int IComponentReload3(
   Component2 Component,
   System.bool ReadOnly,
   System.int Options
)
```

### C++/CLI

```cpp
System.int IComponentReload3(
   Component2^ Component,
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

See [AssemblyDoc::IComponentReload3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IComponentReload3.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
