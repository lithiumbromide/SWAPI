---
title: "ConnectionLines Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "ConnectionLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ConnectionLines.html"
---

# ConnectionLines Property (ICenterMark)

Gets or sets the visibility of the connection line of this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConnectionLines As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Integer

instance.ConnectionLines = value

value = instance.ConnectionLines
```

### C#

```csharp
System.int ConnectionLines {get; set;}
```

### C++/CLI

```cpp
property System.int ConnectionLines {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

State of the visibility of the connection line as defined in [swCenterMarkConnectionLine_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkConnectionLine_e.html)

## VBA Syntax

See [CenterMark::ConnectionLines](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~ConnectionLines.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
