---
title: "LoadDraftingStandard Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "LoadDraftingStandard"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard.html"
---

# LoadDraftingStandard Method (IModelDocExtension)

Loads a custom drafting standard from a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadDraftingStandard( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean

value = instance.LoadDraftingStandard(FileName)
```

### C#

```csharp
System.bool LoadDraftingStandard(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool LoadDraftingStandard(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of the drafting standard to load

### Return Value

True if the specified drafting standard is loaded, false if not

## VBA Syntax

See [ModelDocExtension::LoadDraftingStandard](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~LoadDraftingStandard.html).

## Examples

[Change Drafting Standard to Custom (VBA)](Change_Drafting_Standard_to_Custom_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.html)
[IModelDocExtension::DeleteDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.html)
[IModelDocExtension::GetDraftingStandardNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.html)
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.html)
[IModelDocExtension::SaveDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
