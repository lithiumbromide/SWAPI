---
title: "IGetPartingSurfaces Method (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "IGetPartingSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.html"
---

# IGetPartingSurfaces Method (IToolingSplitFeatureData)

Gets the parting surface bodies in this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPartingSurfaces( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetPartingSurfaces(Count)
```

### C#

```csharp
Body2 IGetPartingSurfaces(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetPartingSurfaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of parting surface bodies

### Return Value

- in-process, unmanaged C++: Pointer to an array of parting surface [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IToolingSplitFeatureData::GetPartingSurfacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount.html) before calling this method to get Count.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)
[IToolingSplitFeatureData::ISetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces.html)
[IToolingSplitFeatureData::PartingSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
