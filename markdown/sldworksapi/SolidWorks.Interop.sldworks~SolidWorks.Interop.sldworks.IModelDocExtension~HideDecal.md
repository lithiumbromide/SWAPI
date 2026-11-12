---
title: "HideDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HideDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html"
---

# HideDecal Method (IModelDocExtension)

Hides or shows the specified decal applied to this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function HideDecal( _
   ByVal DecalID As System.Integer, _
   ByVal Hide As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DecalID As System.Integer
Dim Hide As System.Boolean
Dim value As System.Boolean

value = instance.HideDecal(DecalID, Hide)
```

### C#

```csharp
System.bool HideDecal(
   System.int DecalID,
   System.bool Hide
)
```

### C++/CLI

```cpp
System.bool HideDecal(
   System.int DecalID,
   System.bool Hide
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DecalID`: [Decal ID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal~DecalID.html)
- `Hide`: True to hide the decal, false to show it

### Return Value

True if the decal is hidden or shown, false if not

## VBA Syntax

See [ModelDocExtension::HideDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~HideDecal.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::DeleteDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html)
[IModelDocExtension::GetDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.html)
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::IGetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetDecals.html)
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
