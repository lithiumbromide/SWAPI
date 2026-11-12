---
title: "CreateInstance2 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "CreateInstance2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance2.html"
---

# CreateInstance2 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInstance2( _
   ByVal OwnerDoc As System.Object, _
   ByVal OwnerEntity As System.Object, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As System.Object
Dim OwnerEntity As System.Object
Dim NameIn As System.String
Dim Options As System.Integer
Dim value As System.Object

value = instance.CreateInstance2(OwnerDoc, OwnerEntity, NameIn, Options)
```

### C#

```csharp
System.object CreateInstance2(
   System.object OwnerDoc,
   System.object OwnerEntity,
   System.string NameIn,
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ CreateInstance2(
   System.Object^ OwnerDoc,
   System.Object^ OwnerEntity,
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

See [AttributeDef::CreateInstance2](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~CreateInstance2.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
