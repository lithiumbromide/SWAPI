---
title: "ViewId Property (ISnapShot)"
project: "SOLIDWORKS API Help"
interface: "ISnapShot"
member: "ViewId"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot~ViewId.html"
---

# ViewId Property (ISnapShot)

Gets the ID of this snapshot.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ViewId As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISnapShot
Dim value As System.Integer

value = instance.ViewId
```

### C#

```csharp
System.int ViewId {get;}
```

### C++/CLI

```cpp
property System.int ViewId {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Snapshot ID

## VBA Syntax

See [SnapShot::ViewId](ms-its:sldworksapivb6.chm::/sldworks~SnapShot~ViewId.html).

## See Also

[ISnapShot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.html)
[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
