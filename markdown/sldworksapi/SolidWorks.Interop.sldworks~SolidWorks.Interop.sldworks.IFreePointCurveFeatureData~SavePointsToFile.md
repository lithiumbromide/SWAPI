---
title: "SavePointsToFile Method (IFreePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFreePointCurveFeatureData"
member: "SavePointsToFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~SavePointsToFile.html"
---

# SavePointsToFile Method (IFreePointCurveFeatureData)

Saves the points for this free-point curve to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SavePointsToFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFreePointCurveFeatureData
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SavePointsToFile(FileName)
```

### C#

```csharp
System.bool SavePointsToFile(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SavePointsToFile(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name of the file to which to save the points; you can specify **.sldcrv** files or **.txt** as the filename extension

### Return Value

True if the points are saved to the file, false if not

## VBA Syntax

See [FreePointCurveFeatureData::SavePointsToFile](ms-its:sldworksapivb6.chm::/sldworks~FreePointCurveFeatureData~SavePointsToFile.html).

## Examples

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

## Remarks

Exported units, e.g., meters, of the document that owns the feature, and not necessarily those of the active document, are used when data is saved to a file.

See SOLIDWORKS Help for details about free-point curve files.

## See Also

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.html)
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
