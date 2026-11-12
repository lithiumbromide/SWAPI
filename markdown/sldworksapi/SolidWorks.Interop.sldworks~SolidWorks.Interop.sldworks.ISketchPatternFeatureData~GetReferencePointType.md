---
title: "GetReferencePointType Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "GetReferencePointType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetReferencePointType.html"
---

# GetReferencePointType Method (ISketchPatternFeatureData)

Gets the type of reference point for this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencePointType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
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

Type of reference point:

- -1 = centroid
- 0 = closed curve
- 1 = sketch point
- 2 = vertex

## VBA Syntax

See [SketchPatternFeatureData::GetReferencePointType](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~GetReferencePointType.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketdhPatternFeatureData::ReferencePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
