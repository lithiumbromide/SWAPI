---
title: "GetRenderMaterialsCount2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetRenderMaterialsCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount2.html"
---

# GetRenderMaterialsCount2 Method (IModelDocExtension)

Gets the number of appearances applied to this model document in the specified display states.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterialsCount2( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Integer

value = instance.GetRenderMaterialsCount2(DisplayStateOption, DisplayStateNames)
```

### C#

```csharp
System.int GetRenderMaterialsCount2(
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

### C++/CLI

```cpp
System.int GetRenderMaterialsCount2(
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateNames`: Array of display state names

### Return Value

Number of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [ModelDocExtension::GetRenderMaterialsCount2](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetRenderMaterialsCount2.html).

## Examples

[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)
[IModelDocExtension::GetRenderMaterials2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials2.html)
[IModelDocExtension::CreateRenderMaterial Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
