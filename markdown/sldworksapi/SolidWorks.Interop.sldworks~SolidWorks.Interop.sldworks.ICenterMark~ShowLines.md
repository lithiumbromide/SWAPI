---
title: "ShowLines Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "ShowLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ShowLines.html"
---

# ShowLines Property (ICenterMark)

Gets or sets whether the extension lines are shown in this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowLines As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

instance.ShowLines = value

value = instance.ShowLines
```

### C#

```csharp
System.bool ShowLines {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowLines {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True shows the lines, false does not

## VBA Syntax

See [CenterMark::ShowLines](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~ShowLines.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
