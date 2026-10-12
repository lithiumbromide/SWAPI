---
title: "Elliptical Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "Elliptical"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Elliptical.html"
---

# Elliptical Property (IDomeFeatureData2)

Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii.

## Syntax

### Visual Basic (Declaration)

```vb
Property Elliptical As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim value As System.Boolean

instance.Elliptical = value

value = instance.Elliptical
```

### C#

```csharp
System.bool Elliptical {get; set;}
```

### C++/CLI

```cpp
property System.bool Elliptical {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the dome is elliptical, false if it is not

## VBA Syntax

See [DomeFeatureData2::Elliptical](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~Elliptical.html).

## Examples

[Change Height of Dome (VBA)](Change_Height_of_Dome_Feature_Example_VB.htm)
[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

This property does not affect geometry until you call [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html).

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
