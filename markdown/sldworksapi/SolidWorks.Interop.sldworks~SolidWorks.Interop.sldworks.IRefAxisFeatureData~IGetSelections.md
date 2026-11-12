---
title: "IGetSelections Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "IGetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.html"
---

# IGetSelections Method (IRefAxisFeatureData)

Gets the selected entities for this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelections( _
   ByVal Count As System.Integer, _
   ByRef TypeArr As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim Count As System.Integer
Dim TypeArr As System.Integer
Dim value As System.Object

value = instance.IGetSelections(Count, TypeArr)
```

### C#

```csharp
System.object IGetSelections(
   System.int Count,
   out System.int TypeArr
)
```

### C++/CLI

```cpp
System.Object^ IGetSelections(
   System.int Count,
   [Out] System.int TypeArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of selected entities for this reference axis feature
- `TypeArr`: Array of the types of selected entities for this reference axis feature as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

- in-process, unmanaged C++: Array of the selected entities

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRefAxisFeatureData::GetSelectionsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.html)
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.html)
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
