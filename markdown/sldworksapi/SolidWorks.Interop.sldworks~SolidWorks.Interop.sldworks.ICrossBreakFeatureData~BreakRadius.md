---
title: "BreakRadius Property (ICrossBreakFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICrossBreakFeatureData"
member: "BreakRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData~BreakRadius.html"
---

# BreakRadius Property (ICrossBreakFeatureData)

Gets or sets the radius for this cross break feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICrossBreakFeatureData
Dim value As System.Double

instance.BreakRadius = value

value = instance.BreakRadius
```

### C#

```csharp
System.double BreakRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BreakRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Radius

## VBA Syntax

See [CrossBreakFeatureData::BreakRadius](ms-its:sldworksapivb6.chm::/sldworks~CrossBreakFeatureData~BreakRadius.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## See Also

[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)
[ICrossBreakFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
