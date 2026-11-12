---
title: "GetMultipleThicknessFacesCount Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "GetMultipleThicknessFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.html"
---

# GetMultipleThicknessFacesCount Method (IShellFeatureData)

Gets the number of faces with multiple thickness in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMultipleThicknessFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim value As System.Integer

value = instance.GetMultipleThicknessFacesCount()
```

### C#

```csharp
System.int GetMultipleThicknessFacesCount()
```

### C++/CLI

```cpp
System.int GetMultipleThicknessFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces with multiple thickness

## VBA Syntax

See [ShellFeatureData::GetMultipleThicknessFacesCount](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~GetMultipleThicknessFacesCount.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## Remarks

Call this method before calling [IShellFeatureData::IGetMultipleThicknessFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.html) to get the size of the array for that method.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.html)
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.html)
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.html)
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html)
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
