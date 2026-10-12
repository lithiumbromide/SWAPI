---
title: "SetDroppedFileFeatureName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetDroppedFileFeatureName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileFeatureName.html"
---

# SetDroppedFileFeatureName Method (IAssemblyDoc)

Sets the name of the feature for the recently dropped file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDroppedFileFeatureName( _
   ByVal FeatureName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FeatureName As System.String
Dim value As System.Boolean

value = instance.SetDroppedFileFeatureName(FeatureName)
```

### C#

```csharp
System.bool SetDroppedFileFeatureName(
   System.string FeatureName
)
```

### C++/CLI

```cpp
System.bool SetDroppedFileFeatureName(
   System.String^ FeatureName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatureName`: Feature name

### Return Value

True if the feature name is set, false if not

## VBA Syntax

See [AssemblyDoc::SetDroppedFileFeatureName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetDroppedFileFeatureName.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetDroppedAtEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDroppedAtEntity.html)
[IAssemblyDoc::SetDroppedFileConfigName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.html)
[IAssemblyDoc::SetDroppedFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
