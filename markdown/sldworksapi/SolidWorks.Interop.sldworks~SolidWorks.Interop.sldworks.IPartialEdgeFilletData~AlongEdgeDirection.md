---
title: "AlongEdgeDirection Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "AlongEdgeDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~AlongEdgeDirection.html"
---

# AlongEdgeDirection Property (IPartialEdgeFilletData)

Gets which end of the edge to start the fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AlongEdgeDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Boolean

value = instance.AlongEdgeDirection
```

### C#

```csharp
System.bool AlongEdgeDirection {get;}
```

### C++/CLI

```cpp
property System.bool AlongEdgeDirection {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to start the fillet at the start point of the edge, false to start the fillet at the end point of the edge

## VBA Syntax

See [PartialEdgeFilletData::AlongEdgeDirection](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~AlongEdgeDirection.html).

## Remarks

To modify the starting point of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
