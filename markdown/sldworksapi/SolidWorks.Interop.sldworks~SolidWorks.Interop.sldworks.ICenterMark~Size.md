---
title: "Size Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Size.html"
---

# Size Property (ICenterMark)

Gets or sets the length of the lines in this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Property Size As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Double

instance.Size = value

value = instance.Size
```

### C#

```csharp
System.double Size {get; set;}
```

### C++/CLI

```cpp
property System.double Size {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of lines

## VBA Syntax

See [CenterMark::Size](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~Size.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
