---
title: "IGetSelections Method (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "IGetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~IGetSelections.html"
---

# IGetSelections Method (IRefPlaneFeatureData)

Gets the selected entities used to create this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelections( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
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

- `Count`: Number of selected entities to use to create this reference plane

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRefPlaneFeatureData::GetSelectionsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~GetSelectionsCount.html) to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Selections.html)
[IRefPlaneFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
