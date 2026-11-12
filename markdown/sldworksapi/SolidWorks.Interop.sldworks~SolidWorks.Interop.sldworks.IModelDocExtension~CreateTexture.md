---
title: "CreateTexture Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html"
---

# CreateTexture Method (IModelDocExtension)

Creates a texture.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTexture( _
   ByVal MatName As System.String, _
   ByVal Scale As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Blend As System.Boolean _
) As Texture
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim MatName As System.String
Dim Scale As System.Double
Dim Angle As System.Double
Dim Blend As System.Boolean
Dim value As Texture

value = instance.CreateTexture(MatName, Scale, Angle, Blend)
```

### C#

```csharp
Texture CreateTexture(
   System.string MatName,
   System.double Scale,
   System.double Angle,
   System.bool Blend
)
```

### C++/CLI

```cpp
Texture^ CreateTexture(
   System.String^ MatName,
   System.double Scale,
   System.double Angle,
   System.bool Blend
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MatName`: Name of the texture file
- `Scale`: Value by which to adjust the granularity of the texture; value between 0.001 and 1000000.00
- `Angle`: Value by which to adjust the rotation of the texture; value between 0.0 and 360.0
- `Blend`: True to blend the part color with the texture color, false to not

### Return Value

[ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.html)

## VBA Syntax

See [ModelDocExtension::CreateTexture](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateTexture.html).

## Examples

[Apply and Remove Texture To and From Model By Display State (VB.NET)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm)
[Apply and Remove Texture To and From Model By Display State (C#)](Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm)
[Apply and Remove Texture To and From Model By Display State (VBA)](Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm)
[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)
[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)
[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::RemoveTexture2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTexture2.html)
[IModelDocExtension::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTexture.html)
[IModelDocExtension::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetTexture.html)
[IModelDocExtenson::RemoveTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveTextureByDisplayState.html)
[IModelDocExtenson::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTextureByDisplayState.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
