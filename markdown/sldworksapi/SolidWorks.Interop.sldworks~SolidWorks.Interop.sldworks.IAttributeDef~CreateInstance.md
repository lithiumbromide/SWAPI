---
title: "CreateInstance Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "CreateInstance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance.html"
---

# CreateInstance Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInstance( _
   ByVal OwnerDoc As System.Object, _
   ByVal OwnerEntity As System.Object, _
   ByVal NameIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As System.Object
Dim OwnerEntity As System.Object
Dim NameIn As System.String
Dim value As System.Object

value = instance.CreateInstance(OwnerDoc, OwnerEntity, NameIn)
```

### C#

```csharp
System.object CreateInstance(
   System.object OwnerDoc,
   System.object OwnerEntity,
   System.string NameIn
)
```

### C++/CLI

```cpp
System.Object^ CreateInstance(
   System.Object^ OwnerDoc,
   System.Object^ OwnerEntity,
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`:
- `OwnerEntity`:
- `NameIn`:

## VBA Syntax

See [AttributeDef::CreateInstance](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~CreateInstance.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
