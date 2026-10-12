---
title: "SetFace Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetFace.html"
---

# SetFace Method (ISurfExtrudeFeatureData)

Sets the end condition face for this extruded surface in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As System.Object

instance.SetFace(Forward, Face)
```

### C#

```csharp
void SetFace(
   System.bool Forward,
   System.object Face
)
```

### C++/CLI

```cpp
void SetFace(
   System.bool Forward,
   System.Object^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the end condition face in the forward direction, false sets it in the reverse direction
- `Face`: End condition [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfExtrudeFeatureData::SetFace](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::ISetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetFace.html)
[ISurfExtrudeFeatureData::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetFace.html)
[ISurfExtrudeFeatureData::IGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetFace.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
