---
title: "BreakAngle Property (ICrossBreakFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICrossBreakFeatureData"
member: "BreakAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData~BreakAngle.html"
---

# BreakAngle Property (ICrossBreakFeatureData)

Gets or sets the angle for this cross break feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICrossBreakFeatureData
Dim value As System.Double

instance.BreakAngle = value

value = instance.BreakAngle
```

### C#

```csharp
System.double BreakAngle {get; set;}
```

### C++/CLI

```cpp
property System.double BreakAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle

## VBA Syntax

See [CrossBreakFeatureData::BreakAngle](ms-its:sldworksapivb6.chm::/sldworks~CrossBreakFeatureData~BreakAngle.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## See Also

[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)
[ICrossBreakFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
