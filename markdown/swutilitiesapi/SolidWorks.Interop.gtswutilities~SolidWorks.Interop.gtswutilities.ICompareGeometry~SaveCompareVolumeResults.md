---
title: "SaveCompareVolumeResults Method (ICompareGeometry)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareGeometry"
member: "SaveCompareVolumeResults"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry~SaveCompareVolumeResults.html"
---

# SaveCompareVolumeResults Method (ICompareGeometry)

Obsolete. Do not use.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveCompareVolumeResults( _
   ByVal resultfile As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareGeometry
Dim resultfile As System.String
Dim value As System.Integer

value = instance.SaveCompareVolumeResults(resultfile)
```

### C#

```csharp
System.int SaveCompareVolumeResults(
   System.string resultfile
)
```

### C++/CLI

```cpp
System.int SaveCompareVolumeResults(
   System.String^ resultfile
)
```

### Parameters

- `resultfile`: Path and file name for the SOLIDWORKS part document (see **Remarks**)

  NOTE: You do not have to specify the filename extension .sldprt. It is automatically appended to the file name.

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareGeometry::SaveCompareVolumeResults](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareGeometry~SaveCompareVolumeResults.html).

## Remarks

This method opens the volume comparison results in a SOLIDWORKS part document after comparing geometry with the **Perform volume comparison** option selected.

If only a directory is specified in resultfile, a part document named "Volume Comparison of <part 1> and <part 2>.sldprt" is opened (but not saved) in SOLIDWORKS.

## See Also

[ICompareGeometry Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry.html)
[ICompareGeometry Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
