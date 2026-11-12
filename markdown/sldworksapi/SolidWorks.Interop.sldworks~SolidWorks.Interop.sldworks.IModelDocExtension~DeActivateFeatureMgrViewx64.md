---
title: "DeActivateFeatureMgrViewx64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeActivateFeatureMgrViewx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeActivateFeatureMgrViewx64.html"
---

# DeActivateFeatureMgrViewx64 Method (IModelDocExtension)

Deactivates a tab in the FeatureManager design tree view in x64 applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeActivateFeatureMgrViewx64( _
   ByRef AppView As System.Long _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppView As System.Long
Dim value As System.Boolean

value = instance.DeActivateFeatureMgrViewx64(AppView)
```

### C#

```csharp
System.bool DeActivateFeatureMgrViewx64(
   ref System.long AppView
)
```

### C++/CLI

```cpp
System.bool DeActivateFeatureMgrViewx64(
   System.int64% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`: Pointer to the FeatureManager design tree view to deactivate

### Return Value

True if view deactivated, false if not

## VBA Syntax

See [ModelDocExtension::DeActivateFeatureMgrViewx64](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeActivateFeatureMgrViewx64.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html)
[IModelDocExtension::AddFeatureMgrView3x64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddFeatureMgrView3x64.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
