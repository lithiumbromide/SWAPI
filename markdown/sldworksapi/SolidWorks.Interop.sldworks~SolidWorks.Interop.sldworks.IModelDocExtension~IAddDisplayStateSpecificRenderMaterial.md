---
title: "IAddDisplayStateSpecificRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IAddDisplayStateSpecificRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.html"
---

# IAddDisplayStateSpecificRenderMaterial Method (IModelDocExtension)

Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddDisplayStateSpecificRenderMaterial( _
   ByVal PRenderMaterial As RenderMaterial, _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateCount As System.Integer, _
   ByRef DisplayStateNames As System.String, _
   ByRef PWMaterialId1 As System.Integer, _
   ByRef PWMaterialId2 As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PRenderMaterial As RenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateCount As System.Integer
Dim DisplayStateNames As System.String
Dim PWMaterialId1 As System.Integer
Dim PWMaterialId2 As System.Integer
Dim value As System.Boolean

value = instance.IAddDisplayStateSpecificRenderMaterial(PRenderMaterial, DisplayStateOption, DisplayStateCount, DisplayStateNames, PWMaterialId1, PWMaterialId2)
```

### C#

```csharp
System.bool IAddDisplayStateSpecificRenderMaterial(
   RenderMaterial PRenderMaterial,
   System.int DisplayStateOption,
   System.int DisplayStateCount,
   ref System.string DisplayStateNames,
   out System.int PWMaterialId1,
   out System.int PWMaterialId2
)
```

### C++/CLI

```cpp
System.bool IAddDisplayStateSpecificRenderMaterial(
   RenderMaterial^ PRenderMaterial,
   System.int DisplayStateOption,
   System.int DisplayStateCount,
   System.String^% DisplayStateNames,
   [Out] System.int PWMaterialId1,
   [Out] System.int PWMaterialId2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PRenderMaterial`: [Material](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) to add
- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateCount`: Number of display states (see **Remarks**)
- `DisplayStateNames`: - in-process, unmanaged C++: Pointer to an array of the names of the display states to which to add material
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `PWMaterialId1`: First ID of material
- `PWMaterialId2`: Second ID of material

### Return Value

True if material is added, false if not

## Remarks

Before calling this method, call [IConfiguration::GetDisplayStatesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html) to get DisplayStateCount.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
