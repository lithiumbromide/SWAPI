---
title: "EditConfiguration Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "EditConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditConfiguration.html"
---

# EditConfiguration Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::EditConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditConfiguration.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditConfiguration( _
   ByVal Name As System.String, _
   ByVal NewName As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal SuppressByDefault As System.Boolean, _
   ByVal HideByDefault As System.Boolean, _
   ByVal MinFeatureManager As System.Boolean, _
   ByVal InheritProperties As System.Boolean, _
   ByVal Flags As System.UInteger _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Name As System.String
Dim NewName As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim SuppressByDefault As System.Boolean
Dim HideByDefault As System.Boolean
Dim MinFeatureManager As System.Boolean
Dim InheritProperties As System.Boolean
Dim Flags As System.UInteger

instance.EditConfiguration(Name, NewName, Comment, AlternateName, SuppressByDefault, HideByDefault, MinFeatureManager, InheritProperties, Flags)
```

### C#

```csharp
void EditConfiguration(
   System.string Name,
   System.string NewName,
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
void EditConfiguration(
   System.String^ Name,
   System.String^ NewName,
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
- `NewName`:
- `Comment`:
- `AlternateName`:
- `SuppressByDefault`:
- `HideByDefault`:
- `MinFeatureManager`:
- `InheritProperties`:
- `Flags`:

## VBA Syntax

See [ModelDoc::EditConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~EditConfiguration.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
