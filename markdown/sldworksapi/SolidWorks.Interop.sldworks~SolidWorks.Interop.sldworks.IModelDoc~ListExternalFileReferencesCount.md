---
title: "ListExternalFileReferencesCount Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ListExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ListExternalFileReferencesCount.html"
---

# ListExternalFileReferencesCount Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ListExternalFileReferencesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferencesCount( _
   ByVal UseSearchRules As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UseSearchRules As System.Boolean
Dim value As System.Integer

value = instance.ListExternalFileReferencesCount(UseSearchRules)
```

### C#

```csharp
System.int ListExternalFileReferencesCount(
   System.bool UseSearchRules
)
```

### C++/CLI

```cpp
System.int ListExternalFileReferencesCount(
   System.bool UseSearchRules
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseSearchRules`:

## VBA Syntax

See [ModelDoc::ListExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ListExternalFileReferencesCount.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
