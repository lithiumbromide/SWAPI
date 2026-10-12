---
title: "EntitiesToMate Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IDistanceMateFeatureData)

Gets or sets the entities to mate in this distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of entities to mate (see **Remarks**)

## VBA Syntax

See [DistanceMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~EntitiesToMate.html).

## Examples

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html) examples.

## Remarks

You can create distance mates with the following mate entity combinations:

| Mate entity/Mate entity | IRefAxis , IFace2 (cone) | ICurve (arc, spline, helix) | IRefAxis, IFace2 (cylinder) | IEdge , IRefAxis, ICenterLine , ISketchLine (line) | IRefPlane , IFace2 | IRefPoint , IVertex , ISketchPoint | ISurface , IFace2 (sphere) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IRefAxis, IFace2 (cone) | ● Both cones must be of the same half angle |  |  |  |  |  |  |
| ICurve (arc, spline, helix) |  |  |  |  |  | ● |  |
| IRefAxis, IFace2 (cylinder) |  |  | ● | ● | ● | ● |  |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) |  |  | ● | ● | ● | ● | ● |
| IRefPlane, IFace2 |  |  | ● | ● | ● | ● | ● |
| IRefPoint, IVertex, ISketchPoint |  | ● | ● | ● | ● | ● | ● |
| ISurface, IFace2 (sphere) |  |  |  | ● | ● | ● | ● |

## See Also

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
