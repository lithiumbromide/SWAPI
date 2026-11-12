---
title: "TransformValue Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TransformValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformValue.html"
---

# TransformValue Property (IMoveCopyBodyFeatureData)

Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double

instance.TransformValue = value

value = instance.TransformValue
```

### C#

```csharp
System.double TransformValue {get; set;}
```

### C++/CLI

```cpp
property System.double TransformValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters or angle in radians

## VBA Syntax

See [MoveCopyBodyFeatureData::TransformValue](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TransformValue.html).

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
