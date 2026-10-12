---
title: "BlurryReflection Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "BlurryReflection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~BlurryReflection.html"
---

# BlurryReflection Property (IAppearanceSetting)

Gets or sets whether to blur the reflections of surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlurryReflection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Boolean

instance.BlurryReflection = value

value = instance.BlurryReflection
```

### C#

```csharp
System.bool BlurryReflection {get; set;}
```

### C++/CLI

```cpp
property System.bool BlurryReflection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to blur reflections, false to not

## VBA Syntax

See [AppearanceSetting::BlurryReflection](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~BlurryReflection.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
