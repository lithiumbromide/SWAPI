---
title: "SetFixedFace Method (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "SetFixedFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SetFixedFace.html"
---

# SetFixedFace Method (IConvertSolidFeatureData)

Sets the face that remains in place when the part is flattened in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFixedFace( _
   ByVal FaceIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim FaceIn As System.Object

instance.SetFixedFace(FaceIn)
```

### C#

```csharp
void SetFixedFace(
   System.object FaceIn
)
```

### C++/CLI

```cpp
void SetFixedFace(
   System.Object^ FaceIn
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FaceIn`: [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See

[ConvertSolidFeatureData::SetFixedFace](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~SetFixedFace.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

[IConvertSolidFeatureData::GetFixedFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GetFixedFace.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
