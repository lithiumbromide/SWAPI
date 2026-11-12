---
title: "DeleteOriginalFace Property (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "DeleteOriginalFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~DeleteOriginalFace.html"
---

# DeleteOriginalFace Property (ISurfExtrudeFeatureData)

Gets or sets whether to delete the original faces of this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property DeleteOriginalFace As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean

instance.DeleteOriginalFace = value

value = instance.DeleteOriginalFace
```

### C#

```csharp
System.bool DeleteOriginalFace {get; set;}
```

### C++/CLI

```cpp
property System.bool DeleteOriginalFace {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to delete the original faces, false to not (see **Remarks**)

## VBA Syntax

See [SurfExtrudeFeatureData::DeleteOriginalFace](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~DeleteOriginalFace.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

This property is only available if [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.html) = false.

Deleting original faces results in the model being hollow where the faces were deleted and creates multiple bodies. To create a single body when original faces are deleted, use [ISurfExtrudeFeatureData::KnitResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~KnitResult.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
