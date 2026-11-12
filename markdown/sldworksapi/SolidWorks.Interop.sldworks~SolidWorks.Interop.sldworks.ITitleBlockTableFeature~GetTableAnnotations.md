---
title: "GetTableAnnotations Method (ITitleBlockTableFeature)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlockTableFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (ITitleBlockTableFeature)

Gets all of the title block table annotations in this title block table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlockTableFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlockTableAnnotation.html) in this title block table feature

## VBA Syntax

See [TitleBlockTableFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~TitleBlockTableFeature~GetTableAnnotations.html).

## Examples

[Get Title Block Tables (VBA)](Get_Title_Block_Tables_Example_VB6.htm)
[Get Title Block Tables (VB.NET)](Get_Title_Block_Tables_Example_VBNET.htm)
[Get Title Block Tables (C#)](Get_Title_Block_Tables_Example_CSharp.htm)

## See Also

[ITitleBlockTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature.html)
[ITitleBlockTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
