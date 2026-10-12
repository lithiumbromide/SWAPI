---
title: "ISetSelections Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "ISetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.html"
---

# ISetSelections Method (IRefAxisFeatureData)

Sets the entities for this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetSelections( _
   ByVal Count As System.Integer, _
   ByRef EntArr As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim Count As System.Integer
Dim EntArr As System.Object
Dim value As System.Boolean

value = instance.ISetSelections(Count, EntArr)
```

### C#

```csharp
System.bool ISetSelections(
   System.int Count,
   ref System.object EntArr
)
```

### C++/CLI

```cpp
System.bool ISetSelections(
   System.int Count,
   System.Object^% EntArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities
- `EntArr`: - in-process,unmanaged C++: Pointer to an array of entities for this reference axis feature
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the method executed, false if not

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.html)
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.html)
[IRefAxisFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.html)
[IRefAxisFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
