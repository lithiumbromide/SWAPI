---
title: "GetAdvancedSaveAsOptions Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetAdvancedSaveAsOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.html"
---

# GetAdvancedSaveAsOptions Method (IModelDocExtension)

Gets the advanced **File > Save As** options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAdvancedSaveAsOptions( _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Object

value = instance.GetAdvancedSaveAsOptions(Options)
```

### C#

```csharp
System.object GetAdvancedSaveAsOptions(
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ GetAdvancedSaveAsOptions(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Save with references options as defined in [swSaveWithReferencesOptions](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveWithReferencesOptions_e.html) (see **Remarks**)

### Return Value

[IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)

## VBA Syntax

See [ModelDocExtension::GetAdvancedSaveAsOptions](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetAdvancedSaveAsOptions.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## Remarks

Call this method before calling [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html).

[IAdvancedSaveAsOptions::GetItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.html) returns a list of items according to how the Options parameter is specified in this method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
