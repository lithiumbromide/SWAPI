---
title: "ReplaceReference Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ReplaceReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReplaceReference.html"
---

# ReplaceReference Method (IComponent2)

Obsolete. Superseded by [AssemblyDoc::ReplaceComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ReplaceComponents.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceReference( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim FileName As System.String
Dim value As System.Integer

value = instance.ReplaceReference(FileName)
```

### C#

```csharp
System.int ReplaceReference(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int ReplaceReference(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [Component2::ReplaceReference](ms-its:sldworksapivb6.chm::/sldworks~Component2~ReplaceReference.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
