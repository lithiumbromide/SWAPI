---
title: "InsertFamilyTableOpen Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertFamilyTableOpen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertFamilyTableOpen.html"
---

# InsertFamilyTableOpen Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertFamilyTableOpen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertFamilyTableOpen.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFamilyTableOpen( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertFamilyTableOpen(FileName)
```

### C#

```csharp
System.bool InsertFamilyTableOpen(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertFamilyTableOpen(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [ModelDoc::InsertFamilyTableOpen](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertFamilyTableOpen.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
