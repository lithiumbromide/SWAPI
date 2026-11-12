---
title: "LineOffset Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "LineOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~LineOffset.html"
---

# LineOffset Property (IPropertyManagerPageLabel)

Gets or sets whether to raise or lower the specified characters above or below their baselines, relative to their heights, in this PropertyManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property LineOffset( _
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

instance.LineOffset(StartChar, EndChar) = value

value = instance.LineOffset(StartChar, EndChar)
```

### C#

```csharp
System.double LineOffset(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.double LineOffset {
   System.double get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

Specify:

- 0.0 to show the character on its baseline
- -1.0 to show the character 1 character below its baseline
- +1.0 to show the character 1 character above its baseline

## VBA Syntax

See [PropertyManagerPageLabel::LineOffset](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~LineOffset.html).

## Remarks

Offsetting (i.e., raising or lowering a character above or below its baseline, relative to its height) a character allows you to show that character as a subscript or exponent in an equation.

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
