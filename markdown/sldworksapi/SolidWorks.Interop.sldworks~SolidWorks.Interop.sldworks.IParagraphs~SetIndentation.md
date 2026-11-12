---
title: "SetIndentation Method (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "SetIndentation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetIndentation.html"
---

# SetIndentation Method (IParagraphs)

Sets the indentation of the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIndentation( _
   ByVal FirstlineIndent As System.Double, _
   ByVal Indent As System.Double, _
   ByVal IndentIncrement As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim FirstlineIndent As System.Double
Dim Indent As System.Double
Dim IndentIncrement As System.Double
Dim value As System.Boolean

value = instance.SetIndentation(FirstlineIndent, Indent, IndentIncrement)
```

### C#

```csharp
System.bool SetIndentation(
   System.double FirstlineIndent,
   System.double Indent,
   System.double IndentIncrement
)
```

### C++/CLI

```cpp
System.bool SetIndentation(
   System.double FirstlineIndent,
   System.double Indent,
   System.double IndentIncrement
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

See [Paragraphs::SetIndentation](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~SetIndentation.html).

## Remarks

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html).

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.html) to update the model.

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)
[IParagraphs::GetIndentation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetIndentation.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
