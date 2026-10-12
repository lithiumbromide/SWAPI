---
title: "ICreateInstance2 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "ICreateInstance2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance2.html"
---

# ICreateInstance2 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateInstance2( _
   ByVal OwnerDoc As ModelDoc, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim Options As System.Integer
Dim value As Attribute

value = instance.ICreateInstance2(OwnerDoc, OwnerEntity, NameIn, Options)
```

### C#

```csharp
Attribute ICreateInstance2(
   ModelDoc OwnerDoc,
   Entity OwnerEntity,
   System.string NameIn,
   System.int Options
)
```

### C++/CLI

```cpp
Attribute^ ICreateInstance2(
   ModelDoc^ OwnerDoc,
   Entity^ OwnerEntity,
   System.String^ NameIn,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`:
- `OwnerEntity`:
- `NameIn`:
- `Options`:

## VBA Syntax

See [AttributeDef::ICreateInstance2](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~ICreateInstance2.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
