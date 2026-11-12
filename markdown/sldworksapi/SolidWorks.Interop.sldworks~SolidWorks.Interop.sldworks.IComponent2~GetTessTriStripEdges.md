---
title: "GetTessTriStripEdges Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetTessTriStripEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripEdges.html"
---

# GetTessTriStripEdges Method (IComponent2)

Gets the edge IDs for the triangle strips.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetTessTriStripEdges()
```

### C#

```csharp
System.object GetTessTriStripEdges()
```

### C++/CLI

```cpp
System.Object^ GetTessTriStripEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the list of edge IDs

## VBA Syntax

See [Component2::GetTessTriStripEdges](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetTessTriStripEdges.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
