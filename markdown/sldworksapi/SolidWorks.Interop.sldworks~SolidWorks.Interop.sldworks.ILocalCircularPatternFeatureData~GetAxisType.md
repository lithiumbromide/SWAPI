---
title: "GetAxisType Method (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "GetAxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetAxisType.html"
---

# GetAxisType Method (ILocalCircularPatternFeatureData)

Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Integer

value = instance.GetAxisType()
```

### C#

```csharp
System.int GetAxisType()
```

### C++/CLI

```cpp
System.int GetAxisType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Axis type used to create the circular pattern:

- 0 = reference axis
- 1 = edge
- 2 = dimension

## VBA Syntax

See [LocalCircularPatternFeatureData::GetAxisType](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~GetAxisType.html).

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Axis.html)
[ILocalCircularPatternFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ReverseDirection.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
