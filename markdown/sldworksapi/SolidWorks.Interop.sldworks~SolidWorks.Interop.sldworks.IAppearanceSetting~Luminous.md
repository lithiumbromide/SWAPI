---
title: "Luminous Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "Luminous"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Luminous.html"
---

# Luminous Property (IAppearanceSetting)

Gets or sets the brightness emitted from the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property Luminous As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.Luminous = value

value = instance.Luminous
```

### C#

```csharp
System.double Luminous {get; set;}
```

### C++/CLI

```cpp
property System.double Luminous {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= `luminosity` <= 1

## VBA Syntax

See [AppearanceSetting::Luminous](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~Luminous.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
