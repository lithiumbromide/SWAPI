---
title: "Edge Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "Edge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Edge.html"
---

# Edge Property (IThreadFeatureData)

Gets or sets the entity where to start the helix of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edge As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As Edge

instance.Edge = value

value = instance.Edge
```

### C#

```csharp
Edge Edge {get; set;}
```

### C++/CLI

```cpp
property Edge^ Edge {
   Edge^ get();
   void set (    Edge^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Planar circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) (see **Remarks**)

## VBA Syntax

See [ThreadFeatureData::Edge](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~Edge.html).

## Examples

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html) examples.

## Remarks

Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) with Mark = 1 to select the edge.

If this property does not set a planar circular edge, then you must use [IThreadFeatureData::StartEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~StartEntity.html) to specify the start location of this thread's helix.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
