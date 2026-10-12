---
title: "ICreateInstance4 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "ICreateInstance4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance4.html"
---

# ICreateInstance4 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateInstance4( _
   ByVal OwnerDoc As ModelDoc2, _
   ByVal OwnerComp As Component2, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc2
Dim OwnerComp As Component2
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute

value = instance.ICreateInstance4(OwnerDoc, OwnerComp, OwnerEntity, NameIn, Options, ConfigurationOption)
```

### C#

```csharp
Attribute ICreateInstance4(
   ModelDoc2 OwnerDoc,
   Component2 OwnerComp,
   Entity OwnerEntity,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

### C++/CLI

```cpp
Attribute^ ICreateInstance4(
   ModelDoc2^ OwnerDoc,
   Component2^ OwnerComp,
   Entity^ OwnerEntity,
   System.String^ NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`:
- `OwnerComp`:
- `OwnerEntity`:
- `NameIn`:
- `Options`:
- `ConfigurationOption`:

## VBA Syntax

See [AttributeDef::ICreateInstance4](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~ICreateInstance4.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
