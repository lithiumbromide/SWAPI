---
title: "GetGtolBoxCount Method (IPMIFrameData)"
project: "SOLIDWORKS API Help"
interface: "IPMIFrameData"
member: "GetGtolBoxCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolBoxCount.html"
---

# GetGtolBoxCount Method (IPMIFrameData)

Gets the number of tolerance boxes in this Gtol frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGtolBoxCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIFrameData
Dim value As System.Integer

value = instance.GetGtolBoxCount()
```

### C#

```csharp
System.int GetGtolBoxCount()
```

### C++/CLI

```cpp
System.int GetGtolBoxCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of Gtol tolerance boxes

## VBA Syntax

See [PMIFrameData::GetGtolBoxCount](ms-its:sldworksapivb6.chm::/sldworks~PMIFrameData~GetGtolBoxCount.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
