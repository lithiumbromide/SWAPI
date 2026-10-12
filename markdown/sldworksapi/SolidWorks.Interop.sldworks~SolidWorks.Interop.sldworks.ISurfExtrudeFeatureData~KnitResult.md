---
title: "KnitResult Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "KnitResult"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~KnitResult.html"
---

# KnitResult Property (ISurfExtrudeFeatureData)

Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property KnitResult As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean

instance.KnitResult = value

value = instance.KnitResult
```

### C#

```csharp
System.bool KnitResult {get; set;}
```

### C++/CLI

```cpp
property System.bool KnitResult {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to knit the bodies created by deleting original faces, false to not (see **Remarks**)

## VBA Syntax

See [SurfExtrudeFeatureData::KnitResult](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~KnitResult.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

This property is only available if:

- [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html) = false.
- [ISurfExtrudeFeatureData::DeleteOriginalFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~DeleteOriginalFace.html) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
