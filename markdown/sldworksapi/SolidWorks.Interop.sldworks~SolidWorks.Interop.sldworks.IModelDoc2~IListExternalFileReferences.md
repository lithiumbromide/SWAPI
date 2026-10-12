---
title: "IListExternalFileReferences Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IListExternalFileReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListExternalFileReferences.html"
---

# IListExternalFileReferences Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::ListExternalReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::IListExternalFileReferences](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IListExternalFileReferences.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
