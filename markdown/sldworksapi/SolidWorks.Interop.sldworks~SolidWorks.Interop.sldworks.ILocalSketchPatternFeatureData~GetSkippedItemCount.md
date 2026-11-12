---
title: "GetSkippedItemCount Method (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "GetSkippedItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetSkippedItemCount.html"
---

# GetSkippedItemCount Method (ILocalSketchPatternFeatureData)

Gets the number of components skipped in this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSkippedItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer

value = instance.GetSkippedItemCount()
```

### C#

```csharp
System.int GetSkippedItemCount()
```

### C++/CLI

```cpp
System.int GetSkippedItemCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components skipped

## VBA Syntax

See [LocalSketchPatternFeatureData::GetSkippedItemCount](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~GetSkippedItemCount.html).

## Examples

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::SkippedItemArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
