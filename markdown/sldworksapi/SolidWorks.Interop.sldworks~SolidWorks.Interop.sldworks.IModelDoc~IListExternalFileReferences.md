---
title: "IListExternalFileReferences Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IListExternalFileReferences.html"
---

# IListExternalFileReferences Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IListExternalFileReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IListExternalFileReferences.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IListExternalFileReferences( _
   ByVal UseSearchRules As System.Boolean, _
   ByVal NumRefs As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UseSearchRules As System.Boolean
Dim NumRefs As System.Integer
Dim value As System.String

value = instance.IListExternalFileReferences(UseSearchRules, NumRefs)
```

### C#

```csharp
System.string IListExternalFileReferences(
   System.bool UseSearchRules,
   System.int NumRefs
)
```

### C++/CLI

```cpp
System.String^ IListExternalFileReferences(
   System.bool UseSearchRules,
   System.int NumRefs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseSearchRules`:
- `NumRefs`:

## VBA Syntax

See [ModelDoc::IListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IListExternalFileReferences.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
