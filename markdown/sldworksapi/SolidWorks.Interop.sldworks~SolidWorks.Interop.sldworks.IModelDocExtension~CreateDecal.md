---
title: "CreateDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html"
---

# CreateDecal Method (IModelDocExtension)

Creates a decal for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDecal() As Decal
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As Decal

value = instance.CreateDecal()
```

### C#

```csharp
Decal CreateDecal()
```

### C++/CLI

```cpp
Decal^ CreateDecal();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Decal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal.html)

## VBA Syntax

See [ModelDocExtension::CreateDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~CreateDecal.html).

## Examples

[Add Decal (VBA)](Add_Decal_Example_VB.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)
[Add Decal (C#)](Add_Decal_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::DeleteDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html)
[IModelDocExtension::GetDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.html)
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::IGetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetDecals.html)
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
