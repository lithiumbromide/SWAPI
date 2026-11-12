---
title: "CurrentParagraph Property (IParagraphs)"
project: "SOLIDWORKS API Help"
interface: "IParagraphs"
member: "CurrentParagraph"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.html"
---

# CurrentParagraph Property (IParagraphs)

Gets or sets the current paragraph.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentParagraph As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IParagraphs
Dim value As System.Integer

instance.CurrentParagraph = value

value = instance.CurrentParagraph
```

### C#

```csharp
System.int CurrentParagraph {get; set;}
```

### C++/CLI

```cpp
property System.int CurrentParagraph {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0-based index of current paragraph

## VBA Syntax

See [Paragraphs::CurrentParagraph](ms-its:sldworksapivb6.chm::/sldworks~Paragraphs~CurrentParagraph.html).

## Examples

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html) examples.

## Remarks

Before calling any of the methods of [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html), you must call this method to set the current paragraph.

Use [IParagraphs::Count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~Count.html) to determine the index with which to set this property.

## See Also

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.html)
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
