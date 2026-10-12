---
title: "SpecularColor Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "SpecularColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularColor.html"
---

# SpecularColor Property (IAppearanceSetting)

Gets or sets the color of reflected highlights for a specular component.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecularColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Integer

instance.SpecularColor = value

value = instance.SpecularColor
```

### C#

```csharp
System.int SpecularColor {get; set;}
```

### C++/CLI

```cpp
property System.int SpecularColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Color of reflected highlights; valid only when [IAppearanceSetting::SpecularSpread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting~SpecularSpread.html) > 0 and [IAppearanceSetting::Specular](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting~Specular.html) > 0 (see **Remarks**)

## VBA Syntax

See [AppearanceSetting::SpecularColor](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~SpecularColor.html).

## Remarks

`specular_color` = MAX(MIN(`red_rgb_value`,255),0) + MAX(MIN(`green_rgb_value`,255),0)*16*16 + MAX(MIN(`blue_rgb_value`,255),0)*16*16*16*16

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
