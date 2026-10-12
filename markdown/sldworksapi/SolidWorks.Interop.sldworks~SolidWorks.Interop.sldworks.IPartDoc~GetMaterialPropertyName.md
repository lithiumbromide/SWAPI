---
title: "GetMaterialPropertyName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetMaterialPropertyName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName.html"
---

# GetMaterialPropertyName Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::GetMaterialPropertyName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialPropertyName( _
   ByRef Database As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Database As System.String
Dim value As System.String

value = instance.GetMaterialPropertyName(Database)
```

### C#

```csharp
System.string GetMaterialPropertyName(
   out System.string Database
)
```

### C++/CLI

```cpp
System.String^ GetMaterialPropertyName(
   [Out] System.String^ Database
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Database`:

## VBA Syntax

See [PartDoc::GetMaterialPropertyName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetMaterialPropertyName.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
