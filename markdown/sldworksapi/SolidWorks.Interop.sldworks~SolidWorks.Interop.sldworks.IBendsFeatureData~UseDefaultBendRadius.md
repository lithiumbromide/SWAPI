---
title: "UseDefaultBendRadius Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "UseDefaultBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendRadius.html"
---

# UseDefaultBendRadius Property (IBendsFeatureData)

Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
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

True to use the default bend radius, false to not

## VBA Syntax

See [BendsFeatureData::UseDefaultBendRadius](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~UseDefaultBendRadius.html).

## Examples

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
[IBendsFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
