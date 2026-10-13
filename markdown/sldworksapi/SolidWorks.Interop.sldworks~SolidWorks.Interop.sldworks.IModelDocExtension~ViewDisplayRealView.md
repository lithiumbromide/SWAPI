---
title: "ViewDisplayRealView Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ViewDisplayRealView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.html"
---

# ViewDisplayRealView Property (IModelDocExtension)

Gets or sets the RealView Graphics setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewDisplayRealView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

instance.ViewDisplayRealView = value

value = instance.ViewDisplayRealView
```

### C#

```csharp
System.bool ViewDisplayRealView {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewDisplayRealView {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if RealView Graphics is set, false if not

## VBA Syntax

See [ModelDocExtension::ViewDisplayRealView](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ViewDisplayRealView.html).

## Examples

[Get Appearance File Name (C#)](Get_Appearance_Filename_Example_CSharp.htm)
[Get Appearance File Name (VB.NET)](Get_Appearance_Filename_Example_VBNET.htm)
[Get Appearance File Name (VBA)](Get_Appearance_Filename_Example_VB.htm)

## Remarks

When you [apply a material to a part](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html), use RealView Graphics to display the model with realistic-looking materials. RealView Graphics is available with supported graphics cards only. See the SOLIDWORKS Help for details.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IMaterialVisualPropertiesData::RealView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~RealView.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
