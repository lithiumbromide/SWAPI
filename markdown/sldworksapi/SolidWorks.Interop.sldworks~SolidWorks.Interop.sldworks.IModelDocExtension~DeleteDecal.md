---
title: "DeleteDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html"
---

# DeleteDecal Method (IModelDocExtension)

Removes the specified decal from this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDecal( _
   ByVal DecalID As System.Integer, _
   ByVal BReassignIdsAndInvalidate As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DecalID As System.Integer
Dim BReassignIdsAndInvalidate As System.Boolean
Dim value As System.Boolean

value = instance.DeleteDecal(DecalID, BReassignIdsAndInvalidate)
```

### C#

```csharp
System.bool DeleteDecal(
   System.int DecalID,
   System.bool BReassignIdsAndInvalidate
)
```

### C++/CLI

```cpp
System.bool DeleteDecal(
   System.int DecalID,
   System.bool BReassignIdsAndInvalidate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DecalID`: [Decal ID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal~DecalID.html)
- `BReassignIdsAndInvalidate`: True if the decal IDs are reassigned and this decal ID is invalidated, false if not

### Return Value

True if the decal is removed from the model, false if not

## VBA Syntax

See [IModelDocExtension::DeleteDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~DeleteDecal.html).

## Examples

[Delete Decal (VBA)](Delete_Decal_Example_VB.htm)
[Delete Decal (VB.NET)](Delete_Decal_Example_VBNET.htm)
[Delete Decal (C#)](Delete_Decal_Example_CSharp.htm)

## Remarks

By default, decal IDs are persistent, which means if three decals (IDs 1, 2, and 3) were applied to the model, and you removed decal ID 2, then the remaining decal IDs are 1 and 3. However, if you set BReassignIdsAndInvalidate to true, then decal ID 2 is invalidated and decal ID 3 becomes decal ID 2.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::GetDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.html)
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::IGetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetDecals.html)
[IModelDocExtension::MoveDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
