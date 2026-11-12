---
title: "DeleteRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial.html"
---

# DeleteRenderMaterial Method (IModelDocExtension)

Not supported in SOLIDWORKS 2011 and later. Superseded by [IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html) and [IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRenderMaterial( _
   ByVal PwMaterialId As System.Integer, _
   ByVal BReassignIdsAndInvalidate As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PwMaterialId As System.Integer
Dim BReassignIdsAndInvalidate As System.Boolean
Dim value As System.Boolean

value = instance.DeleteRenderMaterial(PwMaterialId, BReassignIdsAndInvalidate)
```

### C#

```csharp
System.bool DeleteRenderMaterial(
   System.int PwMaterialId,
   System.bool BReassignIdsAndInvalidate
)
```

### C++/CLI

```cpp
System.bool DeleteRenderMaterial(
   System.int PwMaterialId,
   System.bool BReassignIdsAndInvalidate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PwMaterialId`: Appearance ID
- `BReassignIdsAndInvalidate`: True if the appearance IDs are reassigned and this appearance ID is invalidated, false if not

### Return Value

True if the appearance is deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteRenderMaterial](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~DeleteRenderMaterial.html).

## Remarks

By default, appearance IDs are persistent, which means if three appearances (IDs 1, 2, and 3) were applied to the model, and you removed appearance ID 2, then the remaining appearance IDs are 1 and 3. However, if you set BReassignIdsAndInvalidate to true, then appearance ID 2 is invalidated and appearance ID 3 becomes appearance ID 2.

To get the IDs of all of the appearances applied to this model document, call [IModelDocExtension::GetRenderMaterialsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
