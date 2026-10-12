---
title: "CreateInstance4 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "CreateInstance4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance4.html"
---

# CreateInstance4 Method (IAttributeDef)

Obsolete. Superseded by [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInstance4( _
   ByVal OwnerDoc As ModelDoc2, _
   ByVal OwnerObj As System.Object, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc2
Dim OwnerObj As System.Object
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute

value = instance.CreateInstance4(OwnerDoc, OwnerObj, NameIn, Options, ConfigurationOption)
```

### C#

```csharp
Attribute CreateInstance4(
   ModelDoc2 OwnerDoc,
   System.object OwnerObj,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

### C++/CLI

```cpp
Attribute^ CreateInstance4(
   ModelDoc2^ OwnerDoc,
   System.Object^ OwnerObj,
   System.String^ NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`:
- `OwnerObj`:
- `NameIn`:
- `Options`:
- `ConfigurationOption`:

## VBA Syntax

See [AttributeDef::CreateInstance4](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~CreateInstance4.html).

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)
