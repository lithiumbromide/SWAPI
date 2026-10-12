---
title: "SetMultipleThicknessAtIndex Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "SetMultipleThicknessAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.html"
---

# SetMultipleThicknessAtIndex Method (IShellFeatureData)

Sets the thickness of the shell at this index in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMultipleThicknessAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Thickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim Index As System.Integer
Dim Thickness As System.Double

instance.SetMultipleThicknessAtIndex(Index, Thickness)
```

### C#

```csharp
void SetMultipleThicknessAtIndex(
   System.int Index,
   System.double Thickness
)
```

### C++/CLI

```cpp
void SetMultipleThicknessAtIndex(
   System.int Index,
   System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index for new thickness
- `Thickness`: New thickness

## VBA Syntax

See [ShellFeatureData::SetMultipleThicknessAtIndex](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~SetMultipleThicknessAtIndex.html).

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.html)
[IShellFeatureData::GetMultipleThicknessFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.html)
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.html)
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html)
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.html)
[IShellFeatureData::IGetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
