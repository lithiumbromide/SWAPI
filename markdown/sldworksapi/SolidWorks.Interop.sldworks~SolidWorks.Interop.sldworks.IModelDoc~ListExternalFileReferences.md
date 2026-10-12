---
title: "ListExternalFileReferences Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ListExternalFileReferences.html"
---

# ListExternalFileReferences Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ListExternalFileReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ListExternalFileReferences.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferences( _
   ByVal UseSearchRules As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UseSearchRules As System.Boolean
Dim value As System.Object

value = instance.ListExternalFileReferences(UseSearchRules)
```

### C#

```csharp
System.object ListExternalFileReferences(
   System.bool UseSearchRules
)
```

### C++/CLI

```cpp
System.Object^ ListExternalFileReferences(
   System.bool UseSearchRules
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseSearchRules`:

## VBA Syntax

See [ModelDoc::ListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ListExternalFileReferences.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
