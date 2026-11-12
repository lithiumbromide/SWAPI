---
title: "GetTextFormatCount Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetTextFormatCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.html"
---

# GetTextFormatCount Method (IAnnotation)

Gets the number of text formats for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormatCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.GetTextFormatCount()
```

### C#

```csharp
System.int GetTextFormatCount()
```

### C++/CLI

```cpp
System.int GetTextFormatCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of text formats

## VBA Syntax

See [Annotation::GetTextFormatCount](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetTextFormatCount.html).

## Remarks

The value returned by this method is intended to be used with [IAnnotation::GetUseDocTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetUseDocTextFormat.html), [IAnnotation::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormat.html), [IAnnotation::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetTextFormat.html), [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html), and [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html). The index input argument for these methods must be less than the number returned by this method.

This value is not necessarily the same as the number of text objects within a symbol. For example, there are multiple text objects in a geometric tolerance symbol, but they all share the same text format so SOLIDWORKS returns 1. In fact, for all of the annotations except blocks (and compound notes in documents created in SOLIDWORKS 2015 and earlier), this method should return 1. For blocks and compound notes, each piece of text within the symbol has its own text format, so the return value should match the number of TextFormat objects.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.html)
[IAnnotation::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.html)
[IAnnotation::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.html)
[IAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.html)
[IAnnotation::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0.
