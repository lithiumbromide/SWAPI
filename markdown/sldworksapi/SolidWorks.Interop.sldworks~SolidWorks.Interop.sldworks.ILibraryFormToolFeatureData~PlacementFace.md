---
title: "PlacementFace Property (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "PlacementFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~PlacementFace.html"
---

# PlacementFace Property (ILibraryFormToolFeatureData)

Gets the placement face where this forming tool is inserted.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PlacementFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.Object

value = instance.PlacementFace
```

### C#

```csharp
System.object PlacementFace {get;}
```

### C++/CLI

```cpp
property System.Object^ PlacementFace {
   System.Object^ get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See

[LibraryFormToolFeatureData::PlacementFace](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~PlacementFace.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

[ILibraryFormToolFeatureData::SetPlacementFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~SetPlacementFace.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
