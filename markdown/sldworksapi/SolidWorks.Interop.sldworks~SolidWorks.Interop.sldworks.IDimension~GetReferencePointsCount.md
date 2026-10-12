---
title: "GetReferencePointsCount Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetReferencePointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.html"
---

# GetReferencePointsCount Method (IDimension)

Gets the number of reference points for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencePointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Integer

value = instance.GetReferencePointsCount()
```

### C#

```csharp
System.int GetReferencePointsCount()
```

### C++/CLI

```cpp
System.int GetReferencePointsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of dimension reference points

## VBA Syntax

See [Dimension::GetReferencePointsCount](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetReferencePointsCount.html).

## Remarks

Call this method before calling [IDimension::IGetReferencePoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetReferencePoints.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.html)
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.html)

## Availability

SOLIDWORKS 2004 Revision Number 12.0
