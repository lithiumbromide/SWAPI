---
title: "GetFirstPoint Method (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "GetFirstPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFirstPoint.html"
---

# GetFirstPoint Method (IPMIGtolData)

Gets the label of the first point for tolerances applied between two points or entities in this PMI Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstPoint() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.String

value = instance.GetFirstPoint()
```

### C#

```csharp
System.string GetFirstPoint()
```

### C++/CLI

```cpp
System.String^ GetFirstPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Label of the first point

## VBA Syntax

See [PMIGtolData::GetFirstPoint](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~GetFirstPoint.html).

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)
[IPMIGtolData::GetSecondPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetSecondPoint.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
