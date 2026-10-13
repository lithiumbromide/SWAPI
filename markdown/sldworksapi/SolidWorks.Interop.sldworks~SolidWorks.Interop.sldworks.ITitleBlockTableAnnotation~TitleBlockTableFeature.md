---
title: "TitleBlockTableFeature Property (ITitleBlockTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlockTableAnnotation"
member: "TitleBlockTableFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation~TitleBlockTableFeature.html"
---

# TitleBlockTableFeature Property (ITitleBlockTableAnnotation)

Gets the title block table feature associated with this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TitleBlockTableFeature As TitleBlockTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlockTableAnnotation
Dim value As TitleBlockTableFeature

value = instance.TitleBlockTableFeature
```

### C#

```csharp
TitleBlockTableFeature TitleBlockTableFeature {get;}
```

### C++/CLI

```cpp
property TitleBlockTableFeature^ TitleBlockTableFeature {
   TitleBlockTableFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[TitleBlockTableFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableFeature.html)

## VBA Syntax

See [TitleBlockTableAnnotation::TitleBlockTableFeature](ms-its:sldworksapivb6.chm::/sldworks~TitleBlockTableAnnotation~TitleBlockTableFeature.html).

## Examples

[Get Title Block Tables (VBA)](Get_Title_Block_Tables_Example_VB6.htm)
[Get Title Block Tables (VB.NET)](Get_Title_Block_Tables_Example_VBNET.htm)
[Get Title Block Tables (C#)](Get_Title_Block_Tables_Example_CSharp.htm)

## See Also

[ITitleBlockTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation.html)
[ITitleBlockTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
