---
title: "ShowSheetMetalBendNotes Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ShowSheetMetalBendNotes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.html"
---

# ShowSheetMetalBendNotes Property (IView)

Gets or sets whether to show sheet metal bend notes.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowSheetMetalBendNotes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.ShowSheetMetalBendNotes = value

value = instance.ShowSheetMetalBendNotes
```

### C#

```csharp
System.bool ShowSheetMetalBendNotes {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowSheetMetalBendNotes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show sheet metal bend notes, false to not

## VBA Syntax

See [View::ShowSheetMetalBendNotes](ms-its:sldworksapivb6.chm::/sldworks~View~ShowSheetMetalBendNotes.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
