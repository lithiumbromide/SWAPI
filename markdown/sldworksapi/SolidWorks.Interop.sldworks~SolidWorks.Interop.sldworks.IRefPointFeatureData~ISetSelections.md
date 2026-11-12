---
title: "ISetSelections Method (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "ISetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections.html"
---

# ISetSelections Method (IRefPointFeatureData)

Sets the number of entities to use to create the reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSelections( _
   ByVal Count As System.Integer, _
   ByRef Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
Dim Count As System.Integer
Dim Entities As System.Object

instance.ISetSelections(Count, Entities)
```

### C#

```csharp
void ISetSelections(
   System.int Count,
   ref System.object Entities
)
```

### C++/CLI

```cpp
void ISetSelections(
   System.int Count,
   System.Object^% Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of selected entities
- `Entities`: - in-process, unmanaged C++: POinter to an array of entities of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)
[IRefPointFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount.html)
[IRefPointFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~IGetSelections.html)
[IRefPointFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
