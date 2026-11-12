---
title: "Height Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Height.html"
---

# Height Property (IDomeFeatureData2)

Gets or sets the height of the dome.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim value As System.Double

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.double Height {get; set;}
```

### C++/CLI

```cpp
property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of the dome

## VBA Syntax

See [DomeFeatureData2::Height](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~Height.html).

## Examples

[Change Height of Dome Feature (VBA)](Change_Height_of_Dome_Feature_Example_VB.htm)
[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

This property does not affect geometry until you call [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html).

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
