---
title: "SaveCompareVolumeResults Method (gtcocswCompareDocument)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswCompareDocument"
member: "SaveCompareVolumeResults"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument~SaveCompareVolumeResults.html"
---

# SaveCompareVolumeResults Method (gtcocswCompareDocument)

Saves the volume comparison results as a SOLIDWORKS part document after comparing documents with the Compare volumes option selected.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveCompareVolumeResults( _
   ByVal resultfile As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswCompareDocument
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

- `resultfile`: Path and filename to which to save the SOLIDWORKS part document

  NOTE: You do not have to specify the filename extension .sldprt. It is automatically appended to the filename.

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareDocument::SaveCompareVolumeResults](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareDocument~SaveCompareVolumeResults.html).

## See Also

[gtcocswCompareDocument Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument.html)
[gtcocswCompareDocument Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS
