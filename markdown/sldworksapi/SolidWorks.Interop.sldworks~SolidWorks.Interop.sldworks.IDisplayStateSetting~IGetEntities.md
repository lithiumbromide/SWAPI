---
title: "IGetEntities Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "IGetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities.html"
---

# IGetEntities Method (IDisplayStateSetting)

Gets the entities for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntities( _
   ByVal EntityCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim EntityCount As System.Integer
Dim value As System.Object

value = instance.IGetEntities(EntityCount)
```

### C#

```csharp
System.object IGetEntities(
   System.int EntityCount
)
```

### C++/CLI

```cpp
System.Object^ IGetEntities(
   System.int EntityCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityCount`: Number of entities

### Return Value

- in-process, unmanaged C++: Pointer to an array entities
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IDisplayStateSetting::GetEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetEntityCount.html) to populate EntityCount.

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.html)
[IDisplayStateSetting::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
