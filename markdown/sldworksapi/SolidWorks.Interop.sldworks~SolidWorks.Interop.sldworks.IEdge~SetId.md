---
title: "SetId Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "SetId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.html"
---

# SetId Method (IEdge)

Sets the edge ID of this edge of an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetId( _
   ByVal IdIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim IdIn As System.Integer

instance.SetId(IdIn)
```

### C#

```csharp
void SetId(
   System.int IdIn
)
```

### C++/CLI

```cpp
void SetId(
   System.int IdIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdIn`: Edge ID of this edge of an imported body

## VBA Syntax

See [Edge::SetId](ms-its:sldworksapivb6.chm::/sldworks~Edge~SetId.html).

## Remarks

SOLIDWORKS uses this ID to track edges of imported bodies.

The ID of the edge of an imported body:

- is not saved with the document.
- must be unique.
- can be changed by any third-party application. The intent is that if you [assign an ID to an edge of an imported body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.html), you can refer to that edge within your application.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) or [tracking ID](sldworksAPIProgGuide.chm::/OVERVIEW/Tracking_IDs.htm).

Use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object to store data with an edge.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IEdge::RemoveId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~RemoveId.html)
[IEdge::GetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
