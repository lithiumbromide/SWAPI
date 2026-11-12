---
title: "GetDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.html"
---

# GetDecal Method (IModelDocExtension)

Gets the specified decal in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDecal( _
   ByVal ID As System.Integer, _
   ByVal Configuration As System.String _
) As Decal
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Configuration As System.String
Dim value As Decal

value = instance.GetDecal(ID, Configuration)
```

### C#

```csharp
Decal GetDecal(
   System.int ID,
   System.string Configuration
)
```

### C++/CLI

```cpp
Decal^ GetDecal(
   System.int ID,
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Decal ID (see **Remarks**)
- `Configuration`: Name of the configuration where to get the decal

### Return Value

[Decal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal.html)

## VBA Syntax

See [ModelDocExtension::GetDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetDecal.html).

## Examples

[Get Mask Types of Each Decal (VBA)](Get_Mask_Types_of_Each_Decal_Example_VB.htm)

## Remarks

The decal ID is the index number of the decal in the model. Call [IModelDocExtension::GetDecalsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDecalsCount.html) to find out the number of decals in the model and their IDs.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::DeleteDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html)
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::IGetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetDecals.html)
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
