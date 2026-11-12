---
title: "AddDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html"
---

# AddDecal Method (IModelDocExtension)

Adds a decal to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDecal( _
   ByVal PDecal As Decal, _
   ByRef DecalID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PDecal As Decal
Dim DecalID As System.Integer
Dim value As System.Boolean

value = instance.AddDecal(PDecal, DecalID)
```

### C#

```csharp
System.bool AddDecal(
   Decal PDecal,
   out System.int DecalID
)
```

### C++/CLI

```cpp
System.bool AddDecal(
   Decal^ PDecal,
   [Out] System.int DecalID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDecal`: [Decal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal.html)
- `DecalID`: Decal ID

### Return Value

True if the decal was added to the model, false if not

## VBA Syntax

See [ModelDocExtension::AddDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddDecal.html).

## Examples

[Add Decal (VBA)](Add_Decal_Example_VB.htm)
[Add Decal (C#)](Add_Decal_Example_CSharp.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html)
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
