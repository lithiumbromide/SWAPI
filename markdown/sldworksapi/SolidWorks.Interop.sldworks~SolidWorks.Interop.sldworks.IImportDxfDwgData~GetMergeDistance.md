---
title: "GetMergeDistance Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetMergeDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance.html"
---

# GetMergeDistance Method (IImportDxfDwgData)

Gets whether points that are within the specified distance are merged in the part sketch after entities are imported.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMergeDistance( _
   ByVal Sheet As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Double

value = instance.GetMergeDistance(Sheet)
```

### C#

```csharp
System.double GetMergeDistance(
   System.string Sheet
)
```

### C++/CLI

```cpp
System.double GetMergeDistance(
   System.String^ Sheet
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Return Value

Distance to determine whether two points should be merged

## VBA Syntax

See [ImportDxfDwgData::GetMergeDistance](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetMergeDistance.html).

## Examples

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

## Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints.html)
[IImportDxfDwgData::SetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
