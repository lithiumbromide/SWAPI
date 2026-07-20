---
title: "SetPlacementFace Method (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "SetPlacementFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~SetPlacementFace.html"
---

# SetPlacementFace Method (ILibraryFormToolFeatureData)

Specifies the face and pickpoint where the forming tool is inserted.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPlacementFace( _
   ByVal Face As System.Object, _
   ByVal PickPoint As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim Face As System.Object
Dim PickPoint As System.Object

instance.SetPlacementFace(Face, PickPoint)
```

### C#

```csharp
void SetPlacementFace(
   System.object Face,
   System.object PickPoint
)
```

### C++/CLI

```cpp
void SetPlacementFace(
   System.Object^ Face,
   System.Object^ PickPoint
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Face`: [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- `PickPoint`: [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See

[LibraryFormToolFeatureData::SetPlacementFace](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~SetPlacementFace.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::PlacementFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~PlacementFace.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
