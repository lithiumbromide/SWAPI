---
title: "ReadOnly Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "ReadOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ReadOnly.html"
---

# ReadOnly Property (INote)

Gets or sets the read-only state of a note.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReadOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.ReadOnly = value

value = instance.ReadOnly
```

### C#

```csharp
System.bool ReadOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ReadOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the note is read-only, false if not

## VBA Syntax

See [Note::ReadOnly](ms-its:sldworksapivb6.chm::/sldworks~Note~ReadOnly.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
