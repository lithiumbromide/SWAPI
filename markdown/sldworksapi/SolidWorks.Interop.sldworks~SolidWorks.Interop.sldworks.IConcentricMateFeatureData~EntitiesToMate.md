---
title: "EntitiesToMate Property (IConcentricMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConcentricMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IConcentricMateFeatureData)

Gets or sets the entities to mate in this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConcentricMateFeatureData
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

Entities to mate (see **Remarks**)

## VBA Syntax

See [ConcentricMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~ConcentricMateFeatureData~EntitiesToMate.html).

## Examples

See the [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html) example.

## Remarks

You can create concentric mates with the following mate entity combinations:

| Mate entity/Mate entity | IEdge (arc, circular edge) | IRefAxis , (cone) | IRefAxis, (cylinder) | IEdge, IRefAxis, ICenterLine , ISketchLine (line) | IRefPoint , IVertex , ISketchPoint | IRefAxis, ISketchPoint, IRefPoint, IVertex (sphere) |
| --- | --- | --- | --- | --- | --- | --- |
| IEdge (arc, circular edge) | ● | ● | ● | ● |  |  |
| IRefAxis (cone) | ● | ● | ● | ● | ● |  |
| IRefAxis (cylinder) | ● | ● | ● | ● | ● | ● |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) | ● | ● | ● |  |  | ● |
| IRefPoint, IVertex, ISketchPoint |  | ● | ● |  |  | ● |
| IRefAxis, IRefPoint, ISketchPoint, IVertex (sphere) |  |  | ● | ● | ● | ● |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html)
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
