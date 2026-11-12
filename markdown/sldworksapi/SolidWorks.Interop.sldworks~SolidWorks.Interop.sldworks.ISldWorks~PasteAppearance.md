---
title: "PasteAppearance Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PasteAppearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PasteAppearance.html"
---

# PasteAppearance Method (ISldWorks)

Applies to the specified entity an appearance that has been copied to the clipboard.

## Syntax

### Visual Basic (Declaration)

```vb
Function PasteAppearance( _
   ByVal Object As System.Object, _
   ByVal AppearanceTarget As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Object As System.Object
Dim AppearanceTarget As System.Integer
Dim value As System.Boolean

value = instance.PasteAppearance(Object, AppearanceTarget)
```

### C#

```csharp
System.bool PasteAppearance(
   System.object Object,
   System.int AppearanceTarget
)
```

### C++/CLI

```cpp
System.bool PasteAppearance(
   System.Object^ Object,
   System.int AppearanceTarget
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html), or [part](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) to which to apply a copied appearance; if Null, the copied appearance is applied to an entity that is pre-selected in the graphics area
- `AppearanceTarget`: Appearance target type as defined in [swAppearanceTargetType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppearanceTargetType_e.html); only valid if Object is a face

### Return Value

True if the copied appearance is successfully applied, false if not

## VBA Syntax

See [SldWorks::PasteAppearance](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PasteAppearance.html).

## Examples

[Copy and Paste Appearances (VBA)](Copy_and_Paste_Appearances_Example_VB.htm)
[Copy and Paste Appearances (VB.NET)](Copy_and_Paste_Appearances_Example_VBNET.htm)
[Copy and Paste Appearances (C#)](Copy_and_Paste_Appearances_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CopyAppearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyAppearance.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
