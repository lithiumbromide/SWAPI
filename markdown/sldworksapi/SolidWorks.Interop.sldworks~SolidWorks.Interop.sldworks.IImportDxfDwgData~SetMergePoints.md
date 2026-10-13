---
title: "SetMergePoints Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "SetMergePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints.html"
---

# SetMergePoints Method (IImportDxfDwgData)

Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMergePoints( _
   ByVal Sheet As System.String, _
   ByVal Merge As System.Boolean, _
   ByVal Distance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Merge As System.Boolean
Dim Distance As System.Double
Dim value As System.Boolean

value = instance.SetMergePoints(Sheet, Merge, Distance)
```

### C#

```csharp
System.bool SetMergePoints(
   System.string Sheet,
   System.bool Merge,
   System.double Distance
)
```

### C++/CLI

```cpp
System.bool SetMergePoints(
   System.String^ Sheet,
   System.bool Merge,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets
- `Merge`: True to merge near-identical points, false to not
- `Distance`: Distance to determine whether two points should be merged

### Return Value

True if near-identical points within the specified distance are merged, false if not

## VBA Syntax

See [ImportDxfDwgData::SetMergePoints](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~SetMergePoints.html).

## Examples

[Import DXF file into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

## Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints.html)
[IImportDxfDwgData::GetMergeDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
