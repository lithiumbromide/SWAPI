---
title: "ReverseDirection Property (ICrossBreakFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICrossBreakFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (ICrossBreakFeatureData)

Gets or sets whether to reverse the direction of this cross break feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICrossBreakFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of this cross break feature, false to not

## VBA Syntax

See [CrossBreakFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~CrossBreakFeatureData~ReverseDirection.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## See Also

[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)
[ICrossBreakFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
