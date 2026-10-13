---
title: "CompConfigProperties Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CompConfigProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties.html"
---

# CompConfigProperties Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CompConfigProperties( _
   ByVal M_suppressed As System.Boolean, _
   ByVal M_show_component As System.Boolean, _
   ByVal M_fdetail As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim M_suppressed As System.Boolean
Dim M_show_component As System.Boolean
Dim M_fdetail As System.Boolean

instance.CompConfigProperties(M_suppressed, M_show_component, M_fdetail)
```

### C#

```csharp
void CompConfigProperties(
   System.bool M_suppressed,
   System.bool M_show_component,
   System.bool M_fdetail
)
```

### C++/CLI

```cpp
void CompConfigProperties(
   System.bool M_suppressed,
   System.bool M_show_component,
   System.bool M_fdetail
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `M_suppressed`:
- `M_show_component`:
- `M_fdetail`:

## VBA Syntax

See [AssemblyDoc::CompConfigProperties](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CompConfigProperties.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
