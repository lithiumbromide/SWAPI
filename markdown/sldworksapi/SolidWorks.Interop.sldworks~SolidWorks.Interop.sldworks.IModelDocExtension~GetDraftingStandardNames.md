---
title: "GetDraftingStandardNames Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetDraftingStandardNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.html"
---

# GetDraftingStandardNames Method (IModelDocExtension)

Get the names of all currently available drafting standards.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftingStandardNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetDraftingStandardNames()
```

### C#

```csharp
System.object GetDraftingStandardNames()
```

### C++/CLI

```cpp
System.Object^ GetDraftingStandardNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the names of all currently available drafting standard names

## VBA Syntax

See [ModelDocExtension::GetDraftingStandardNames](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetDraftingStandardNames.html).

## Examples

[Change Drafting Standard to Custom (VBA)](Change_Drafting_Standard_to_Custom_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.html)
[IModelDocExtension::DeleteDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.html)
[IModelDocExtension::LoadDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard.html)
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.html)
[IModelDocExtension::SaveDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
