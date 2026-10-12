---
title: "IDeleteDisplayStateSpecificRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IDeleteDisplayStateSpecificRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html"
---

# IDeleteDisplayStateSpecificRenderMaterial Method (IModelDocExtension)

Deletes the specified materials, using the IDs of the materials, from the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteDisplayStateSpecificRenderMaterial( _
   ByVal IdCount As System.Integer, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim IdCount As System.Integer
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean

value = instance.IDeleteDisplayStateSpecificRenderMaterial(IdCount, PWMaterialId1, PWMaterialId2)
```

### C#

```csharp
System.bool IDeleteDisplayStateSpecificRenderMaterial(
   System.int IdCount,
   ref System.int PWMaterialId1,
   ref System.int PWMaterialId2
)
```

### C++/CLI

```cpp
System.bool IDeleteDisplayStateSpecificRenderMaterial(
   System.int IdCount,
   System.int% PWMaterialId1,
   System.int% PWMaterialId2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdCount`: Number of material IDs
- `PWMaterialId1`: - in-process, unmanaged C++: Pointer to an array of the first IDs of the material to delete

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `PWMaterialId2`: - in-process, unmanaged C++: Pointer to an array of the second IDs of the material to delete

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the materials are deleted, false if not

## Remarks

Before calling this method, call:

- [IModelDocExtension::GetRenderMaterialsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html) to get the value for IdCount.
- [IRenderMaterial::GetMaterialIds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetMaterialIDs.html) to the get the values for PWMaterialId1 and PWMaterialId2, the IDs of the materials added to the model.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
