---
title: "DoubleSided Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "DoubleSided"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~DoubleSided.html"
---

# DoubleSided Property (IAppearanceSetting)

Gets or sets whether to enable shading from both sides of a surface when rendering a model using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property DoubleSided As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Boolean

instance.DoubleSided = value

value = instance.DoubleSided
```

### C#

```csharp
System.bool DoubleSided {get; set;}
```

### C++/CLI

```cpp
property System.bool DoubleSided {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable shading from both sides, false to not

## VBA Syntax

See [AppearanceSetting::DoubleSided](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~DoubleSided.html).

## Remarks

This method is only available when a ray-trace rendering engine is loaded.

**NOTES:**

- When this property is disabled, surfaces that do not face the camera seem invisible.
- Double-sided surfaces can cause rendering errors. Use sparingly.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
