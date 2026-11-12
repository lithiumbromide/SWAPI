---
title: "SetFixedFace Method (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "SetFixedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetFixedFace.html"
---

# SetFixedFace Method (ISketchedBendFeatureData)

Sets the fixed face of this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFixedFace( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal EdgeArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim EdgeArray As System.Object

instance.SetFixedFace(X, Y, Z, EdgeArray)
```

### C#

```csharp
void SetFixedFace(
   System.double X,
   System.double Y,
   System.double Z,
   System.object EdgeArray
)
```

### C++/CLI

```cpp
void SetFixedFace(
   System.double X,
   System.double Y,
   System.double Z,
   System.Object^ EdgeArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X location
- `Y`: Y location
- `Z`: Z location
- `EdgeArray`: Array of edges

## VBA Syntax

See [SketchedBendFeatureData::SetFixedFace](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~SetFixedFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::GetFixedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetFixedFace.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
