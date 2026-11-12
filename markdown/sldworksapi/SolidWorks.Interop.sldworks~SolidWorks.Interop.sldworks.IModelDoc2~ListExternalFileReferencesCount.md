---
title: "ListExternalFileReferencesCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ListExternalFileReferencesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListExternalFileReferencesCount.html"
---

# ListExternalFileReferencesCount Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ListExternalFileReferenceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferencesCount( _
   ByVal UseSearchRules As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::ListExternalFileReferencesCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ListExternalFileReferencesCount.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
