---
title: "ReplaceEntitiesAtEnd1 Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "ReplaceEntitiesAtEnd1"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~ReplaceEntitiesAtEnd1.html"
---

# ReplaceEntitiesAtEnd1 Method (ICWCable)

Removes the entities at End 1 of this linkage rod connector and replaces them with the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReplaceEntitiesAtEnd1( _
   ByVal selDispArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
Dim selDispArray As System.Object

instance.ReplaceEntitiesAtEnd1(selDispArray)
```

### C#

```csharp
void ReplaceEntitiesAtEnd1(
   System.object selDispArray
)
```

### C++/CLI

```cpp
void ReplaceEntitiesAtEnd1(
   System.Object^ selDispArray
)
```

### Parameters

- `selDispArray`: Array containing a vertex, edge(s), or face for End 1 (see **Remarks**)

## VBA Syntax

See [CWCable::ReplaceEntitiesAtEnd1](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~ReplaceEntitiesAtEnd1.html).

## Remarks

Specify selDispArray with an array containing the following object(s) obtained by using [IModelDocExtension::SelectByRay](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) and [ISelectionMgr::GetSelectedObject6](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html):

- Vertex
- 1 or 2 circular edges (on same cylindrical face for shells)
- Planar face or cylindrical face (for solid bodies)

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
