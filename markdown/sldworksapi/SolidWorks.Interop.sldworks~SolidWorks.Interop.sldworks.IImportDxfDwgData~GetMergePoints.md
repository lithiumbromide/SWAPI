---
title: "GetMergePoints Method (IImportDxfDwgData)"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: "GetMergePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints.html"
---

# GetMergePoints Method (IImportDxfDwgData)

Gets whether near-identical points are merged in the part sketch after entities are imported.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMergePoints( _
   ByVal Sheet As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean

value = instance.GetMergePoints(Sheet)
```

### C#

```csharp
System.bool GetMergePoints(
   System.string Sheet
)
```

### C++/CLI

```cpp
System.bool GetMergePoints(
   System.String^ Sheet
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Sheet (layout) name of the input file or an empty string for all sheets

### Return Value

True to merge near-identical points, false to not

## VBA Syntax

See [ImportDxfDwgData::GetMergePoints](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData~GetMergePoints.html).

## Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

## See Also

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[IImportDxfDwgData::GetMergeDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance.html)
[IImportDxfDwgData::SetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
