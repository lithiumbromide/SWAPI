---
title: "GetFrameAtIndex Method (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "GetFrameAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFrameAtIndex.html"
---

# GetFrameAtIndex Method (IPMIGtolData)

Gets the data of the frame at the specified index of this PMI Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFrameAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetFrameAtIndex(Index)
```

### C#

```csharp
System.object GetFrameAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetFrameAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the frame to get

### Return Value

[IPMIFrameData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)

## VBA Syntax

See [PMIGtolData::GetFrameAtIndex](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~GetFrameAtIndex.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

Use [IPMIGtolData::GetFrameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFrameCount.html) to determine Index.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
