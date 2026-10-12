---
title: "ModifyItemsNameAndPath Method (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "ModifyItemsNameAndPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html"
---

# ModifyItemsNameAndPath Method (IAdvancedSaveAsOptions)

Modifies the specified reference components with the specified names and paths.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifyItemsNameAndPath( _
   ByVal IdsList As System.Object, _
   ByVal NamesList As System.Object, _
   ByVal PathsList As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions
Dim IdsList As System.Object
Dim NamesList As System.Object
Dim PathsList As System.Object
Dim value As System.Integer

value = instance.ModifyItemsNameAndPath(IdsList, NamesList, PathsList)
```

### C#

```csharp
System.int ModifyItemsNameAndPath(
   System.object IdsList,
   System.object NamesList,
   System.object PathsList
)
```

### C++/CLI

```cpp
System.int ModifyItemsNameAndPath(
   System.Object^ IdsList,
   System.Object^ NamesList,
   System.Object^ PathsList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdsList`: Array of reference component IDs (see **Remarks**)
- `NamesList`: Array of new reference component names
- `PathsList`: Array of new reference component paths

### Return Value

Return code as defined in [swSaveItemsPathError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveItemsPathError_e.html)

## VBA Syntax

See [AdvancedSaveAsOptions::ModifyItemsNameAndPath](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~ModifyItemsNameAndPath.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## Remarks

Before calling this method call:

1. [IAdvancedSaveAsOptions::SetPrefixSuffixToAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SetPrefixSuffixToAll.html)
2. [IAdvancedSaveAsOptions::GetItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.html) to populate IDsList.

IdsList, NamesList, and PathsList are the same array size and map one to one. Use Nothing or null to specify no change to an individual reference in each array.

If you use this method to change the name or path of the top-level document, then it overrides the name or path passed in the Name parameter of [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)
[IAdvancedSaveAsOptions::SaveAsPreviousVersion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
