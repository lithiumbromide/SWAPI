---
title: "ReferenceOffsetEndType Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "ReferenceOffsetEndType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEndType.html"
---

# ReferenceOffsetEndType Property (IPartialEdgeFilletData)

Gets the type of [offset reference for the end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEnd.html) for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceOffsetEndType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Integer

value = instance.ReferenceOffsetEndType
```

### C#

```csharp
System.int ReferenceOffsetEndType {get;}
```

### C++/CLI

```cpp
property System.int ReferenceOffsetEndType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition offset reference type as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [PartialEdgeFilletData::ReferenceOffsetEndType](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~ReferenceOffsetEndType.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
