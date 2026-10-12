---
title: "ICreateInstance3 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "ICreateInstance3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~ICreateInstance3.html"
---

# ICreateInstance3 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateInstance3( _
   ByVal OwnerDoc As ModelDoc, _
   ByVal OwnerComp As Component, _
   ByVal OwnerEntity As Entity, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc
Dim OwnerComp As Component
Dim OwnerEntity As Entity
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute

value = instance.ICreateInstance3(OwnerDoc, OwnerComp, OwnerEntity, NameIn, Options, ConfigurationOption)
```

### C#

```csharp
Attribute ICreateInstance3(
   ModelDoc OwnerDoc,
   Component OwnerComp,
   Entity OwnerEntity,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

### C++/CLI

```cpp
Attribute^ ICreateInstance3(
   ModelDoc^ OwnerDoc,
   Component^ OwnerComp,
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

See [AttributeDef::ICreateInstance3](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~ICreateInstance3.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
