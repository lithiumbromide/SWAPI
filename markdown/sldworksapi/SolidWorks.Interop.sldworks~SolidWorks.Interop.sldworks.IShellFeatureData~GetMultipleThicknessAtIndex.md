---
title: "GetMultipleThicknessAtIndex Method (IShellFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShellFeatureData"
member: "GetMultipleThicknessAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.html"
---

# GetMultipleThicknessAtIndex Method (IShellFeatureData)

Gets the thickness of the shell at the specified index in this shell feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMultipleThicknessAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IShellFeatureData
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetMultipleThicknessAtIndex(Index)
```

### C#

```csharp
System.double GetMultipleThicknessAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetMultipleThicknessAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index for the thickness

### Return Value

Shell thickness

## VBA Syntax

See [ShellFeatureData::GetMultipleThicknessAtIndex](ms-its:sldworksapivb6.chm::/sldworks~ShellFeatureData~GetMultipleThicknessAtIndex.html).

## Examples

See the [IShellFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html) examples.

## See Also

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.html)
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html)
[IShellFeatureData::GetMultipleThicknessFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.html)
[IShellFeatureData::IGetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.html)
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.html)
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.html)
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.html)
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
