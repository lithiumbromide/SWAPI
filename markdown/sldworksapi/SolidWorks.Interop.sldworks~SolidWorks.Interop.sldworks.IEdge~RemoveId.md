---
title: "RemoveId Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "RemoveId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveId.html"
---

# RemoveId Method (IEdge)

Removes the edge ID assigned to this edge of an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveId()
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge

instance.RemoveId()
```

### C#

```csharp
void RemoveId()
```

### C++/CLI

```cpp
void RemoveId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Edge::RemoveId](ms-its:sldworksapivb6.chm::/sldworks~Edge~RemoveId.html).

## Remarks

SOLIDWORKS uses an edge ID to track edges of imported bodies.

The ID of the edge of an imported body:

- is not saved with the document.
- must be unique.
- can be changed by any third-party application. The intent is that if you [assign an ID to an edge of an imported body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.html), you can refer to that edge within your application.
- is not a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) or [tracking ID](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm).

Use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object to store data with an edge.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.html)
[IEdge::SetId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
