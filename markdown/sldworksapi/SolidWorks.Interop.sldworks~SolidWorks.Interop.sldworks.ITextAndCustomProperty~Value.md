---
title: "Value Property (ITextAndCustomProperty)"
project: "SOLIDWORKS API Help"
interface: "ITextAndCustomProperty"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty~Value.html"
---

# Value Property (ITextAndCustomProperty)

Gets or sets the value of the text or custom property in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) for a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Value As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITextAndCustomProperty
Dim value As System.String

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.string Value {get; set;}
```

### C++/CLI

```cpp
property System.String^ Value {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value

## VBA Syntax

See [TextAndCustomProperty::Value](ms-its:sldworksapivb6.chm::/sldworks~TextAndCustomProperty~Value.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## See Also

[ITextAndCustomProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.html)
[ITextAndCustomProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
