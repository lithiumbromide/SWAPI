---
title: "GetVertexCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetVertexCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertexCount.html"
---

# GetVertexCount Method (IBody2)

Gets the number of vertices in this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetVertexCount()
```

### C#

```csharp
System.int GetVertexCount()
```

### C++/CLI

```cpp
System.int GetVertexCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of vertices in this body

## VBA Syntax

See [Body2::GetVertexCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetVertexCount.html).

## Remarks

Call this method before calling [IBody2::IGetVertices](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetVertices.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
