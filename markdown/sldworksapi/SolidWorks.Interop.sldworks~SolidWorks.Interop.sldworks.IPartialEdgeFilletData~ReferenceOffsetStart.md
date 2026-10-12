---
title: "ReferenceOffsetStart Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "ReferenceOffsetStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.html"
---

# ReferenceOffsetStart Property (IPartialEdgeFilletData)

Gets the offset reference for the start condition for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceOffsetStart As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Object

value = instance.ReferenceOffsetStart
```

### C#

```csharp
System.object ReferenceOffsetStart {get;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceOffsetStart {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset reference (2D/3D sketch [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html), reference [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html))

## VBA Syntax

See [PartialEdgeFilletData::ReferenceOffsetStart](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~ReferenceOffsetStart.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::StartCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.html) is swSimpleFilletPartialEdgeCondition_e.PartialEdgeReferenceOffset.

Use [IPartialEdgeFilletData::ReferenceOffsetStartType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStartType.html) to get the type of object returned by this property.

To modify reference offset for the start condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
