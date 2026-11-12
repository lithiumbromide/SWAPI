---
title: "FocusLocked Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "FocusLocked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~FocusLocked.html"
---

# FocusLocked Property (ISheet)

Gets or sets whether focus is locked on this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property FocusLocked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Boolean

instance.FocusLocked = value

value = instance.FocusLocked
```

### C#

```csharp
System.bool FocusLocked {get; set;}
```

### C++/CLI

```cpp
property System.bool FocusLocked {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if focus locked on sheet, false if not

## VBA Syntax

See [Sheet::FocusLocked](ms-its:sldworksapivb6.chm::/sldworks~Sheet~FocusLocked.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[IView::FocusLocked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FocusLocked.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
