---
title: "Copy2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Copy2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy2.html"
---

# Copy2 Method (IBody2)

Gets a copy of this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function Copy2( _
   ByVal PreserveFaceIDs As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim PreserveFaceIDs As System.Boolean
Dim value As System.Object

value = instance.Copy2(PreserveFaceIDs)
```

### C#

```csharp
System.object Copy2(
   System.bool PreserveFaceIDs
)
```

### C++/CLI

```cpp
System.Object^ Copy2(
   System.bool PreserveFaceIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PreserveFaceIDs`: True to copy face IDs, false to create new IDs

### Return Value

Copied IBody2

## VBA Syntax

See [Body2::Copy2](ms-its:sldworksapivb6.chm::/sldworks~Body2~Copy2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
