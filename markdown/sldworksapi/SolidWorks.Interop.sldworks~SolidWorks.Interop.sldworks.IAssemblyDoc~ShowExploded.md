---
title: "ShowExploded Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ShowExploded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded.html"
---

# ShowExploded Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::ShowExploded2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ShowExploded2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowExploded( _
   ByVal ShowIt As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ShowIt As System.Boolean
Dim value As System.Boolean

value = instance.ShowExploded(ShowIt)
```

### C#

```csharp
System.bool ShowExploded(
   System.bool ShowIt
)
```

### C++/CLI

```cpp
System.bool ShowExploded(
   System.bool ShowIt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowIt`: True if you want to show the existing exploded state for the current assembly configuration, false if you want to show the assembly in the collapsed state

### Return Value

True if successful in displaying the existing exploded assembly state, false if not

## VBA Syntax

See [AssemblyDoc::ShowExploded](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ShowExploded.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AutoExplode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode.html)
[ViewCollapseAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.html)
[ViewExplodeAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.html)
