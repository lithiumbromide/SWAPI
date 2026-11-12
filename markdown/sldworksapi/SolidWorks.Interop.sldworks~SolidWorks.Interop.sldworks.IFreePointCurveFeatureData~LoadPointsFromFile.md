---
title: "LoadPointsFromFile Method (IFreePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFreePointCurveFeatureData"
member: "LoadPointsFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~LoadPointsFromFile.html"
---

# LoadPointsFromFile Method (IFreePointCurveFeatureData)

Loads the points for this free-point curve from a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadPointsFromFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFreePointCurveFeatureData
Dim FileName As System.String
Dim value As System.Boolean

value = instance.LoadPointsFromFile(FileName)
```

### C#

```csharp
System.bool LoadPointsFromFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool LoadPointsFromFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name of the free-point curve file that contains the points to load; you can specify **.sldcrv** files or **.txt** files that use the same format as **.sldcrv** files

### Return Value

True if the points loaded successfully, false if not

## VBA Syntax

See [FreePointCurveFeatureData::LoadPointsFromFile](ms-its:sldworksapivb6.chm::/sldworks~FreePointCurveFeatureData~LoadPointsFromFile.html).

## Remarks

See SOLIDWORKS Help for details about free-point curve files.

## See Also

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.html)
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
