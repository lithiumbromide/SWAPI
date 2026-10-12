---
title: "Transparent Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "Transparent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Transparent.html"
---

# Transparent Property (IAppearanceSetting)

Gets or sets the degree to which light can pass through a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property Transparent As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.Transparent = value

value = instance.Transparent
```

### C#

```csharp
System.double Transparent {get; set;}
```

### C++/CLI

```cpp
property System.double Transparent {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= `transparency` <= 100, where 0 is for total opaqueness, and 100 is for total transparency

## VBA Syntax

See [AppearanceSetting::Transparent](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~Transparent.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
