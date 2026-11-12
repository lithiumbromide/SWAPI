---
title: "SetMaterialPropertyName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetMaterialPropertyName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName.html"
---

# SetMaterialPropertyName Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::SetMaterialPropertyName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialPropertyName( _
   ByVal Database As System.String, _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Database As System.String
Dim Name As System.String

instance.SetMaterialPropertyName(Database, Name)
```

### C#

```csharp
void SetMaterialPropertyName(
   System.string Database,
   System.string Name
)
```

### C++/CLI

```cpp
void SetMaterialPropertyName(
   System.String^ Database,
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Database`:
- `Name`:

## VBA Syntax

See [PartDoc::SetMaterialPropertyName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetMaterialPropertyName.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
