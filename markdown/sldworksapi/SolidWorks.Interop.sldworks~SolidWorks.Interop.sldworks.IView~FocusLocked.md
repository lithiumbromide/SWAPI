---
title: "FocusLocked Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "FocusLocked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FocusLocked.html"
---

# FocusLocked Property (IView)

Gets or sets whether or not focus is locked on this view.

## Syntax

### Visual Basic (Declaration)

```vb
Property FocusLocked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
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

True if focus is locked on the view, false if not

## VBA Syntax

See [View::FocusLocked](ms-its:sldworksapivb6.chm::/sldworks~View~FocusLocked.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[ISheet::FocusLocked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~FocusLocked.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
