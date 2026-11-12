---
title: "GetPartingLinesType Method (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "GetPartingLinesType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesType.html"
---

# GetPartingLinesType Method (IPartingSurfaceFeatureData)

Gets the type of entity to use for parting lines for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartingLinesType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer

value = instance.GetPartingLinesType()
```

### C#

```csharp
System.int GetPartingLinesType()
```

### C++/CLI

```cpp
System.int GetPartingLinesType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- 0 = [Parting-line feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingLineFeatureData.html)
- 1 = [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [PartingSurfaceFeatureData::GetPartingLinesType](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~GetPartingLinesType.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~GetPartingLinesCount.html)
[IPartingSurfaceFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~IGetPartingLines.html)
[IPartingSurfaceFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ISetPartingLines.html)
[IPartingSurfaceFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingLines.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
