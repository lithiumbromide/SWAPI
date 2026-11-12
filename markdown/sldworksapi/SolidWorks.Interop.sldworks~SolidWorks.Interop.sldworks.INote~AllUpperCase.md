---
title: "AllUpperCase Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "AllUpperCase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AllUpperCase.html"
---

# AllUpperCase Property (INote)

Gets or sets whether the text of this note is all uppercase.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllUpperCase As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.AllUpperCase = value

value = instance.AllUpperCase
```

### C#

```csharp
System.bool AllUpperCase {get; set;}
```

### C++/CLI

```cpp
property System.bool AllUpperCase {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the text of this note is all uppercase, false if not

## VBA Syntax

See [Note::AllUpperCase](ms-its:sldworksapivb6.chm::/sldworks~Note~AllUpperCase.html).

## Examples

[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)
[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
