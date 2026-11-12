---
title: "GetPartingLinesCount Method (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "GetPartingLinesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesCount.html"
---

# GetPartingLinesCount Method (IPartingSurfaceFeatureData)

Gets the number of parting lines for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartingLinesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer

value = instance.GetPartingLinesCount()
```

### C#

```csharp
System.int GetPartingLinesCount()
```

### C++/CLI

```cpp
System.int GetPartingLinesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parting lines

## VBA Syntax

See [PartingSurfaceFeatureData::GetPartingLinesCount](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~GetPartingLinesCount.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## Remarks

Call this method before calling [IPartingSurfaceFeatureData::IGetPartingLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingSurfaceFeatureData~IGetPartingLines.html).

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ISetPartingLines.html)
[IPartingSurfaceFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingLines.html)
[IPartingSurfaceFeatureData::GetPartingLinesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
