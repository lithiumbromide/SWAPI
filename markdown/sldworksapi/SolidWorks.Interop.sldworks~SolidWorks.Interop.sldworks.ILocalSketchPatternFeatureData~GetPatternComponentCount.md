---
title: "GetPatternComponentCount Method (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "GetPatternComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetPatternComponentCount.html"
---

# GetPatternComponentCount Method (ILocalSketchPatternFeatureData)

Gets the number of components in this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer

value = instance.GetPatternComponentCount()
```

### C#

```csharp
System.int GetPatternComponentCount()
```

### C++/CLI

```cpp
System.int GetPatternComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components

## VBA Syntax

See [LocalSketchPatternFeatureData::GetPatternComponentCount](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~GetPatternComponentCount.html).

## Examples

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::PatternComponentArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~PatternComponentArray.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
