---
title: "GetDimensionItemCount Method (IPMIDimensionData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionData"
member: "GetDimensionItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemCount.html"
---

# GetDimensionItemCount Method (IPMIDimensionData)

Gets the number of dimension items in this PMI dimension annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimensionItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionData
Dim value As System.Integer

value = instance.GetDimensionItemCount()
```

### C#

```csharp
System.int GetDimensionItemCount()
```

### C++/CLI

```cpp
System.int GetDimensionItemCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of dimension items

## VBA Syntax

See [PMIDimensionData::GetDimensionItemCount](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionData~GetDimensionItemCount.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html)
[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.html)
[IPMIDimensionData::GetDimensionItemAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemAtIndex.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
