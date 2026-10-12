---
title: "GetSecondPoint Method (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "GetSecondPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetSecondPoint.html"
---

# GetSecondPoint Method (IPMIGtolData)

Gets the label of the second point for tolerances applied between two points or entities in this PMI Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSecondPoint() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.String

value = instance.GetSecondPoint()
```

### C#

```csharp
System.string GetSecondPoint()
```

### C++/CLI

```cpp
System.String^ GetSecondPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Label of the second point

## VBA Syntax

See [PMIGtolData::GetSecondPoint](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~GetSecondPoint.html).

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)
[IPMIGtolData::GetFirstPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFirstPoint.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
