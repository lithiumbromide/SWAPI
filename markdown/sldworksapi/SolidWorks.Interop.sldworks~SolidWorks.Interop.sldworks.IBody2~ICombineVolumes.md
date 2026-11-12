---
title: "ICombineVolumes Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICombineVolumes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICombineVolumes.html"
---

# ICombineVolumes Method (IBody2)

Combines the volumes of two bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICombineVolumes( _
   ByVal ToolBody As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ToolBody As Body2

instance.ICombineVolumes(ToolBody)
```

### C#

```csharp
void ICombineVolumes(
   Body2 ToolBody
)
```

### C++/CLI

```cpp
void ICombineVolumes(
   Body2^ ToolBody
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToolBody`: Pointer to the [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to be used as the tool

## VBA Syntax

See [Body2::ICombineVolumes](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICombineVolumes.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
