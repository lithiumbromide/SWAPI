---
title: "SetPlacementPlane Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "SetPlacementPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetPlacementPlane.html"
---

# SetPlacementPlane Method (ILibraryFeatureData)

Sets the face or plane on which to place the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPlacementPlane( _
   ByVal PDispIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim PDispIn As System.Object

instance.SetPlacementPlane(PDispIn)
```

### C#

```csharp
void SetPlacementPlane(
   System.object PDispIn
)
```

### C++/CLI

```cpp
void SetPlacementPlane(
   System.Object^ PDispIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDispIn`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) on which to place the library feature

## VBA Syntax

See [LibraryFeatureData::SetPlacementPlane](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~SetPlacementPlane.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetPlacementPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetPlacementPlane.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
