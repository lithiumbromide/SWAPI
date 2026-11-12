---
title: "GetDecalsCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetDecalsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html"
---

# GetDecalsCount Method (IModelDocExtension)

Gets the number of decals applied to this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDecalsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetDecalsCount()
```

### C#

```csharp
System.int GetDecalsCount()
```

### C++/CLI

```cpp
System.int GetDecalsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of decals applied to this model

## VBA Syntax

See [ModelDocExtension::GetDecalsCount](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetDecalsCount.html).

## Examples

[Get Mask Types of Each Decal (VBA)](Get_Mask_Types_of_Each_Decal_Example_VB.htm)

## Remarks

Call this method before calling [IModelDocExtension::GetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDecals.html) to get the size of the array for that method.

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
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
