---
title: "IGetFinVertices Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFinVertices"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFinVertices.html"
---

# IGetFinVertices Method (ITessellation)

Gets the IDs of the two vertices that correspond to a fin.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFinVertices( _
   ByVal FinId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Integer

value = instance.IGetFinVertices(FinId)
```

### C#

```csharp
System.int IGetFinVertices(
   System.int FinId
)
```

### C++/CLI

```cpp
System.int IGetFinVertices(
   System.int FinId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FinId`: Fin ID of the fin from which you want to return the vertices

### Return Value

- in-process, unmanaged C++: Pointer to an array of two longs or integers describing the vertices IDs of a fin

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellate::GetFinVertices Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinVertices.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Numbe 9.0
