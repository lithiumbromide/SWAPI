---
title: "AddConfiguration2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddConfiguration2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddConfiguration2.html"
---

# AddConfiguration2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddConfiguration2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddConfiguration2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConfiguration2( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal SuppressByDefault As System.Boolean, _
   ByVal HideByDefault As System.Boolean, _
   ByVal MinFeatureManager As System.Boolean, _
   ByVal InheritProperties As System.Boolean, _
   ByVal Flags As System.UInteger _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim SuppressByDefault As System.Boolean
Dim HideByDefault As System.Boolean
Dim MinFeatureManager As System.Boolean
Dim InheritProperties As System.Boolean
Dim Flags As System.UInteger
Dim value As System.Boolean

value = instance.AddConfiguration2(Name, Comment, AlternateName, SuppressByDefault, HideByDefault, MinFeatureManager, InheritProperties, Flags)
```

### C#

```csharp
System.bool AddConfiguration2(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.bool SuppressByDefault,
   System.bool HideByDefault,
   System.bool MinFeatureManager,
   System.bool InheritProperties,
   System.uint Flags
)
```

### C++/CLI

```cpp
System.bool AddConfiguration2(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.bool SuppressByDefault,
   System.bool HideByDefault,
   System.bool MinFeatureManager,
   System.bool InheritProperties,
   System.uint Flags
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Comment`:
- `AlternateName`:
- `SuppressByDefault`:
- `HideByDefault`:
- `MinFeatureManager`:
- `InheritProperties`:
- `Flags`:

## VBA Syntax

See [ModelDoc::AddConfiguration2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddConfiguration2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
