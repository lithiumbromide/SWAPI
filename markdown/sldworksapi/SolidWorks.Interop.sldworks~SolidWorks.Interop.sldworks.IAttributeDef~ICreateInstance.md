---
title: "ICreateInstance Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "ICreateInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance.html"
---

# ICreateInstance Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateInstance( _
   ByVal OwnerDoc As ModelDoc, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim value As Attribute

value = instance.ICreateInstance(OwnerDoc, OwnerEntity, NameIn)
```

### C#

```csharp
Attribute ICreateInstance(
   ModelDoc OwnerDoc,
   Entity OwnerEntity,
   System.string NameIn
)
```

### C++/CLI

```cpp
Attribute^ ICreateInstance(
   ModelDoc^ OwnerDoc,
   Entity^ OwnerEntity,
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`:
- `OwnerEntity`:
- `NameIn`:

## VBA Syntax

See [AttributeDef::ICreateInstance](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~ICreateInstance.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
