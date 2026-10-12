---
title: "SaveDraftingStandard Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveDraftingStandard"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard.html"
---

# SaveDraftingStandard Method (IModelDocExtension)

Saves the current custom drafting standard to a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveDraftingStandard( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveDraftingStandard(FileName)
```

### C#

```csharp
System.bool SaveDraftingStandard(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveDraftingStandard(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename for the current custom drafting standard to save to a file

### Return Value

True if the current custom drafting standard is saved to a file, false if not

## VBA Syntax

See [ModelDocExtension::SaveDraftingStandard](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveDraftingStandard.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.html)
[IModelDocExtension::DeleteDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.html)
[IModelDocExtension::GetDraftingStandardNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.html)
[IModelDocExtension::LoadDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard.html)
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
