---
title: "AddDisplayStateSpecificRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddDisplayStateSpecificRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html"
---

# AddDisplayStateSpecificRenderMaterial Method (IModelDocExtension)

Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDisplayStateSpecificRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean

value = instance.AddDisplayStateSpecificRenderMaterial(PRenderMaterial, DisplayStateOption, DisplayStateNames, PWMaterialId1, PWMaterialId2)
```

### C#

```csharp
System.bool AddDisplayStateSpecificRenderMaterial(
   RenderMaterial PRenderMaterial,
   System.int DisplayStateOption,
   System.object DisplayStateNames,
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

### C++/CLI

```cpp
System.bool AddDisplayStateSpecificRenderMaterial(
   RenderMaterial^ PRenderMaterial,
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames,
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PRenderMaterial`: [Appearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html) to add
- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateNames`: Names of display states to which to add the appearance
- `PWMaterialId1`: First ID of appearance
- `PWMaterialId2`: Second ID of appearance

### Return Value

True if appearance is added, false if not

## VBA Syntax

See [ModelDocExtension::AddDisplayStateSpecificRenderMaterial](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddDisplayStateSpecificRenderMaterial.html).

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
