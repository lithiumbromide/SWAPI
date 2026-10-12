---
title: "HasLegacyCThreads Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HasLegacyCThreads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.html"
---

# HasLegacyCThreads Method (IModelDocExtension)

Gets whether this model has legacy cosmetic threads.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasLegacyCThreads() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.HasLegacyCThreads()
```

### C#

```csharp
System.bool HasLegacyCThreads()
```

### C++/CLI

```cpp
System.bool HasLegacyCThreads();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model has legacy cosmetic threads, false if not

## VBA Syntax

See [ModelDocExtension::HasLegacyCThreads](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~HasLegacyCThreads.html).

## Remarks

If this method returns true, you can call [IModelDocExtension::UpgradeLegacyCThreads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCThreads.html) to upgrade cosmetic thread features to the latest cosmetic thread architecture.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[IView::GetCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.html)
[IView::GetFirstCThread Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.html)

## Availability

SOLIDWORKS 2022 SP02, Revision Number 30.2
