---
title: "NextReference Method (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "NextReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~NextReference.html"
---

# NextReference Method (IRibFeatureData2)

Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours.

## Syntax

### Visual Basic (Declaration)

```vb
Function NextReference() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Integer

value = instance.NextReference()
```

### C#

```csharp
System.int NextReference()
```

### C++/CLI

```cpp
System.int NextReference();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Index of the entity that is used

## VBA Syntax

See [RibFeatureData2::NextReference](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~NextReference.html).

## Remarks

This method cycles through the entities. It starts at the beginning again once the last entity is reached.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
