---
title: "GetItemsNameAndPath Method (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "GetItemsNameAndPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.html"
---

# GetItemsNameAndPath Method (IAdvancedSaveAsOptions)

Gets all reference components' names and paths.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetItemsNameAndPath( _
   ByRef IdsList As System.Object, _
   ByRef NamesList As System.Object, _
   ByRef PathsList As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions
Dim IdsList As System.Object
Dim NamesList As System.Object
Dim PathsList As System.Object

instance.GetItemsNameAndPath(IdsList, NamesList, PathsList)
```

### C#

```csharp
void GetItemsNameAndPath(
   out System.object IdsList,
   out System.object NamesList,
   out System.object PathsList
)
```

### C++/CLI

```cpp
void GetItemsNameAndPath(
   [Out] System.Object^ IdsList,
   [Out] System.Object^ NamesList,
   [Out] System.Object^ PathsList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdsList`: Array of component reference IDs
- `NamesList`: Array of component reference names
- `PathsList`: Array of component reference paths

## VBA Syntax

See [AdvancedSaveAsOptions::GetItemsNameAndPath](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~GetItemsNameAndPath.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## Remarks

IdsList, NamesList, and PathsList are the same array size and map one to one. Call this method to obtain the current list of component references before calling [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html) to modify them.

This method lists component references according to the Options parameter that was specified in the call to [IModelDocExtension::GetAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
