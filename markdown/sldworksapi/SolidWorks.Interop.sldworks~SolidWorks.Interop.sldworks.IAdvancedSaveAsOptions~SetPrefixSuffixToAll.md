---
title: "SetPrefixSuffixToAll Method (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "SetPrefixSuffixToAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SetPrefixSuffixToAll.html"
---

# SetPrefixSuffixToAll Method (IAdvancedSaveAsOptions)

Sets a prefix and/or a suffix on all component reference names.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPrefixSuffixToAll( _
   ByVal PrefixString As System.String, _
   ByVal SuffixString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions
Dim PrefixString As System.String
Dim SuffixString As System.String

instance.SetPrefixSuffixToAll(PrefixString, SuffixString)
```

### C#

```csharp
void SetPrefixSuffixToAll(
   System.string PrefixString,
   System.string SuffixString
)
```

### C++/CLI

```cpp
void SetPrefixSuffixToAll(
   System.String^ PrefixString,
   System.String^ SuffixString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PrefixString`: Prefix
- `SuffixString`: Suffix

## VBA Syntax

See [AdvancedSaveAsOptions::SetPrefixSuffixToAll](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~SetPrefixSuffixToAll.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## Remarks

This method applies a prefix/suffix to the names of all references except the top-level document. After calling this method, call [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.html) to modify the name and path of individual references and/or the top-level assembly.

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
