---
title: "PickPoint Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "PickPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~PickPoint.html"
---

# PickPoint Property (ILibraryFormToolFeatureData)

Gets the pickpoint where this forming tool is inserted.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PickPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Object

value = instance.PickPoint
```

### C#

```csharp
System.object PickPoint {get;}
```

### C++/CLI

```cpp
property System.Object^ PickPoint {
   System.Object^ get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

[IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See

[LibraryFormToolFeatureData::PickPoint](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~PickPoint.html)

.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::SetPlacementFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~SetPlacementFace.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
