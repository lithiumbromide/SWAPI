---
title: "EntitiesToMate Property (ITangentMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITangentMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ITangentMateFeatureData)

Gets or sets the entities to mate in this tangent mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITangentMateFeatureData
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

See [TangentMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~TangentMateFeatureData~EntitiesToMate.html).

## Examples

See the [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html) example.

## Remarks

You can create tangent mates with the following mate entity combinations:

| Mate entity/Mate entity | ISurface , IFace2 (cone, cylinder) | IFace2 (extrusion face, draft is not allowed) | IEdge , IRefAxis, ICenterLine , ISketchLine (line) | IRefPlane | ISurface, IFace2 (sphere) | ISurface |
| --- | --- | --- | --- | --- | --- | --- |
| ISurface, IFace2 (cone, cylinder) | ● | ● | ● | ● | ● | ● |
| IFace2 (extrusion face; draft is not allowed) | ● |  |  |  | ● |  |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) | ● |  |  |  | ● |  |
| IRefPlane | ● |  |  |  | ● |  |
| ISurface, IFace2 (sphere) | ● | ● | ● | ● | ● | ● |
| ISurface | ● |  |  |  | ● |  |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[ITangentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html)
[ITangentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
