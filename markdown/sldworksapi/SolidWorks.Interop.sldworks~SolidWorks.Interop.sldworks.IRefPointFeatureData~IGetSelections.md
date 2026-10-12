---
title: "IGetSelections Method (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "IGetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~IGetSelections.html"
---

# IGetSelections Method (IRefPointFeatureData)

Gets the selected entities to use to create the reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelections( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetSelections(Count)
```

### C#

```csharp
System.object IGetSelections(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetSelections(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of selected entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of selected entities of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [RefPointFeatureData::IGetSelections](ms-its:sldworksapivb6.chm::/sldworks~RefPointFeatureData~IGetSelections.html).

## Remarks

Call [IRefPointFeatureData::GetSelectionsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)
[IRefPointFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections.html)
[IRefPointFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
