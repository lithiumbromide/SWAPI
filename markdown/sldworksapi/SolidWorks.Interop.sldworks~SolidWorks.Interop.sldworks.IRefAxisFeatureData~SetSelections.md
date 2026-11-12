---
title: "SetSelections Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "SetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.html"
---

# SetSelections Method (IRefAxisFeatureData)

Sets the entities for this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSelections( _
   ByVal EntitiesVar As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim EntitiesVar As System.Object
Dim value As System.Boolean

value = instance.SetSelections(EntitiesVar)
```

### C#

```csharp
System.bool SetSelections(
   System.object EntitiesVar
)
```

### C++/CLI

```cpp
System.bool SetSelections(
   System.Object^ EntitiesVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntitiesVar`: Array of entities for this reference axis feature

### Return Value

True if the method executed, false if not

## VBA Syntax

See [RefAxisFeatureData::SetSelections](ms-its:sldworksapivb6.chm::/sldworks~RefAxisFeatureData~SetSelections.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.html)
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.html)
[IRefAxisFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.html)
[IRefAxisFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
