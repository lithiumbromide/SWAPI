---
title: "Visible Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Visible.html"
---

# Visible Property (INote)

Gets and sets the visibility state of a note during the creation of a block.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True makes the note visible in the block, false does not

## VBA Syntax

See [Note::Visible](ms-its:sldworksapivb6.chm::/sldworks~Note~Visible.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
