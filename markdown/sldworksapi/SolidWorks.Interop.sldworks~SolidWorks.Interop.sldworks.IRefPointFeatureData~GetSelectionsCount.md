---
title: "GetSelectionsCount Method (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "GetSelectionsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount.html"
---

# GetSelectionsCount Method (IRefPointFeatureData)

Gets the number of entities selected to use to create the reference point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
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

Number of selected entities

## VBA Syntax

See [RefPointFeatureData::GetSelectionsCount](ms-its:sldworksapivb6.chm::/sldworks~RefPointFeatureData~GetSelectionsCount.html).

## Remarks

Call this method before calling [IRefPointFeatureData::IGetSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPointFeatureData~IGetSelections.html).

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)
[IRefPointFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections.html)
[IRefPointFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
