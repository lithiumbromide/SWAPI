---
title: "SpecularSpread Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "SpecularSpread"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~SpecularSpread.html"
---

# SpecularSpread Property (IAppearanceSetting)

Gets or sets the blurriness of reflections on a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecularSpread As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.SpecularSpread = value

value = instance.SpecularSpread
```

### C#

```csharp
System.double SpecularSpread {get; set;}
```

### C++/CLI

```cpp
property System.double SpecularSpread {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= specular_spread <= 1; valid only when [IAppearanceSetting::Specular](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting~Specular.html) > 0 and [IAppearanceSetting::SpecularColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting~SpecularColor.html) > 0 (not black)

## VBA Syntax

See [AppearanceSetting::SpecularSpread](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~SpecularSpread.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
