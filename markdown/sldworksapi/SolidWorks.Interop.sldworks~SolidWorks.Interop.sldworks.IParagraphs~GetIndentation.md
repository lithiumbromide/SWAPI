---
title: "GetIndentation Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "GetIndentation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetIndentation.html"
---

# GetIndentation Method (IParagraphs)

Gets the indentation of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIndentation( _
   ByRef FirstlineIndent As System.Double, _
   ByRef Indent As System.Double, _
   ByRef IndentIncrement As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim FirstlineIndent As System.Double
Dim Indent As System.Double
Dim IndentIncrement As System.Double
Dim value As System.Boolean

value = instance.GetIndentation(FirstlineIndent, Indent, IndentIncrement)
```

### C#

```csharp
System.bool GetIndentation(
   out System.double FirstlineIndent,
   out System.double Indent,
   out System.double IndentIncrement
)
```

### C++/CLI

```cpp
System.bool GetIndentation(
   [Out] System.double FirstlineIndent,
   [Out] System.double Indent,
   [Out] System.double IndentIncrement
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstlineIndent`: Indentation of first line
- `Indent`: Indentation of lines other than the first line
- `IndentIncrement`: Amount by which to increment the current indents

### Return Value

True if successful, false if not

## VBA Syntax

See [Paragraphs::GetIndentation](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~GetIndentation.html).

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::SetIndentation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
