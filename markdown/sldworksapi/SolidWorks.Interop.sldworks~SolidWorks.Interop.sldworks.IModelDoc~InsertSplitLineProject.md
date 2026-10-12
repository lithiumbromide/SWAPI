---
title: "InsertSplitLineProject Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertSplitLineProject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertSplitLineProject.html"
---

# InsertSplitLineProject Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertSplitLineProject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSplitLineProject.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSplitLineProject( _
   ByVal IsDirectional As System.Boolean, _
   ByVal FlipDir As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim IsDirectional As System.Boolean
Dim FlipDir As System.Boolean

instance.InsertSplitLineProject(IsDirectional, FlipDir)
```

### C#

```csharp
void InsertSplitLineProject(
   System.bool IsDirectional,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
void InsertSplitLineProject(
   System.bool IsDirectional,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsDirectional`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc::InsertSplitLineProject](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertSplitLineProject.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
