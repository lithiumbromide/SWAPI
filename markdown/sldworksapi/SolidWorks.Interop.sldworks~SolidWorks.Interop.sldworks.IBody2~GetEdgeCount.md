---
title: "GetEdgeCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetEdgeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdgeCount.html"
---

# GetEdgeCount Method (IBody2)

Gets the number of edges for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetEdgeCount()
```

### C#

```csharp
System.int GetEdgeCount()
```

### C++/CLI

```cpp
System.int GetEdgeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of edges

## VBA Syntax

See [Body2::GetEdgeCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetEdgeCount.html).

## Examples

[Get Original Body from Pattern Body (VBA)](Get_Original_Body_from_Pattern_Body_Example_VB.htm)
[Get Original Body from Pattern Body (VB.NET)](Get_Original_Body_from_Pattern_Body_Example_VBNET.htm)
[Get Original Body from Pattern Body (C#)](Get_Original_Body_from_Pattern_Body_Example_CSharp.htm)

## Remarks

Call this method before calling [IBody2::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetEdges.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
