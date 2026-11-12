---
title: "GetVertices Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertices.html"
---

# GetVertices Method (IBody2)

Gets the vertices in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertices() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetVertices()
```

### C#

```csharp
System.object GetVertices()
```

### C++/CLI

```cpp
System.Object^ GetVertices();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [vertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) in this body

## VBA Syntax

See [Body2::GetVertices](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetVertices.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IGetVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetVertices.html)
[GetVertexCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertexCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
