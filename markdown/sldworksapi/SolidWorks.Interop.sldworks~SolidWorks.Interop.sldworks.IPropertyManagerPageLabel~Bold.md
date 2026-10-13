---
title: "Bold Property (IPropertyManagerPageLabel)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageLabel"
member: "Bold"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Bold.html"
---

# Bold Property (IPropertyManagerPageLabel)

Gets or sets whether the range of specified characters are bolded in this ProperytManager label.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bold( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Boolean

instance.Bold(StartChar, EndChar) = value

value = instance.Bold(StartChar, EndChar)
```

### C#

```csharp
System.bool Bold(
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

### C++/CLI

```cpp
property System.bool Bold {
   System.bool get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartChar`: 0-based index value of start character
- `EndChar`: 0-based index value of end character

### Property Value

TRUE to bold the specified range of characters, FALSE to not

## VBA Syntax

See [PropertyManagerPageLabel::Bold](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageLabel~Bold.html).

## See Also

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.html)
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
