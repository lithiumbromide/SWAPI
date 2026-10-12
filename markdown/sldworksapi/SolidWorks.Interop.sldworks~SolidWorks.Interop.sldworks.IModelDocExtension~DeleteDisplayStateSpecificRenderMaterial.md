---
title: "DeleteDisplayStateSpecificRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteDisplayStateSpecificRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html"
---

# DeleteDisplayStateSpecificRenderMaterial Method (IModelDocExtension)

Deletes the specified appearances, using the IDs of the appearances, from the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDisplayStateSpecificRenderMaterial( _
   ByVal PWMaterialId1 As System.Object, _
   ByVal PWMaterialId2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PWMaterialId1 As System.Object
Dim PWMaterialId2 As System.Object
Dim value As System.Boolean

value = instance.DeleteDisplayStateSpecificRenderMaterial(PWMaterialId1, PWMaterialId2)
```

### C#

```csharp
System.bool DeleteDisplayStateSpecificRenderMaterial(
   System.object PWMaterialId1,
   System.object PWMaterialId2
)
```

### C++/CLI

```cpp
System.bool DeleteDisplayStateSpecificRenderMaterial(
   System.Object^ PWMaterialId1,
   System.Object^ PWMaterialId2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PWMaterialId1`: - Array of the first IDs of the appearances to delete
- `PWMaterialId2`: - Array of the second IDs of the appearance to delete

### Return Value

True if the appearances are deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteDisplayStateSpecificRenderMaterial](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html).

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## Remarks

Call [IRenderMaterial::GetMaterialIds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetMaterialIDs.html) to the get IDs of the appearances added to the model, then call IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial to delete the appearances.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
