---
title: "IsLightLockedToModel Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsLightLockedToModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsLightLockedToModel.html"
---

# IsLightLockedToModel Method (IModelDoc2)

Gets whether the specified light is fixed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLightLockedToModel( _
   ByVal LightId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim LightId As System.Integer
Dim value As System.Boolean

value = instance.IsLightLockedToModel(LightId)
```

### C#

```csharp
System.bool IsLightLockedToModel(
   System.int LightId
)
```

### C++/CLI

```cpp
System.bool IsLightLockedToModel(
   System.int LightId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightId`: Light ID

### Return Value

True if the light is fixed, false otherwise

## VBA Syntax

See [ModelDoc2::IsLightLockedToModel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsLightLockedToModel.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::LockLightToModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockLightToModel.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
