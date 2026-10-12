---
title: "DeleteDraftingStandard Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteDraftingStandard"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.html"
---

# DeleteDraftingStandard Method (IModelDocExtension)

Delete the current custom drafting standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDraftingStandard() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.DeleteDraftingStandard()
```

### C#

```csharp
System.bool DeleteDraftingStandard()
```

### C++/CLI

```cpp
System.bool DeleteDraftingStandard();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the current custom drfting standard is deleted, false if not

## VBA Syntax

See [ModelDocExtension::DeleteDraftingStandard](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeleteDraftingStandard.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.html)
[IModelDocExtension::GetDraftingStandardNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.html)
[IModelDocExtension::LoadDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard.html)
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.html)
[IModelDocExtension::SaveDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
