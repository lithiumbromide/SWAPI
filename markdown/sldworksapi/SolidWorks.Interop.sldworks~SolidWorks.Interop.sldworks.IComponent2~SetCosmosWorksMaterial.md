---
title: "SetCosmosWorksMaterial Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetCosmosWorksMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetCosmosWorksMaterial.html"
---

# SetCosmosWorksMaterial Method (IComponent2)

Assigns the material to use during analysis to this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCosmosWorksMaterial( _
   ByVal ConfigName As System.String, _
   ByVal Type As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConfigName As System.String
Dim Type As System.Integer
Dim value As System.Boolean

value = instance.SetCosmosWorksMaterial(ConfigName, Type)
```

### C#

```csharp
System.bool SetCosmosWorksMaterial(
   System.string ConfigName,
   System.int Type
)
```

### C++/CLI

```cpp
System.bool SetCosmosWorksMaterial(
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

See [Component2::SetCosmosWorksMaterial](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetCosmosWorksMaterial.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IPartDoc::SetCosmosWorksMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetCosmosWorksMaterial.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
