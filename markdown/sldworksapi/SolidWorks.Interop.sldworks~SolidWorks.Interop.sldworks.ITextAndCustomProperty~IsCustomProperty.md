---
title: "IsCustomProperty Property (ITextAndCustomProperty)"
project: "SOLIDWORKS API Help"
interface: "ITextAndCustomProperty"
member: "IsCustomProperty"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty~IsCustomProperty.html"
---

# IsCustomProperty Property (ITextAndCustomProperty)

Gets whether this is text or a custom property in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) for a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsCustomProperty As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITextAndCustomProperty
Dim value As System.Boolean

value = instance.IsCustomProperty
```

### C#

```csharp
System.bool IsCustomProperty {get;}
```

### C++/CLI

```cpp
property System.bool IsCustomProperty {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a custom property, false if text

## VBA Syntax

See [TextAndCustomProperty::IsCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~TextAndCustomProperty~IsCustomProperty.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

This property corresponds to a **Text Field** or **Custom Property Field** group box in a theme.

## See Also

[ITextAndCustomProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.html)
[ITextAndCustomProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
