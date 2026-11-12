---
title: "GetParagraphs Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetParagraphs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetParagraphs.html"
---

# GetParagraphs Method (IAnnotation)

Gets the paragraphs in this note annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParagraphs() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetParagraphs()
```

### C#

```csharp
System.object GetParagraphs()
```

### C++/CLI

```cpp
System.Object^ GetParagraphs();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)

## VBA Syntax

See [Annotation::GetParagraphs](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetParagraphs.html).

## Examples

[Get and Set Paragraph Properties (VBA)](Get_and_Set_Paragraph_Properties_Example_VB.htm)
[Get and Set Paragraph Properties (VB.NET)](Get_and_Set_Paragraph_Properties_Example_VBNET.htm)
[Get and Set Paragraph Properties (C#)](Get_and_Set_Paragraph_Properties_Example_CSharp.htm)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
