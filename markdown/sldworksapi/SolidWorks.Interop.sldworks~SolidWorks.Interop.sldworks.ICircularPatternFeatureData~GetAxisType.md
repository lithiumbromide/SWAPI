---
title: "GetAxisType Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetAxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetAxisType.html"
---

# GetAxisType Method (ICircularPatternFeatureData)

Gets the type of geometry used to determine the direction of this circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

Geometry type used to create the circular pattern:

- 0 = reference axis
- 1 = edge
- 2 = dimension
- 3 = sketch line

## VBA Syntax

See [CircularPatternFeatureData::GetAxisType](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetAxisType.html).

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
