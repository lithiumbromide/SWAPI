---
title: "GetRenderMaterials2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetRenderMaterials2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials2.html"
---

# GetRenderMaterials2 Method (IModelDocExtension)

Gets the appearances applied to this model document in the specified display states.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterials2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Object

value = instance.GetRenderMaterials2(DisplayStateOption, DisplayStateNames)
```

### C#

```csharp
System.object GetRenderMaterials2(
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

### C++/CLI

```cpp
System.Object^ GetRenderMaterials2(
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateNames`: Array of display state names

### Return Value

Array of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [ModelDocExtension::GetRenderMaterials2](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetRenderMaterials2.html).

## Examples

[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateRenderMaterial Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)
[IModelDocExtension::GetRenderMaterialsCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount2.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
