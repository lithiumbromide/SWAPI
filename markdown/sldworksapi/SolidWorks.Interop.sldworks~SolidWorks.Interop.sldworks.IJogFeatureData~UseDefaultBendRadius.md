---
title: "UseDefaultBendRadius Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "UseDefaultBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendRadius.html"
---

# UseDefaultBendRadius Property (IJogFeatureData)

Gets or sets whether to use the default bend radius for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRadius = value

value = instance.UseDefaultBendRadius
```

### C#

```csharp
System.bool UseDefaultBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the default bend radius, false does not

## VBA Syntax

See [JogFeatureData::UseDefaultBendRadius](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~UseDefaultBendRadius.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
