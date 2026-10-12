---
title: "GetID Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetID.html"
---

# GetID Method (IEdge)

Gets the edge ID of this edge in an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Edge ID of this edge in an imported body

## VBA Syntax

See [Edge::GetID](ms-its:sldworksapivb6.chm::/sldworks~Edge~GetID.html).

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
[IEdge::SetId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~SetId.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
