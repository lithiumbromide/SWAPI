---
title: "ReferenceOffsetStartType Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "ReferenceOffsetStartType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStartType.html"
---

# ReferenceOffsetStartType Property (IPartialEdgeFilletData)

Gets the type of [offset reference for the start condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.html) for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceOffsetStartType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Integer

value = instance.ReferenceOffsetStartType
```

### C#

```csharp
System.int ReferenceOffsetStartType {get;}
```

### C++/CLI

```cpp
property System.int ReferenceOffsetStartType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Start condition offset reference type as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [PartialEdgeFilletData::ReferenceOffsetStartType](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~ReferenceOffsetStartType.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
