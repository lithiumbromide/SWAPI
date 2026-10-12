---
title: "CreateInstance3 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "CreateInstance3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance3.html"
---

# CreateInstance3 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInstance3( _
   ByVal OwnerDoc As System.Object, _
   ByVal OwnerComp As System.Object, _
   ByVal OwnerEntity As System.Object, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As System.Object
Dim OwnerComp As System.Object
Dim OwnerEntity As System.Object
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As System.Object

value = instance.CreateInstance3(OwnerDoc, OwnerComp, OwnerEntity, NameIn, Options, ConfigurationOption)
```

### C#

```csharp
System.object CreateInstance3(
   System.object OwnerDoc,
   System.object OwnerComp,
   System.object OwnerEntity,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

### C++/CLI

```cpp
System.Object^ CreateInstance3(
   System.Object^ OwnerDoc,
   System.Object^ OwnerComp,
   System.Object^ OwnerEntity,
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

See [AttributeDef::CreateInstance3](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~CreateInstance3.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
