---
title: "InsertBendTableOpen Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertBendTableOpen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertBendTableOpen.html"
---

# InsertBendTableOpen Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertBendTableOpen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertBendTableOpen.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTableOpen( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertBendTableOpen(FileName)
```

### C#

```csharp
System.bool InsertBendTableOpen(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertBendTableOpen(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [ModelDoc::InsertBendTableOpen](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertBendTableOpen.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
