---
title: "RealView Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "RealView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~RealView.html"
---

# RealView Property (IMaterialVisualPropertiesData)

Gets or sets whether textures are displayed in RealView or Standard graphics.

## Syntax

### Visual Basic (Declaration)

```vb
Property RealView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.RealView = value

value = instance.RealView
```

### C#

```csharp
System.bool RealView {get; set;}
```

### C++/CLI

```cpp
property System.bool RealView {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if textures are RealView graphics, false if Standard graphics

## VBA Syntax

See [MaterialVisualPropertiesData::RealView](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~RealView.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## Remarks

[IMaterialVisualPropertiesData::AdvancedGraphics](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData~AdvancedGraphics.html) must be True to set this property.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)
[IModelDocExtension::ViewDisplayRealView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
