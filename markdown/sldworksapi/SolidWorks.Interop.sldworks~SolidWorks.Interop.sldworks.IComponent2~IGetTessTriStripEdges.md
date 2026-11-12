---
title: "IGetTessTriStripEdges Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTessTriStripEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStripEdges.html"
---

# IGetTessTriStripEdges Method (IComponent2)

Gets the edge IDs for the triangle strips.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStripEdges() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IGetTessTriStripEdges()
```

### C#

```csharp
System.int IGetTessTriStripEdges()
```

### C++/CLI

```cpp
System.int IGetTessTriStripEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of type long containing the list of edge ID

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStripEdges.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
