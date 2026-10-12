---
title: "Reflection Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "Reflection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Reflection.html"
---

# Reflection Property (IAppearanceSetting)

Gets or sets the reflectivity of a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reflection As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.Reflection = value

value = instance.Reflection
```

### C#

```csharp
System.double Reflection {get; set;}
```

### C++/CLI

```cpp
property System.double Reflection {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= `reflectivity` <= 1, where 0 is for no reflection, and 1 is for a mirror reflection

## VBA Syntax

See [AppearanceSetting::Reflection](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~Reflection.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
