---
title: "GetPatternBodyCount Method (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "GetPatternBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~GetPatternBodyCount.html"
---

# GetPatternBodyCount Method (IMirrorSolidFeatureData)

Gets the number of seed bodies in this mirror solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
Dim value As System.Integer

value = instance.GetPatternBodyCount()
```

### C#

```csharp
System.int GetPatternBodyCount()
```

### C++/CLI

```cpp
System.int GetPatternBodyCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of seed bodies

## VBA Syntax

See [MirrorSolidFeatureData::GetPatternBodyCount](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~GetPatternBodyCount.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)
[IMirrorSolidFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~IGetPatternBodyArray.html)
[IMirrorSolidFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~ISetPatternBodyArray.html)
[IMirrorSolidFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~PatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
