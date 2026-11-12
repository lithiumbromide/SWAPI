---
title: "EntitiesToMate Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IAngleMateFeatureData)

Gets or sets the entities to mate in this angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
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

See [AngleMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~EntitiesToMate.html).

## Examples

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html) examples.

## Remarks

You can create angle mates with the following mate entity combinations:

| Mate entity/Mate entity | IRefAxis (cone, cylinder) | IFace2 (extrusion face, draft is not allowed) | IEdge , IRefAxis, ICenterLine , ISketchLine (line) | IRefPlane |
| --- | --- | --- | --- | --- |
| IRefAxis (cone, cylinder) | ● | ● | ● |  |
| IFace2 (extrusion face, draft is not allowed) | ● | ● | ● |  |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) | ● | ● | ● |  |
| IRefPlane |  |  |  | ● |

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
