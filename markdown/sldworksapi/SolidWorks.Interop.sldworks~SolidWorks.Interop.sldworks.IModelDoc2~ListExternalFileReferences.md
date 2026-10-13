---
title: "ListExternalFileReferences Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListExternalFileReferences.html"
---

# ListExternalFileReferences Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ListExternalReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ListExternalFileReferences( _
   ByVal UseSearchRules As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::ListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ListExternalFileReferences.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
