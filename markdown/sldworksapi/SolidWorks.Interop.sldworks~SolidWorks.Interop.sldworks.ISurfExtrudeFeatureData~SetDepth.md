---
title: "SetDepth Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetDepth.html"
---

# SetDepth Method (ISurfExtrudeFeatureData)

Sets the depth of this extruded surface in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDepth( _
   ByVal Forward As System.Boolean, _
   ByVal Depth As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Depth As System.Double

instance.SetDepth(Forward, Depth)
```

### C#

```csharp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

### C++/CLI

```cpp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the depth in the forward direction, false sets it in the reverse direction
- `Depth`: Extrusion depth

## VBA Syntax

See [SurfExtrudeFeatureData::SetDepth](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetDepth.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::GetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetDepth.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
