---
title: "GetFinCoFin Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetFinCoFin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetFinCoFin.html"
---

# GetFinCoFin Method (ITessellation)

Gets the ID of the CoFin that is shared by a fin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFinCoFin( _
   ByVal FinId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FinId As System.Integer
Dim value As System.Integer

value = instance.GetFinCoFin(FinId)
```

### C#

```csharp
System.int GetFinCoFin(
   System.int FinId
)
```

### C++/CLI

```cpp
System.int GetFinCoFin(
   System.int FinId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FinId`: Fin ID that to use to return the cofin ID

### Return Value

Long or integer value that describes the ID number of the cofin

## VBA Syntax

See [Tessellation::GetFinCoFin](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetFinCoFin.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
