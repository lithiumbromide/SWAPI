---
title: "Specular Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "Specular"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~Specular.html"
---

# Specular Property (IAppearanceSetting)

Gets or sets the intensity of highlights on surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Property Specular As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.Specular = value

value = instance.Specular
```

### C#

```csharp
System.double Specular {get; set;}
```

### C++/CLI

```cpp
property System.double Specular {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= `specular_value` <= 1; valid only when [IAppearanceSetting::SpecularSpread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting~SpecularSpread.html) > 0

## VBA Syntax

See [AppearanceSetting::Specular](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~Specular.html).

## Remarks

See SOLIDWORKS Help for more information about appearances.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
