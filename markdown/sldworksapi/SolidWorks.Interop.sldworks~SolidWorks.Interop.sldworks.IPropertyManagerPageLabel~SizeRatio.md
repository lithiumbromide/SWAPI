---
title: "SizeRatio Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "SizeRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~SizeRatio.html"
---

# SizeRatio Property (IPropertyManagerPageLabel)

Gets or sets the size of the specified characters in this PropertyManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property SizeRatio( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Double

instance.SizeRatio(StartChar, EndChar) = value

value = instance.SizeRatio(StartChar, EndChar)
```

### C#

```csharp
System.double SizeRatio(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.double SizeRatio {
   System.double get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

Ratio for the height of the characters relative to their expected heights; >0 increases their heights and <0 decreases their height

## VBA Syntax

See [PropertyManagerPageLabel::SizeRatio](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~SizeRatio.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
