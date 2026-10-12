---
title: "GetSelectionsCount Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "GetSelectionsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.html"
---

# GetSelectionsCount Method (IRefAxisFeatureData)

Gets the number of selections that define this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim value As System.Integer

value = instance.GetSelectionsCount()
```

### C#

```csharp
System.int GetSelectionsCount()
```

### C++/CLI

```cpp
System.int GetSelectionsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of selections that define this reference axis featu

## VBA Syntax

See [RefAxisFeatureData::GetSelectionsCount](ms-its:sldworksapivb6.chm::/sldworks~RefAxisFeatureData~GetSelectionsCount.html).

## Remarks

Call this method before calling [IRefAxisFeatureData::IGetSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxisFeatureData~IGetSelections.html).

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.html)
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.html)
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
