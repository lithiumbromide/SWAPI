---
title: "SetCosmosWorksMaterial Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetCosmosWorksMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetCosmosWorksMaterial.html"
---

# SetCosmosWorksMaterial Method (IPartDoc)

Assigns the material to use during analysis to this part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCosmosWorksMaterial( _
   ByVal ConfigName As System.String, _
   ByVal Type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ConfigName As System.String
Dim Type As System.Integer

instance.SetCosmosWorksMaterial(ConfigName, Type)
```

### C#

```csharp
void SetCosmosWorksMaterial(
   System.string ConfigName,
   System.int Type
)
```

### C++/CLI

```cpp
void SetCosmosWorksMaterial(
   System.String^ ConfigName,
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration
- `Type`: Type of material to assign as defined by [swCosmosWorksMat](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmosWorksMat.html)

### Return Value

True if the material is assigned, false if not

## VBA Syntax

See [PartDoc::SetCosmosWorksMaterial](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetCosmosWorksMaterial.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IComponent2::SetCosmosWorksMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetCosmosWorksMaterial.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
