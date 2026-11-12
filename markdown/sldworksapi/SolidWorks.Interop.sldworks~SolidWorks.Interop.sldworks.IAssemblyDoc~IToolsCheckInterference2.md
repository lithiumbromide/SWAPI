---
title: "IToolsCheckInterference2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IToolsCheckInterference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference2.html"
---

# IToolsCheckInterference2 Method (IAssemblyDoc)

Obsolete. See [IAssemblyDoc::IToolsCheckInterference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IToolsCheckInterference2( _
   ByVal NumComponents As System.Integer, _
   ByRef LpComponents As Component, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As Component
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object

instance.IToolsCheckInterference2(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

### C#

```csharp
void IToolsCheckInterference2(
   System.int NumComponents,
   ref Component LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

### C++/CLI

```cpp
void IToolsCheckInterference2(
   System.int NumComponents,
   Component^% LpComponents,
   System.bool CoincidentInterference,
   [Out] System.Object^ PComp,
   [Out] System.Object^ PFace
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumComponents`:
- `LpComponents`:
- `CoincidentInterference`:
- `PComp`:
- `PFace`:

## VBA Syntax

See [AssemblyDoc::IToolsCheckInterference2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IToolsCheckInterference2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
