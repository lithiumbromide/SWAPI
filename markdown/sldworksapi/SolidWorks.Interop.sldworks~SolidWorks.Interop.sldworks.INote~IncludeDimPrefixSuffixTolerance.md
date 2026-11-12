---
title: "IncludeDimPrefixSuffixTolerance Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IncludeDimPrefixSuffixTolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IncludeDimPrefixSuffixTolerance.html"
---

# IncludeDimPrefixSuffixTolerance Property (INote)

Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDimPrefixSuffixTolerance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.IncludeDimPrefixSuffixTolerance = value

value = instance.IncludeDimPrefixSuffixTolerance
```

### C#

```csharp
System.bool IncludeDimPrefixSuffixTolerance {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDimPrefixSuffixTolerance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include the dimension prefix, suffix, and tolerance; false to not

## VBA Syntax

See [Note::IncludeDimPrefixSuffixTolerance](ms-its:sldworksapivb6.chm::/sldworks~Note~IncludeDimPrefixSuffixTolerance.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
