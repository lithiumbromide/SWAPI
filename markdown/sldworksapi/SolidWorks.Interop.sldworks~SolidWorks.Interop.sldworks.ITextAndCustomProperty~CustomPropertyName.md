---
title: "CustomPropertyName Property (ITextAndCustomProperty)"
project: "SOLIDWORKS API Help"
interface: "ITextAndCustomProperty"
member: "CustomPropertyName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty~CustomPropertyName.html"
---

# CustomPropertyName Property (ITextAndCustomProperty)

Gets or sets the name of the custom property in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) for a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomPropertyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITextAndCustomProperty
Dim value As System.String

instance.CustomPropertyName = value

value = instance.CustomPropertyName
```

### C#

```csharp
System.string CustomPropertyName {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomPropertyName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of custom property

## VBA Syntax

See [TextAndCustomProperty::CustomPropertyName](ms-its:sldworksapivb6.chm::/sldworks~TextAndCustomProperty~CustomPropertyName.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

This property corresponds to the **Custom property** text box in a **Custom Property Field** group box in a theme.

## See Also

[ITextAndCustomProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.html)
[ITextAndCustomProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
