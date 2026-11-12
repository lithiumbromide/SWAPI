---
title: "ISetFace Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "ISetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetFace.html"
---

# ISetFace Method (ISurfExtrudeFeatureData)

Sets the end condition face for this extruded surface in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As Face2

instance.ISetFace(Forward, Face)
```

### C#

```csharp
void ISetFace(
   System.bool Forward,
   Face2 Face
)
```

### C++/CLI

```cpp
void ISetFace(
   System.bool Forward,
   Face2^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the end condition face in the forward direction, false sets it in the reverse direction
- `Face`: End condition [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfExtrudeFeatureData::ISetFace](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~ISetFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetFace.html)
[ISurfExtrudeFeatureData::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetFace.html)
[ISurfExtrudeFeatureData::IGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetFace.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
