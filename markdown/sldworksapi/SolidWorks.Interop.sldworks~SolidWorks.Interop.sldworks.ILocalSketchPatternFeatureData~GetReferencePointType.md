---
title: "GetReferencePointType Method (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "GetReferencePointType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetReferencePointType.html"
---

# GetReferencePointType Method (ILocalSketchPatternFeatureData)

Gets the type of reference point of this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencePointType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Integer

value = instance.GetReferencePointType()
```

### C#

```csharp
System.int GetReferencePointType()
```

### C++/CLI

```cpp
System.int GetReferencePointType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of reference point as defined in [swLocalSketchPatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalSketchPatternReferencePoint_e.html); -1 for default, orgin, or none

## VBA Syntax

See [LocalSketchPatternFeatureData::GetReferencePointType](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~GetreferencePointType.html).

## Examples

[Create Local Sketch-driven Pattern (C#)](Create_Local_Sketch-driven_Pattern_Example_CSharp.htm)
[Create Local Sketch-driven Pattern (VB.NET)](Create_Local_Sketch-driven_Pattern_Example_VBNET.htm)
[Create Local Sketch-driven Pattern (VBA)](Create_Local_Sketch-driven_Pattern_Example_VB.htm)

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ReferencePoint.html)
[ILocalSketchPatternFeatureData::SelectedPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SelectedPoint.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
