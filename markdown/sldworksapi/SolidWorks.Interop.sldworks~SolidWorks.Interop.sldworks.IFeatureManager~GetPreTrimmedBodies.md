---
title: "GetPreTrimmedBodies Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetPreTrimmedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetPreTrimmedBodies.html"
---

# GetPreTrimmedBodies Method (IFeatureManager)

Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by [IFeatureManager::PreTrimSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreTrimSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreTrimmedBodies( _
   ByVal TargetSurface As Body2 _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim TargetSurface As Body2
Dim value As System.Object

value = instance.GetPreTrimmedBodies(TargetSurface)
```

### C#

```csharp
System.object GetPreTrimmedBodies(
   Body2 TargetSurface
)
```

### C++/CLI

```cpp
System.Object^ GetPreTrimmedBodies(
   Body2^ TargetSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TargetSurface`: Target sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

Array of temporary trimmed bodies

## VBA Syntax

See [FeatureManager::GetPreTrimmedBodies](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetPreTrimmedBodies.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::PostTrimSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
