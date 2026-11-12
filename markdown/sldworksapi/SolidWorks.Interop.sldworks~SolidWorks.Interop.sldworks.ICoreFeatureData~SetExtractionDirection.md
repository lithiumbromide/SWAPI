---
title: "SetExtractionDirection Method (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "SetExtractionDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~SetExtractionDirection.html"
---

# SetExtractionDirection Method (ICoreFeatureData)

Sets the entities that define the extraction direction of this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtractionDirection( _
   ByVal PDir1 As System.Object, _
   ByVal PDir2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim PDir1 As System.Object
Dim PDir2 As System.Object
Dim value As System.Boolean

value = instance.SetExtractionDirection(PDir1, PDir2)
```

### C#

```csharp
System.bool SetExtractionDirection(
   System.object PDir1,
   System.object PDir2
)
```

### C++/CLI

```cpp
System.bool SetExtractionDirection(
   System.Object^ PDir1,
   System.Object^ PDir2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PDir1`: Entity that defines the extraction direction (see **Remarks**)
- `PDir2`: Entity that defines the extraction direction (see Remarks)

### Return Value

True if the entities that define the extraction direction of this core feature are set, false if not

## VBA Syntax

See [CoreFeatureData::SetExtractionDirection](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~SetExtractionDirection.html).

## Remarks

The types of entities that define the extraction direction are:

- Face
- Plane
- Edge
- Vertex
- Sketch line
- Sketch point

There can be two entities because two sketch points can specify a direction.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)
[ICoreFeatureData::GetExtractionDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~GetExtractionDirection.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
