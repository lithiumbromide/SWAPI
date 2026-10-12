---
title: "CheckVersionCompatibility Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CheckVersionCompatibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CheckVersionCompatibility.html"
---

# CheckVersionCompatibility Method (IModelDocExtension)

Checks whether a document can be saved in the file format for an earlier version of SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckVersionCompatibility( _
   ByVal Version As System.Integer, _
   ByVal showDialog As System.Integer, _
   ByRef Incompatibilities As System.Object, _
   ByRef Warnings As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Version As System.Integer
Dim showDialog As System.Integer
Dim Incompatibilities As System.Object
Dim Warnings As System.Object
Dim value As System.Integer

value = instance.CheckVersionCompatibility(Version, showDialog, Incompatibilities, Warnings)
```

### C#

```csharp
System.int CheckVersionCompatibility(
   System.int Version,
   System.int showDialog,
   out System.object Incompatibilities,
   out System.object Warnings
)
```

### C++/CLI

```cpp
System.int CheckVersionCompatibility(
   System.int Version,
   System.int showDialog,
   [Out] System.Object^ Incompatibilities,
   [Out] System.Object^ Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Version`: The previous file format to check for compatibility. (See [swSaveToVersion_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveToVersion_e.html))
- `showDialog`: Display the compatibility results dialog. (See [swCompatibilityDialogOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCompatibilityDialogOptions_e.html))
- `Incompatibilities`: Array of [IVersionCompatibilityItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html) objects preventing the document from saving to the specified version.
- `Warnings`: Array of [IVersionCompatibilityItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html) objects warning about saving the document to the specified version.

### Return Value

The outcome of the compatibility check (See [swVersionCompatibilityResult_e](ms-its:swConst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVersionCompatibilityResult_e.html) ).

## VBA Syntax

See [ModelDocExtension::CheckVersionCompatibility](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CheckVersionCompatibility.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

**SOLIDWORKS 2026 SP03, Revision Number 34.3**
